from tkinter import *
from tkinter import messagebox
import mysql.connector
import display_patient

def patient():
    home = Tk()
    home.geometry("1550x900")
    home.config(bg='snow2')
    home.title("Patient Details")

    def go_back():
        home.destroy()

    myconn = mysql.connector.connect(host="localhost", user="root", password="Pratham", database="hospital")

    cur = myconn.cursor()

    try:
        cur.execute("select patient.patient_id, patient.fname, patient.sname, ward.ward_id, bed.bed_id, patient.ad_date,patient.disease, bed.cost, patient.phone from patient join ward on patient.ward_id = ward.ward_id join bed on patient.bed_id = bed.bed_id")
        result = cur.fetchall()
        print(result)
        count = cur.rowcount


    except:
        print("Error")
        myconn.rollback()
    myconn.close()

    head_label = Label(home, text="PATIENT DETAILS", background="turquoise1", foreground="white",
                       font=('Times', 50, 'bold'), width=35).place(x=0, y=30)

    back = Button(home, text='Back', fg='black', font=('arial', 16, 'bold'), bg='turquoise1',
                  relief='raised', bd=10, command=go_back).place(x=1260, y=625)

    id_label = Label(home,text="Patient Id",bg="snow2",fg = "black",font=('Times', 16, 'bold'),relief = "solid",padx=5,width=10).place(x=10,y=130)

    id_Name = Label(home, text="Name", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                     width=27).place(x=143, y=130)
    id_ward = Label(home, text="Ward No.", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                     width=10).place(x=480, y=130)
    id_bed = Label(home, text="Bed No.", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                     width=10).place(x=613, y=130)
    id_admit = Label(home, text="Admited Date", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                     width=10).place(x=746, y=130)
    id_dis = Label(home, text="Disease", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                     width=12).place(x=879, y=130)
    id_bill = Label(home, text="Bill", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                     width=10).place(x=1036, y=130)
    id_cattend = Label(home, text="Contact No.", bg="snow2", fg="black", font=('Times', 16, 'bold'), relief="solid", padx=5,
                       width=14).place(x=1169, y=130)

    global z

    id_no = IntVar()
    id_no.set("")


    z= 159
    for i in range(0,count):

        p_id = result[i][0]
        p_name = result[i][1] + " " + result[i][2]
        p_ward = result[i][3]
        p_bed = result[i][4]
        p_admit = result[i][5]
        p_dis = result[i][6]
        p_bill = "Rs. " + str(result[i][7])
        p_contact = result[i][8]


        id_label = Label(home, text=p_id, bg="snow2", fg="black", font=('Times', 14), relief="solid",
                         padx=5, width=12).place(x=10, y=z)

        id_Name = Label(home, text=p_name, bg="snow2", fg="black", font=('Times', 14), relief="solid", padx=5,
                        width=33).place(x=143, y=z)
        id_ward = Label(home, text=p_ward, bg="snow2", fg="black", font=('Times', 14), relief="solid",
                        padx=5,
                        width=12).place(x=480, y=z)
        id_bed = Label(home, text=p_bed, bg="snow2", fg="black", font=('Times', 14), relief="solid", padx=5,
                       width=12).place(x=613, y=z)
        id_admit = Label(home, text=p_admit, bg="snow2", fg="black", font=('Times', 14), relief="solid",
                         padx=5,
                         width=12).place(x=746, y=z)
        id_dis = Label(home, text=p_dis, bg="snow2", fg="black", font=('Times', 14), relief="solid",
                       padx=5,
                       width=17).place(x=879, y=z)
        id_bill = Label(home, text=p_bill, bg="snow2", fg="black", font=('Times', 14), relief="solid", padx=5,
                        width=12).place(x=1036, y=z)
        id_cattend = Label(home, text=p_contact, bg="snow2", fg="black", font=('Times', 14), relief="solid",
                           padx=5,
                           width=17).place(x=1169, y=z)

        z+=24

    def jumping():
        id = id_no.get()
        display_patient.jump(id)

    z+=35



    search = Button(home, text='Search Specific Record', fg="black", font=('arial', 16, 'bold'), width=60,
                    padx=5,
                    bg='turquoise1',
                    relief='raised', bd=10, command=jumping).place(x=300, y=z)
    z+=85
    entry = Entry(home, textvariable=id_no, width=30, font=('Times', 18, 'bold'), bg="peachpuff").place(x=530, y=z)

    home.mainloop()
patient()