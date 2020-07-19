from tkinter import*
import mysql.connector

def info():
    home= Toplevel()
    home.title("WARD")
    home.geometry("1550x900")

    myconn = mysql.connector.connect(host="localhost", user="root", password="Pratham", database="hospital")

    cur = myconn.cursor()

    try:
        cur.execute("select ward.ward_id, ward.ward_name, doctor.doctor_name from ward join doctor on ward.doctor_id = doctor.doctor_id")
        result = cur.fetchall()
        count = cur.rowcount
        print(result)

    except:
        myconn.rollback()

    try:
        cur.execute("select bed.occupied_bed, bed.available_bed from ward join bed on ward.bed_id = bed.bed_id")
        result_b = cur.fetchall()

    except:
        myconn.rollback()
    myconn.close()

    def go_back():
        home.destroy()

    head_label = Label(home, text="WARD DETAILS", background="turquoise1", foreground="white",
                       font=('Times', 50, 'bold'), width=35).place(x=0, y=30)

    back = Button(home, text='Back', fg='black', font=('arial', 16, 'bold'), bg='turquoise1',
                  relief='raised', bd=10, command=go_back).place(x=1260, y=625)

    id_label = Label(home, text="Ward Id", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                     width=10).place(x=111, y=130)
    id_Name = Label(home, text="Ward Name", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                    width=17).place(x=243, y=130)
    id_quali = Label(home, text="Doctor", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid",
                     padx=5,
                     width=24).place(x=459, y=130)
    id_specality = Label(home, text="No. Of Occupied Beds", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid",
                         padx=5,
                         width=20).place(x=760, y=130)
    id_exp = Label(home, text="No. of Available Beds", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                   width=20).place(x=1010, y=130)

    global z
    z = 159
    global flag
    flag = 0
    for i in range(0, count):

        ward_id = result[i][0]
        ward_name = result[i][1]
        doctor_name = result[i][2]
        occu_bed = result_b[i][0]
        avail_bed = result_b[i][1]

        id_label = Label(home, text=ward_id, bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid",
                         padx=5,
                         width=10).place(x=111, y=z)
        id_Name = Label(home, text=ward_name, bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid",
                        padx=5,
                        width=17).place(x=243, y=z)
        id_quali = Label(home, text=doctor_name, bg="snow2", fg="black", font=('Times', 16, 'bold'),
                         relief="solid",
                         padx=5,
                         width=24).place(x=459, y=z)
        id_specality = Label(home, text=occu_bed, bg="snow2", fg="black", font=('Times', 16, 'bold'),
                             relief="solid",
                             padx=5,
                             width=20).place(x=760, y=z)
        id_exp = Label(home, text=avail_bed, bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid",
                       padx=5,
                       width=20).place(x=1010, y=z)
        z += 24


    home.mainloop()