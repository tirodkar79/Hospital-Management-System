from tkinter import *
from tkinter import messagebox
import mysql.connector

global setting
setting = 0
flag =0
def details():

    global count
    global result

    myconn = mysql.connector.connect(host="localhost", user="root", password="Pratham", database="hospital")

    cur = myconn.cursor()

    try:
        cur.execute("select doctor.doctor_id, doctor.doctor_name, doctor.qualification, doctor.specality, doctor.exp, ward.ward_name, doctor.contact from doctor join ward on doctor.doctor_id = ward.doctor_id")
        result = cur.fetchall()
        print(result)
        count = cur.rowcount


    except:
        print("Error")
        myconn.rollback()
    myconn.close()

    home = Toplevel()
    home.geometry("1550x900")
    home.config(bg='snow2')
    home.title("Doctor Details")

    global id
    global doctor_name
    global qualify
    global special
    global exp
    global phone

    def go_back():
        home.destroy()

    head_label = Label(home, text="DOCTOR DETAILS", background="turquoise1", foreground="white",
                       font=('Times', 50, 'bold'), width=35).place(x=0, y=30)

    back = Button(home, text='Back', fg='black', font=('arial', 16, 'bold'), bg='turquoise1',
                  relief='raised', bd=10, command=go_back).place(x=1260, y=625)

    id_label = Label(home,text="Doctor Id",bg="snow2",fg = "black",font=('Times', 16, 'bold'),relief = "solid",padx=5,width=10).place(x=6,y=130)

    id_Name = Label(home, text="Name", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                     width=27).place(x=139, y=130)
    id_quali = Label(home, text="Qualification", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                     width=10).place(x=476, y=130)
    id_specality = Label(home, text="Specality", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                     width=15).place(x=609, y=130)
    id_exp = Label(home, text="Experience", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                     width=10).place(x=802, y=130)
    id_contact = Label(home, text="Ward Head", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                     width=20).place(x=935, y=130)
    id_contact = Label(home, text="Contact Number", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid",
                       padx=5,
                       width=13).place(x=1184, y=130)
    global z
    z = 159
    for i in range(0,count):

        id = result[i][0]
        doctor_name = result[i][1]
        qualify = result[i][2]
        special = result[i][3]
        exp = result[i][4]
        ward_h = result[i][5]
        phone = result[i][6]



        id_label = Label(home, text=id, bg="snow2", fg="black", font=('Times', 14), relief="solid",
                         padx=5, width=12).place(x=6,y=z)

        id_Name = Label(home, text=doctor_name, bg="snow2", fg="black", font=('Times', 14), relief="solid", padx=5,
                        width=33).place(x=139, y=z)
        id_quali = Label(home, text=qualify, bg="snow2", fg="black", font=('Times', 14), relief="solid",
                         padx=5,
                         width=12).place(x=476, y=z)
        id_specality = Label(home, text=special, bg="snow2", fg="black", font=('Times', 14), relief="solid",
                             padx=5,
                             width=18).place(x=609, y=z)
        id_exp = Label(home, text=exp, bg="snow2", fg="black", font=('Times', 14), relief="solid",
                       padx=5,
                       width=12).place(x=802, y=z)
        id_contact = Label(home, text=ward_h, bg="snow2", fg="black", font=('Times', 14),
                           relief="solid", padx=5,
                           width=24).place(x=935, y=z)
        id_contact = Label(home, text=phone, bg="snow2", fg="black", font=('Times', 14),
                           relief="solid", padx=5,
                           width=15).place(x=1184, y=z)
        z+=24





    def add():
        global z

        name = StringVar()
        qualification = StringVar()
        speciality = StringVar()
        contact = StringVar()
        experience = StringVar()
        ward_head =StringVar()

        def done():

            global count
            global result
            doctor_id = count +1

            doctor_name = name.get()
            qualify = qualification.get()
            special = speciality.get()
            exp = experience.get()
            phone = contact.get()
            ward_h = ward_head.get()

            if (doctor_name != "" and qualify != "" and special != "" and exp != "" and phone != "" and ward_h !=""):

                myconn = mysql.connector.connect(host="localhost", user="root", password="Pratham", database="hospital")

                cur = myconn.cursor()

                sql = "insert into doctor(doctor_id, doctor_name,qualification,specality,exp,contact) values(%s,%s,%s,%s,%s,%s)"

                val = (doctor_id, doctor_name, qualify, special, exp, phone)

                try:
                    cur.execute(sql, val)

                    myconn.commit()


                except:

                    myconn.rollback()

                try:
                    sql = "insert into ward(ward_id, ward_name,doctor_id) values(%s,%s,%s)"
                    val = (doctor_id,ward_h,doctor_id)
                    cur.execute(sql,val)

                    myconn.commit()

                except:
                    print("Error 2")
                    myconn.rollback()
                myconn.close()
                messagebox.showinfo("Hospital Management System", "Details Successfully inserted")
                setting = 1
                home.destroy()

            else:
                messagebox.showinfo("Hospital Management System", "Fill all the credentials")

        z+=90
        add_label = Label(home, text="Add Contents", bg="turquoise1", fg="white", font=('Times', 16,'bold'), padx=5,
                           width=18, relief='raised').place(x=30, y=z)

        z+=38
        id_Name = Label(home, text="Name", bg="turquoise1", fg="white", font=('Times', 14,'bold'), padx=5,
                        width=15).place(x=70, y=z)
        entry_Name = Entry(home,textvariable = name,width= 30,font=('Times', 14,'bold'),bg = "peachpuff").place(x=270,y=z)

        submit = Button(home, text='Submit', fg="black", font=('arial', 16, 'bold'), height=3, width=20, padx=5,
                        bg='turquoise1',
                        relief='raised', bd=10, command=done).place(x=700, y=z)

        z+=35

        id_qualification = Label(home, text="Qualification", bg="turquoise1", fg="white", font=('Times', 14, 'bold'),
                                 padx=5,
                                 width=15).place(x=70, y=z)
        entry_qualify = Entry(home, textvariable=qualification, width=30, font=('Times', 14, 'bold'),bg = "peachpuff").place(x=270, y=z)

        z+=35

        id_specality = Label(home, text="Specality", bg="turquoise1", fg="white", font=('Times', 14, 'bold'),
                             padx=5, width=15).place(x=70, y=z)
        entry_specality = Entry(home, textvariable=speciality, width=30, font=('Times', 14, 'bold'),bg = "peachpuff").place(x=270, y=z)

        z+=35

        id_exp = Label(home, text="Experience", bg="turquoise1", fg="white", font=('Times', 14, 'bold'), padx=5,
                           width=15).place(x=70, y=z)
        entry_exp = Entry(home, textvariable=experience, width=30, font=('Times', 14, 'bold'), bg="peachpuff").place(
            x=270, y=z)

        z += 35
        id_contact = Label(home, text="Ward ", bg="turquoise1", fg="white", font=('Times', 14, 'bold'), padx=5,
                           width=15).place(x=70, y=z)
        entry_contact = Entry(home, textvariable=ward_head, width=30, font=('Times', 14, 'bold'), bg="peachpuff").place(
            x=270, y=z)

        z += 35
        id_contact = Label(home, text="Contact No.", bg="turquoise1", fg="white", font=('Times', 14,'bold'), padx=5,
                        width=15).place(x=70, y=z)
        entry_contact = Entry(home,textvariable = contact, width= 30,font=('Times', 14,'bold'),bg = "peachpuff").place(x=270,y=z)

        z+=35




    def update():

        global count
        global result
        global z
        global old
        id_no = IntVar()
        id_no.set("")

        def check():

            global z
            global old

            z = old

            id = id_no.get()
            name = StringVar()
            qualification = StringVar()
            speciality = StringVar()
            experience = StringVar()
            ward_head = StringVar()
            contact = StringVar()

            flag = 0
            for i in range(0, count):
                if (id == result[i][0]):
                    flag = 1

            if(flag == 1):
                def get_new():
                    doctor_name = name.get()
                    qualify = qualification.get()
                    special = speciality.get()
                    exp = experience.get()
                    ward_h= ward_head.get()
                    phone = contact.get()

                    if (doctor_name == "" and qualify == "" and special == "" and exp == "" and phone == "" and ward_h == ""):
                        messagebox.showinfo("Hospital Management System", "Enter Contents")

                    else:
                        myconn = mysql.connector.connect(host="localhost", user="root", password="Pratham",
                                                         database="hospital")

                        cur = myconn.cursor()

                        try:
                            cur.execute("select*from ward")
                            result_w = cur.fetchall()
                            myconn.commit()

                        except:
                            myconn.rollback()

                        for i in range(0, count):
                            if (result_w[i][2] == id):
                                ward_id = result_w[i][0]
                                print(ward_id)

                        if (doctor_name != ""):
                            try:

                                sql = "update doctor set doctor_name = %s where doctor_id = %s"
                                val = [doctor_name, id]

                                cur.execute(sql, val)

                                myconn.commit()
                            except:
                                myconn.rollback()

                        if (qualify != ""):
                            try:

                                sql = "update doctor set qualification = %s where doctor_id = %s"
                                val = [qualify, id]

                                cur.execute(sql, val)

                                myconn.commit()
                            except:
                                myconn.rollback()
                            messagebox.showinfo("Hospital Management System", "Successfully Inserted Details")

                        if (special != ""):
                            try:

                                sql = "update doctor set specality = %s where doctor_id = %s"
                                val = [special, id]

                                cur.execute(sql, val)

                                myconn.commit()
                            except:
                                myconn.rollback()
                            messagebox.showinfo("Hospital Management System", "Successfully Inserted Details")

                        if (exp != ""):
                            try:

                                sql = "update doctor set exp = %s where doctor_id = %s"
                                val = [exp, id]

                                cur.execute(sql, val)

                                myconn.commit()
                            except:
                                myconn.rollback()
                            messagebox.showinfo("Hospital Management System", "Successfully Inserted Details")

                        if (ward_h != ""):
                            try:

                                sql = "update ward set ward_name = %s where ward_id = %s"
                                val = [ward_h, ward_id]

                                cur.execute(sql, val)

                                myconn.commit()
                            except:
                                myconn.rollback()
                            messagebox.showinfo("Hospital Management System", "Successfully Inserted Details")

                        if (phone != ""):
                            try:

                                sql = "update doctor set contact = %s where doctor_id = %s"
                                val = [phone, id]

                                cur.execute(sql, val)

                                myconn.commit()
                            except:
                                myconn.rollback()
                            setting = 1
                            home.destroy()
                            messagebox.showinfo("Hospital Management System", "Successfully Inserted Details")

                        myconn.close()

                id_Name = Label(home, text="Name", bg="turquoise1", fg="white", font=('Times', 14, 'bold'), padx=5,
                                width=15).place(x=700, y=z)
                entry_Name = Entry(home, textvariable=name, width=30, font=('Times', 14, 'bold'), bg="peachpuff").place(
                    x=970,
                    y=z)

                z  += 35

                id_qualification = Label(home, text="Qualification", bg="turquoise1", fg="white",
                                         font=('Times', 14, 'bold'),
                                         padx=5,
                                         width=15).place(x=700, y=z)
                entry_qualify = Entry(home, textvariable=qualification, width=30, font=('Times', 14, 'bold'),
                                      bg="peachpuff").place(x=970,
                                                            y=z)

                z += 35

                id_specality = Label(home, text="Specality", bg="turquoise1", fg="white", font=('Times', 14, 'bold'),
                                     padx=5, width=15).place(x=700, y=z)
                entry_specality = Entry(home, textvariable=speciality, width=30, font=('Times', 14, 'bold'),
                                        bg="peachpuff").place(x=970, y=z)

                z += 35

                id_exp = Label(home, text="Experience", bg="turquoise1", fg="white", font=('Times', 14, 'bold'),
                               padx=5, width=15).place(x=700, y=z)
                entry_exp = Entry(home, textvariable=experience, width=30, font=('Times', 14, 'bold'),
                                  bg="peachpuff").place(
                    x=970, y=z)

                upd_btn = Button(home, text='SUBMIT', fg="black", font=('arial', 16, 'bold'), width=20, padx=5,
                                 bg='turquoise1',
                                 relief='raised', bd=10, command=get_new).place(x=130, y=z)

                z += 35

                id_contact = Label(home, text="Ward", bg="turquoise1", fg="white", font=('Times', 14, 'bold'),
                                   padx=5,
                                   width=15).place(x=700, y=z)
                entry_contact = Entry(home, textvariable=ward_head, width=30, font=('Times', 14, 'bold'),
                                      bg="peachpuff").place(x=970, y=z)

                z+=35

                id_contact = Label(home, text="Contact No.", bg="turquoise1", fg="white", font=('Times', 14, 'bold'),
                                   padx=5,
                                   width=15).place(x=700, y=z)
                entry_contact = Entry(home, textvariable=contact, width=30, font=('Times', 14, 'bold'),
                                      bg="peachpuff").place(x=970, y=z)


            else:
                messagebox.showinfo("Hospital Management System", "Invalid Credentials")


        z+=90
        add_label = Label(home, text="Updating Contents", bg="turquoise1", fg="white", font=('Times', 16,'bold'), padx=5,
                           width=18, relief='raised').place(x=30, y=z)

        z+=38
        id = Label(home, text="ID No.", bg="turquoise1", fg="white", font=('Times', 14,'bold'), padx=5,
                        width=15).place(x=70, y=z)
        entry = Entry(home,textvariable = id_no,width= 30,font=('Times', 14,'bold'),bg="peachpuff").place(x=270,y=z)

        old = z

        z+=35

        enter = Button(home, text='Enter', fg="black", font=('arial', 14, 'bold'), width=10, padx=5, bg='turquoise1',
                        relief='raised', bd=10, command=check).place(x=200, y=z)


    def delete():
        global z
        id_no = StringVar()

        def gayab():

            no = id_no.get()
            no1 = int(no)

            print(no1)

            myconn = mysql.connector.connect(host="localhost", user="root", password="Pratham", database="hospital")

            cur = myconn.cursor()

            try:
                cur.execute("select*from doctor")
                result = cur.fetchall()
                count = cur.rowcount


            except:
                myconn.rollback()

            myconn.close()

            flag =0
            for i in range(0,count):
                if(no1 ==  result[i][0]):
                    flag = 1

            if(flag):
                myconn = mysql.connector.connect(host="localhost", user="root", password="Pratham", database="hospital")


                try:
                    cur = myconn.cursor()
                    sql = "DELETE FROM doctor WHERE doctor_id = %s"

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
                id_no.set("")



        z += 90
        add_label = Label(home, text="Deleting Contents", bg="turquoise1", fg="white", font=('Times', 16, 'bold'),
                          padx=5,
                          width=18, relief='raised').place(x=30, y=z)

        z += 38
        id = Label(home, text="ID No.", bg="turquoise1", fg="white", font=('Times', 14, 'bold'), padx=5,
                   width=15).place(x=70, y=z)
        entry = Entry(home, textvariable=id_no, width=30, font=('Times', 14, 'bold'), bg="peachpuff").place(x=270, y=z)

        z+=35

        del_button = Button(home, text='Delete', fg="black", font=('arial', 14, 'bold'), width=10, padx=5, bg='turquoise1',
                       relief='raised', bd=10, command = gayab).place(x=200, y=z)


    z+=30

    add_btn = Button(home, text='ADD NEW DOCTOR', fg="black", font=('arial', 16, 'bold'),width = 20, padx= 5, bg='turquoise1',
                          relief='raised', bd=10, command = add).place(x=200, y=z)
    del_btn = Button(home, text='DELETE', fg="black", font=('arial', 16, 'bold'), width=20, padx=5, bg='turquoise1',
                     relief='raised', bd=10,command = delete).place(x=550, y=z)
    upd_btn = Button(home, text='UPDATE DETAILS', fg="black", font=('arial', 16, 'bold'), width=20, padx=5, bg='turquoise1',
                     relief='raised', bd=10, command = update).place(x=900, y=z)



    home.mainloop()
if(setting == 1):
    details()
