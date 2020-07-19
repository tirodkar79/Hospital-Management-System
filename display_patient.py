from tkinter import *
from tkinter import messagebox
import mysql.connector


def jump(id):

    id1 =id
    print(id1)
    home1 = Toplevel()
    home1.geometry("1550x900")
    home1.config(bg='snow2')
    home1.title("Specifi Patient Details")

    photo = PhotoImage(file="E://icons/user.png")

    photo1 = photo.subsample(3, 3)

    admin = Label(home1, image=photo1).place(x=30, y=140)

    myconn = mysql.connector.connect(host="localhost", user="root", password="Pratham", database="hospital")

    cur = myconn.cursor()

    try:
        cur.execute("select patient.patient_id,patient.fname, patient.sname, patient.age, patient.gender, patient.married,patient.ad_date, patient.address, patient.disease,patient.phone, doctor.doctor_name,bed.cost,ward.ward_name, bed.bed_id from patient join ward on patient.ward_id = ward.ward_id join bed on patient.bed_id = bed.bed_id join doctor on patient.doctor_id = doctor.doctor_id")
        result = cur.fetchall()
        print(result)
        count = cur.rowcount



    except:
        print("Error")
        myconn.rollback()
    myconn.close()

    for i in range(0, count):
        if (result[i][0] == id1):
            print(id1)
            break

    fname = result[i][1]
    sname = result[i][2]
    age = result[i][3]
    gender = result[i][4]
    mstatus = result[i][5]
    date = result[i][6]
    address = result[i][7]
    disease_name = result[i][8]
    phone = result[i][9]
    doctor_name = result[i][10]
    cost = result[i][11]
    ward_name = result[i][12]
    bed = result[i][13]

    def go_back():
        home1.destroy()

    back = Button(home1, text='Back', fg='black', font=('arial', 16, 'bold'), bg='turquoise1',
                  relief='raised', bd=10, command=go_back).place(x=1260, y=625)

    head_label = Label(home1, text="PATIENT DETAILS", background="turquoise1", foreground="white",
                       font=('Times', 50, 'bold'), width=35).place(x=0, y=30)

    patient_id = Label(home1, text="Patient ID: ", foreground="deepskyblue", bg="snow2",
                       font=('Times', 24, 'bold')).place(x=290, y=140)
    patient_id = Label(home1, text=id1, foreground="deepskyblue", bg="snow2",
                       font=('Times', 24, 'bold')).place(x=530, y=140)

    patient_fname = Label(home1, text="First Name", foreground="deepskyblue", bg="snow2",
                          font=('Times', 20, 'bold')).place(x=290, y=200)
    entry_fname = Label(home1, text=fname, width=20, font=('Times', 20, 'bold'), bg="peachpuff").place(x=490,
                                                                                                               y=200)

    patient_sname = Label(home1, text="Surname", foreground="deepskyblue", bg="snow2",
                          font=('Times', 20, 'bold')).place(x=790, y=200)
    entry_sname = Label(home1, text=sname, width=20, font=('Times', 20, 'bold'), bg="peachpuff").place(x=990,
                                                                                                               y=200)

    patient_age = Label(home1, text="Age", foreground="deepskyblue", bg="snow2",
                        font=('Times', 20, 'bold')).place(x=290, y=260)
    entry_age = Label(home1, text=age, width=20, font=('Times', 20, 'bold'), bg="peachpuff").place(x=490,
                                                                                                           y=260)

    patient_gender = Label(home1, text="Gender", foreground="deepskyblue", bg="snow2",
                           font=('Times', 20, 'bold')).place(x=790, y=260)
    entry_age = Label(home1, text=gender, width=20, font=('Times', 20, 'bold'), bg="peachpuff").place(x=990,
                                                                                                   y=260)

    patient_mstatus = Label(home1, text="Martial Status", foreground="deepskyblue", bg="snow2",
                            font=('Times', 20, 'bold')).place(x=290, y=320)
    entry_mstatus = Label(home1, text=mstatus, width=20, font=('Times', 20, 'bold'), bg="peachpuff").place(
        x=490, y=320)

    patient_date = Label(home1, text="Date", foreground="deepskyblue", bg="snow2",
                         font=('Times', 20, 'bold')).place(x=790, y=320)
    entry_date = Label(home1, text=date, width=20, font=('Times', 20, 'bold'), bg="peachpuff").place(x=990,
                                                                                                             y=320)

    patient_add = Label(home1, text="Address", foreground="deepskyblue", bg="snow2",
                        font=('Times', 20, 'bold')).place(x=290, y=380)
    entry_add = Label(home1, text=address, width=56, font=('Times', 20, 'bold'), bg="peachpuff").place(
        x=490, y=380)

    patient_disease = Label(home1, text="Disease", foreground="deepskyblue", bg="snow2",
                            font=('Times', 20, 'bold')).place(x=290, y=460)
    entry_disease = Label(home1, text=disease_name, width=20, font=('Times', 20, 'bold'),
                          bg="peachpuff").place(x=490, y=460)

    patient_phone = Label(home1, text="Phone No.", foreground="deepskyblue", bg="snow2",
                          font=('Times', 20, 'bold')).place(x=790, y=460)
    entry_phone = Label(home1, text=phone, width=20, font=('Times', 20, 'bold'), bg="peachpuff").place(x=990,
                                                                                                               y=460)

    patient_doctor = Label(home1, text="Attended By", foreground="deepskyblue", bg="snow2",
                           font=('Times', 20, 'bold')).place(x=290, y=520)
    entry_doctor = Label(home1, text=doctor_name, width=20, font=('Times', 20, 'bold'),
                         bg="peachpuff").place(x=490, y=520)

    patient_doctor = Label(home1, text="Cost", foreground="deepskyblue", bg="snow2",
                           font=('Times', 20, 'bold')).place(x=790, y=520)
    entry_doctor = Label(home1, text=cost, width=20, font=('Times', 20, 'bold'),
                         bg="peachpuff").place(x=990, y=520)

    patient_ward = Label(home1, text="Ward Name", foreground="deepskyblue", bg="snow2",
                         font=('Times', 20, 'bold')).place(x=290, y=580)
    entry_ward = Label(home1, text=ward_name, width=20, font=('Times', 20, 'bold'), bg="peachpuff").place(
        x=490, y=580)

    patient_ward = Label(home1, text="Bed No.", foreground="deepskyblue", bg="snow2",
                         font=('Times', 20, 'bold')).place(x=790, y=580)
    entry_ward = Label(home1, text=bed, width=20, font=('Times', 20, 'bold'), bg="peachpuff").place(
        x=990, y=580)

    home1.mainloop()
