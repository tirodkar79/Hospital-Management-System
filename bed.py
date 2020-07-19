from tkinter import *
from tkinter import messagebox
import mysql.connector

global flag
flag = 0
def show1():
    home = Toplevel()
    home.title("Available Beds")
    home.geometry("1550x900")

    myconn = mysql.connector.connect(host="localhost", user="root", password="Pratham", database="hospital")

    cur = myconn.cursor()

    try:
        cur.execute("select*from bed")
        result = cur.fetchall()
        count = cur.rowcount


    except:
        myconn.rollback()
    myconn.close()

    def go_back():
        home.destroy()

    head_label = Label(home, text="BED DETAILS", background="turquoise1", foreground="white",
                       font=('Times', 50, 'bold'), width=35).place(x=0, y=30)

    back = Button(home, text='Back', fg='black', font=('arial', 16, 'bold'), bg='turquoise1',
                  relief='raised', bd=10, command=go_back).place(x=1260, y=625)

    id_label = Label(home, text="Bed No.", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid",
                     padx=5,
                     width=10).place(x=55, y=130)
    id_Name = Label(home, text="Bed Type", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid",
                    padx=5,
                    width=27).place(x=186, y=130)
    id_quali = Label(home, text="Cost", bg="snow2", fg="black", font=('Times', 16, 'bold'),
                     relief="solid",
                     padx=5,
                     width=15).place(x=524, y=130)
    id_specality = Label(home, text="Available Beds", bg="snow2", fg="black", font=('Times', 16, 'bold'),
                         relief="solid",
                         padx=5,
                         width=15).place(x=717, y=130)
    id_exp = Label(home, text="Occupied Beds", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid",
                   padx=5,
                   width=15).place(x=910, y=130)
    id_exp = Label(home, text="Total Beds", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid",
                   padx=5,
                   width=10).place(x=1100, y=130)
    global z
    z = 159
    global flag
    flag = 0

    for i in range(0, count):
        id = result[i][0]
        bed_type = result[i][1]
        cost = result[i][2]
        a_bed = result[i][3]
        o_bed = result[i][4]
        total = result[i][5]

        id_label = Label(home, text=id, bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid",
                         padx=5,
                         width=10).place(x=55, y=z)
        id_Name = Label(home, text=bed_type, bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid",
                        padx=5,
                        width=27).place(x=186, y=z)
        id_quali = Label(home, text=cost, bg="snow2", fg="black", font=('Times', 16, 'bold'),
                         relief="solid",
                         padx=5,
                         width=15).place(x=524, y=z)
        id_specality = Label(home, text=a_bed, bg="snow2", fg="black", font=('Times', 16, 'bold'),
                             relief="solid",
                             padx=5,
                             width=15).place(x=717, y=z)
        id_exp = Label(home, text=o_bed, bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid",
                       padx=5,
                       width=15).place(x=910, y=z)
        id_exp = Label(home, text=total, bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid",
                       padx=5,
                       width=10).place(x=1100, y=z)
        z += 24



    def add():
        global z
        b_type = StringVar()
        costs = IntVar()
        costs.set("")
        t_bed = IntVar()
        t_bed.set("")


        def done():
            global flag
            bed_type = b_type.get()
            cost = costs.get()
            total = t_bed.get()
            available = total
            occupied = 0

            global z
            if (bed_type != "" and cost != "" and total != ""):

                myconn = mysql.connector.connect(host="localhost", user="root", password="Pratham", database="hospital")

                cur = myconn.cursor()

                try:

                    cur.execute("select*from bed")
                    result = cur.fetchall()
                    count = cur.rowcount

                    no = count + 1

                    sql = "insert into bed(bed_id,bed_type,cost,available_bed,occupied_bed,total_bed)values(%s,%s,%s,%s,%s,%s)"

                    val = (no,bed_type,cost,available,occupied,total)
                    cur.execute(sql, val)

                    myconn.commit()

                except:
                    myconn.rollback()
                myconn.close()
                messagebox.showinfo("Hospital Management System", "Details Successfully inserted")
                flag = 1
                ava.destroy()

            else:
                messagebox.showinfo("Hospital Management System", "Fill all the credentials")


        z += 90
        add_label = Label(home, text="Add Contents", bg="turquoise1", fg="white", font=('Times', 16, 'bold'),
                          padx=5,
                          width=18, relief='raised').place(x=30, y=z)

        z += 38
        # id_Name = Label(home, text="Bed Id", bg="turquoise1", fg="white", font=('Times', 14, 'bold'), padx=5,
        #               width=15).place(x=70, y=z)
        # entry_Name = Entry(home, textvariable="", width=30, font=('Times', 14, 'bold'), bg="peachpuff").place(
        #   x=270,
        #  y=z)

        submit = Button(home, text='Submit', fg="black", font=('arial', 16, 'bold'), height=3, width=20, padx=5,
                        bg='turquoise1',
                        relief='raised', bd=10, command=done).place(x=700, y=z)

        z += 35

        id_specality = Label(home, text="Bed Type", bg="turquoise1", fg="white", font=('Times', 14, 'bold'),
                             padx=5, width=15).place(x=70, y=z)
        entry_specality = Entry(home, textvariable=b_type, width=30, font=('Times', 14, 'bold'),
                                bg="peachpuff").place(
            x=270, y=z)
        z += 35

        id_qualification = Label(home, text="Cost", bg="turquoise1", fg="white",
                                 font=('Times', 14, 'bold'),
                                 padx=5,
                                 width=15).place(x=70, y=z)
        entry_qualify = Entry(home, textvariable=costs, width=30, font=('Times', 14, 'bold'),
                              bg="peachpuff").place(x=270, y=z)

        z += 35

        id_specality = Label(home, text="Total Beds", bg="turquoise1", fg="white", font=('Times', 14, 'bold'),
                             padx=5, width=15).place(x=70, y=z)
        entry_specality = Entry(home, textvariable=t_bed, width=30, font=('Times', 14, 'bold'),
                                bg="peachpuff").place(x=270, y=z)

        z += 35

    z += 30

    add_btn = Button(home, text='ADD NEW DETAILS', fg="black", font=('arial', 16, 'bold'), width=20, padx=5,
                     bg='turquoise1',
                     relief='raised', bd=10, command=add).place(x=550, y=z)
    home.mainloop()

if(flag == 1):
    show1()
