from tkinter import *
import mysql.connector
from tkinter import messagebox


global flag
flag =0
def add_patient():
    home = Toplevel()
    home.geometry("1550x900")
    home.config(bg='snow2')
    home.title("Patient Details")

    def go_back():
        home.destroy()

    head_label = Label(home, text="ADD NEW PATIENTS", background="turquoise1", foreground="white",
                       font=('Times', 50, 'bold'), width=35).place(x=0, y=30)

    photo = PhotoImage(file = "E://icons/user.png")

    photo1 = photo.subsample(3,3)

    admin = Label(home,image=photo1).place(x=30,y=140)

    fname = StringVar()
    sname = StringVar()
    age = IntVar()
    gender = IntVar()
    mstatus = StringVar()
    date = StringVar()
    addresss = StringVar()
    phone = StringVar()
    disease_name = StringVar()
    doctor_name = StringVar()
    ward_name = StringVar()

    age.set("")
    def adding():

        global flag
        first = fname.get()
        second = sname.get()
        year = age.get()
        ling = gender.get()
        married = mstatus.get()
        admit_date = date.get()
        address = addresss.get()
        contact = phone.get()
        disease = disease_name.get()
        doctor = doctor_name.get()
        ward = ward_name.get()


        if(ling == 1):
            lings = "Male"

        else:
            lings = "Female"

        myconn = mysql.connector.connect(host="localhost", user="root", password="Pratham", database="hospital")

        cur = myconn.cursor()

        try:
            cur.execute("select doctor.doctor_id, doctor.doctor_name,ward.ward_id, ward.ward_name from doctor join ward on doctor.doctor_id = ward.doctor_id")
            result_d = cur.fetchall()
            count = cur.rowcount

            for i in range (0,count):
                if(result_d[i][1] == doctor):
                    doctor_id = result_d[i][0]
                    ward_id = result_d[i][2]
                    j=i

            myconn.commit()

        except:
            myconn.rollback()

        try:
            cur.execute("select ward.ward_id,bed.bed_id from ward join bed on ward.bed_id = bed.bed_id")
            result_b = cur.fetchall()
            bed_id = result_b[j][1]


            myconn.commit()

        except:
            myconn.rollback()


        try:

            cur.execute("select*from patient")
            result = cur.fetchall()
            count = cur.rowcount

            no = count + 1
            sql = "insert into patient(patient_id, fname, sname, age, gender, married, ad_date, address, phone,disease,doctor_id, ward_id, bed_id)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            val = (no, first, second, year, lings, married, admit_date, address, contact, disease, doctor_id,ward_id ,bed_id)

            cur.execute(sql, val)

            myconn.commit()


        except:
            myconn.rollback()

        try:
            sql = "select available_bed, occupied_bed from bed where bed_id = %s"
            val = [bed_id]
            cur.execute(sql,val)
            inc = cur.fetchall()

            avail = inc[0][0]
            avail -=1
            occupy = inc[0][1]
            occupy +=1

            myconn.commit()
        except:
            myconn.rollback()

        try:
            sql = "update bed set available_bed = %s, occupied_bed = %s where bed_id = %s"
            val = (avail,occupy,bed_id)
            cur.execute(sql,val)

            myconn.commit()

        except:
            myconn.rollback()


        myconn.close()
        messagebox.showinfo("Hospital Management System", "Details inserted successfully")
        flag = 1



    patient_id = Label(home, text="Patient Details", foreground="deepskyblue",bg= "snow2",
                       font=('Times', 24, 'bold')).place(x=290, y=140)

    patient_fname = Label(home, text="First Name", foreground="deepskyblue", bg="snow2",
                       font=('Times', 20, 'bold')).place(x=290, y=200)
    entry_fname = Entry(home, textvariable=fname, width=20, font=('Times', 20, 'bold'),bg = "peachpuff").place(x=490,y=200)


    patient_sname = Label(home, text="Surname", foreground="deepskyblue", bg="snow2",
                       font=('Times', 20, 'bold')).place(x=790, y=200)
    entry_sname = Entry(home, textvariable=sname, width=20, font=('Times', 20, 'bold'), bg="peachpuff").place(x=990,y=200)


    patient_age = Label(home, text="Age", foreground="deepskyblue", bg="snow2",
                       font=('Times', 20, 'bold')).place(x=290, y=260)
    entry_age = Entry(home, textvariable=age, width=20, font=('Times', 20, 'bold'), bg="peachpuff").place(x=490,y=260)

    patient_gender = Label(home, text="Gender", foreground="deepskyblue", bg="snow2",
                       font=('Times', 20, 'bold')).place(x=790, y=260)
    male = Radiobutton(home,text="Male", variable=gender,value = 1,font=('Times', 20, 'bold'),bg= "snow2",fg = "deepskyblue").place(x=990,y=260)
    female = Radiobutton(home, text="Female", variable=gender, value=2,font=('Times', 20, 'bold'),bg="snow2",fg = "deepskyblue").place(x=1150, y=260)

    patient_mstatus = Label(home, text="Martial Status", foreground="deepskyblue", bg="snow2",
                       font=('Times', 20, 'bold')).place(x=290, y=320)
    entry_mstatus = Entry(home, textvariable=mstatus, width=20, font=('Times', 20, 'bold'), bg="peachpuff").place(x=490, y=320)

    patient_date = Label(home, text="Date", foreground="deepskyblue", bg="snow2",
                       font=('Times', 20, 'bold')).place(x=790, y=320)
    entry_date = Entry(home, textvariable=date, width=20, font=('Times', 20, 'bold'), bg="peachpuff").place(x=990, y=320)

    patient_add = Label(home, text="Address", foreground="deepskyblue", bg="snow2",
                       font=('Times', 20, 'bold')).place(x=290, y=380)
    entry_add = Entry(home, textvariable=addresss, width=56, font=('Times', 20, 'bold'), bg="peachpuff").place(x=490, y=380)

    patient_disease = Label(home, text="Disease", foreground="deepskyblue", bg="snow2",
                       font=('Times', 20, 'bold')).place(x=290, y=460)
    entry_disease = Entry(home, textvariable=disease_name, width=20, font=('Times', 20, 'bold'), bg="peachpuff").place(x=490, y=460)

    patient_phone = Label(home, text="Phone No.", foreground="deepskyblue", bg="snow2",
                       font=('Times', 20, 'bold')).place(x=790, y=460)
    entry_phone = Entry(home, textvariable=phone, width=20, font=('Times', 20, 'bold'), bg="peachpuff").place(x=990, y=460)

    patient_doctor = Label(home, text="Attended By", foreground="deepskyblue", bg="snow2",
                       font=('Times', 20, 'bold')).place(x=290, y=520)
    entry_doctor = Entry(home, textvariable=doctor_name, width=56, font=('Times', 20, 'bold'), bg="peachpuff").place(x=490,
                                                                                                                 y=520)

    patient_ward = Label(home, text="Ward Name", foreground="deepskyblue", bg="snow2",
                       font=('Times', 20, 'bold')).place(x=290, y=580)
    entry_ward = Entry(home, textvariable=ward_name, width=20, font=('Times', 20, 'bold'), bg="peachpuff").place(x=490, y=580)

    add_btn = Button(home, text='Add Patient Information', fg="black", font=('arial', 16, 'bold'), width=75, padx=5,  bg='turquoise1',
                    relief='raised', bd=10, command = adding).place(x=290, y=640)

    home.mainloop()

if(flag == 1):
    add_patient()
add_patient()