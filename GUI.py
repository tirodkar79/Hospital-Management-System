from tkinter import *
from tkinter import messagebox
import mysql.connector

global setting
setting = 0

def doctor():
    global count
    global result
    myconn = mysql.connector.connect(host="localhost", user="root", password="Pratham", database="hospital")

    cur = myconn.cursor()

    try:
        cur.execute("select*from pharmacy")
        result = cur.fetchall()
        count = cur.rowcount


    except:
        myconn.rollback()
    myconn.close()

    home = Toplevel()
    home.geometry("1550x900")
    home.config(bg='snow2')
    home.title("Pharmacy")

    def go_back():
        home.destroy()

    head_label = Label(home, text="Pharmacy", background="turquoise1", foreground="white",
                       font=('Times', 50, 'bold'), width=35).place(x=0, y=30)

    back = Button(home, text='Back', fg='black', font=('arial', 16, 'bold'), bg='turquoise1',
                  relief='raised', bd=10, command=go_back).place(x=1260, y=625)

    id_label = Label(home,text="Medicine Id",bg="snow2",fg = "black",font=('Times', 16, 'bold'),relief = "solid",padx=5,width=10).place(x=158,y=130)

    id_Name = Label(home, text="Medicine Name", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                     width=27).place(x=290, y=130)
    id_quali = Label(home, text="In Stock", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                     width=10).place(x= 626, y=130)
    id_specality = Label(home, text="Expiry date", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                     width=15).place(x=758, y=130)
    id_exp = Label(home, text="Recent Renewal date", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                     width=18).place(x=950, y=130)
    global z
    z = 159
    global flag
    flag =0
    for i in range(0,count):

        pharma_id = result[i][0]
        pharma_name = result[i][1]
        pharma_quantity = result[i][2]
        pharama_exp = result[i][3]
        pharma_recent = result[i][4]


        id_label = Label(home, text= pharma_id, bg="snow2", fg="black", font=('Times', 14), relief="solid",
                         padx=5, width=12).place(x=158,y=z)

        id_Name = Label(home, text= pharma_name, bg="snow2", fg="black", font=('Times', 14), relief="solid", padx=5,
                        width=33).place(x=290, y=z)
        id_quali = Label(home, text= pharma_quantity, bg="snow2", fg="black", font=('Times', 14), relief="solid",
                         padx=5,width=12).place(x=626, y=z)
        id_specality = Label(home, text=pharama_exp, bg="snow2", fg="black", font=('Times', 14), relief="solid",
                             padx=5,
                             width=18).place(x=758, y=z)
        id_exp = Label(home, text=pharma_recent, bg="snow2", fg="black", font=('Times', 14), relief="solid",
                       padx=5,
                       width=21).place(x=950, y=z)
        z+=24

    def add():
        global z
        p_name = StringVar()
        p_quantity = IntVar()
        p_quantity.set("")
        p_exp = StringVar()
        p_recent = StringVar()

        def done():
            global z
            global count
            global setting

            pharma_name = p_name.get()
            pharma_quantity = p_quantity.get()
            pharama_exp = p_exp.get()
            pharma_recent = p_recent.get()

            if (pharma_name != "" and pharma_quantity != "" and pharama_exp != "" and pharma_recent != ""):

                myconn = mysql.connector.connect(host="localhost", user="root", password="Pratham", database="hospital")

                cur = myconn.cursor()



                try:

                    pharma_id = count + 1
                    sql = "insert into pharmacy(pharmacy_id, medicine_name,quantity,expiry_date,r_date) values(%s,%s,%s,%s,%s)"

                    val = (pharma_id, pharma_name, pharma_quantity, pharama_exp, pharma_recent)
                    cur.execute(sql, val)

                    myconn.commit()

                except:
                    print("error")
                    myconn.rollback()
                myconn.close()
                messagebox.showinfo("Hospital Management System", "Details Successfully inserted")
                setting =1
                home.destroy()

            else:
                messagebox.showinfo("Hospital Management System", "Fill all the credentials")



        z+=90
        add_label = Label(home, text="Add Contents", bg="turquoise1", fg="white", font=('Times', 16,'bold'), padx=5,
                           width=18, relief='raised').place(x=30, y=z)

        z+=38
        id_Name = Label(home, text="Medicine Name", bg="turquoise1", fg="white", font=('Times', 14,'bold'), padx=5,
                        width=15).place(x=70, y=z)
        entry_Name = Entry(home,textvariable = p_name,width= 30,font=('Times', 14,'bold'),bg = "peachpuff").place(x=270,y=z)

        submit = Button(home, text='Submit', fg="black", font=('arial', 16, 'bold'), height=3, width=20, padx=5,
                        bg='turquoise1',
                        relief='raised', bd=10, command=done).place(x=700, y=z)

        z+=35

        id_qualification = Label(home, text="New stock", bg="turquoise1", fg="white", font=('Times', 14, 'bold'),
                                 padx=5,
                                 width=15).place(x=70, y=z)
        entry_qualify = Entry(home, textvariable=p_quantity, width=30, font=('Times', 14, 'bold'),bg = "peachpuff").place(x=270, y=z)

        z+=35

        id_specality = Label(home, text="Expiry date", bg="turquoise1", fg="white", font=('Times', 14, 'bold'),
                             padx=5, width=15).place(x=70, y=z)
        entry_specality = Entry(home, textvariable=p_exp, width=30, font=('Times', 14, 'bold'),bg = "peachpuff").place(x=270, y=z)

        z+=35

        id_specality = Label(home, text="Recent renewal date", bg="turquoise1", fg="white", font=('Times', 14, 'bold'),
                             padx=5, width=15).place(x=70, y=z)
        entry_specality = Entry(home, textvariable=p_recent, width=30, font=('Times', 14, 'bold'), bg="peachpuff").place(
            x=270, y=z)

        z += 35

    def update():

        global count
        global result
        global z
        id_no = IntVar()
        id_no.set("")

        def check():

            global z

            ids = id_no.get()
            pharma_name = StringVar()
            pharama_exp = StringVar()
            pharma_recent = StringVar()
            pharma_quantity = StringVar()

            flag = 0
            for i in range(0, count):
                if (ids == result[i][0]):
                    flag = 1

            if (flag == 1):
                def get_new():
                    p_name = pharma_name.get()
                    p_exp = pharama_exp.get()
                    p_recent = pharma_recent.get()
                    p_quantity = pharma_quantity.get()

                    if (p_name == "" and p_quantity == "" and p_exp == "" and p_recent == "" ):
                        messagebox.showinfo("Hospital Management System", "Enter Contents")

                    else:
                        myconn = mysql.connector.connect(host="localhost", user="root", password="Pratham",
                                                         database="hospital")

                        cur = myconn.cursor()

                        try:
                            cur.execute("select*from pharmacy")
                            result_w = cur.fetchall()
                            myconn.commit()

                        except:
                            myconn.rollback()

                        if (p_name != ""):
                            try:

                                sql = "update pharmacy set medicine_name = %s where pharmacy_id = %s"
                                val = [p_name,ids]

                                cur.execute(sql, val)

                                myconn.commit()
                            except:
                                myconn.rollback()

                        if (p_exp != ""):
                            try:

                                sql = "update pharmacy set expiry = %s where pharmacy_id = %s"
                                val = [p_recent, ids]

                                cur.execute(sql, val)

                                myconn.commit()
                            except:
                                myconn.rollback()
                            messagebox.showinfo("Hospital Management System", "Successfully Inserted Details")

                        if (p_quantity != ""):
                            try:

                                sql = "update pharmacy set quantity = %s where pharmacy_id = %s"
                                val = [p_quantity, ids]

                                cur.execute(sql, val)

                                myconn.commit()
                            except:
                                myconn.rollback()
                            messagebox.showinfo("Hospital Management System", "Successfully Inserted Details")

                        if (p_recent != ""):
                            try:

                                sql = "update pharmacy set r_date = %s where pharmacy_id = %s"
                                val = [p_recent, ids]

                                cur.execute(sql, val)

                                myconn.commit()
                            except:
                                myconn.rollback()
                            messagebox.showinfo("Hospital Management System", "Successfully Inserted Details")

                            setting = 1
                            home.destroy()
                            messagebox.showinfo("Hospital Management System", "Successfully Inserted Details")

                        myconn.close()

                id_Name = Label(home, text="Medicine Name", bg="turquoise1", fg="white", font=('Times', 14, 'bold'), padx=5,
                                width=15).place(x=700, y=z)
                entry_Name = Entry(home, textvariable=pharma_name, width=30, font=('Times', 14, 'bold'), bg="peachpuff").place(
                    x=970,
                    y=z)

                z += 35

                id_qualification = Label(home, text="Quantity", bg="turquoise1", fg="white",
                                         font=('Times', 14, 'bold'),
                                         padx=5,
                                         width=15).place(x=700, y=z)
                entry_qualify = Entry(home, textvariable=pharma_quantity, width=30, font=('Times', 14, 'bold'),
                                      bg="peachpuff").place(x=970,
                                                            y=z)

                z += 35

                id_specality = Label(home, text="Expiry Date", bg="turquoise1", fg="white", font=('Times', 14, 'bold'),
                                     padx=5, width=15).place(x=700, y=z)
                entry_specality = Entry(home, textvariable=pharama_exp, width=30, font=('Times', 14, 'bold'),
                                        bg="peachpuff").place(x=970, y=z)

                z += 35

                id_exp = Label(home, text="Recent Renewal Date", bg="turquoise1", fg="white", font=('Times', 14, 'bold'),
                               padx=5, width=15).place(x=700, y=z)
                entry_exp = Entry(home, textvariable=pharma_recent, width=30, font=('Times', 14, 'bold'),
                                  bg="peachpuff").place(
                    x=970, y=z)

                upd_btn = Button(home, text='SUBMIT', fg="black", font=('arial', 16, 'bold'), width=20, padx=5,
                                 bg='turquoise1',
                                 relief='raised', bd=10, command=get_new).place(x=130, y=z)

                z += 35

            else:
                messagebox.showinfo("Hospital Management System", "Invalid Credentials")

        z+=90
        add_label = Label(home, text="Updating Contents", bg="turquoise1", fg="white", font=('Times', 16,'bold'), padx=5,
                           width=18, relief='raised').place(x=30, y=z)

        z+=38
        id = Label(home, text="ID No.", bg="turquoise1", fg="white", font=('Times', 14,'bold'), padx=5,
                        width=15).place(x=70, y=z)
        entry = Entry(home,textvariable =id_no,width= 30,font=('Times', 14,'bold'),bg="peachpuff").place(x=270,y=z)



        z+=35

        enter = Button(home, text='Enter', fg="black", font=('arial', 14, 'bold'), width=10, padx=5, bg='turquoise1',
                        relief='raised', bd=10, command=check).place(x=200, y=z)


    def delete():
        global z
        p_id = IntVar()
        p_id.set("")

        def gayab():
            global count
            global result
            global setting

            no = p_id.get()
            no1 = int(no)


            flag =0
            for i in range(0,count):
                if(no1 ==  result[i][0]):
                    flag = 1

            if(flag):
                myconn = mysql.connector.connect(host="localhost", user="root", password="Pratham", database="hospital")


                try:
                    cur = myconn.cursor()
                    sql = "DELETE FROM pharmacy WHERE pharmacy_id = %s"

                    val = [no1]

                    cur.execute(sql,val)
                    myconn.commit()

                except:
                    print("Error")
                    myconn.rollback()

                myconn.close()

                messagebox.showinfo("Hospital Management System","Deleted Successfully")
                setting = 1
                home.destroy()
            else:
                messagebox.showinfo("Hospital Management System", "Wrong Credentials")
                p_id.set("")


        z += 90
        add_label = Label(home, text="Deleting Contents", bg="turquoise1", fg="white", font=('Times', 16, 'bold'),
                          padx=5,
                          width=18, relief='raised').place(x=30, y=z)

        z += 38
        id = Label(home, text="ID No.", bg="turquoise1", fg="white", font=('Times', 14, 'bold'), padx=5,
                   width=15).place(x=70, y=z)
        entry = Entry(home, textvariable=p_id, width=30, font=('Times', 14, 'bold'), bg="peachpuff").place(x=270, y=z)

        z+=35

        del_button = Button(home, text='Delete', fg="black", font=('arial', 14, 'bold'), width=10, padx=5, bg='turquoise1',
                       relief='raised', bd=10,command = gayab).place(x=200, y=z)


    z+=30

    add_btn = Button(home, text='ADD To Stock', fg="black", font=('arial', 16, 'bold'),width = 20, padx= 5, bg='turquoise1',
                          relief='raised', bd=10, command = add).place(x=150, y=z)
    del_btn = Button(home, text='Delete Medicine', fg="black", font=('arial', 16, 'bold'), width=20, padx=5, bg='turquoise1',
                     relief='raised', bd=10,command = delete).place(x=510, y=z)
    upd_btn = Button(home, text='Update Details', fg="black", font=('arial', 16, 'bold'), width=20, padx=5, bg='turquoise1',
                     relief='raised', bd=10, command = update).place(x=870, y=z)
    home.mainloop()

if(setting == 1):
    doctor()