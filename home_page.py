from tkinter import *
import bed
import addpatient
import ward
import patient
import doctor
import pharma


def inputs():

    home=Toplevel()
    home.geometry("1550x900")
    home.config(bg='snow2')

    def patient_details():
        patient.patient()


    def doc():
        doctor.details()

    def beds():
        bed.show1()

    def adding():
        addpatient.add_patient()

    def wards():
        ward.info()

    def gui():
        pharma.pharma()

    head_label = Label(home, text="HOSPITAL MANAGEMENT SYSTEM", background="turquoise1", foreground="white",
                       font=('Times', 50, 'bold'),width= 35).place(x=0, y=30)

    insert= Label(home,text = "Welcome to Admin Login", background="turquoise1",wraplength = 150,foreground="white",font=('Times', 22,'bold'),width= 17,height = 13, relief = "raised",bd=10).place(x=50, y=190)

    patient_info = Button(home, text='Patient Information', fg="black", font=('arial', 16, 'bold'), bg='turquoise1', relief='raised',
                       bd=10, height =7,width = 20, padx= 5,  command=patient_details).place(x=370, y=200)
    patient_info = Button(home, text='Pharmacy', fg="black", font=('arial', 16, 'bold'),height =7,width = 20, padx= 5, bg='turquoise1',
                          relief='raised', bd=10, command=gui).place(x=669, y=200)

    patient_info = Button(home, text='Ward', fg="black", font=('arial', 16, 'bold'), height =7,width = 20, padx= 5, bg='turquoise1',
                          relief='raised', bd=10, command=wards).place(x=970, y=200)



    patient_info = Button(home, text='Patient Beds', fg="black", font=('arial', 16, 'bold'),height =7,width = 20,
                              bg='turquoise1', relief='raised', bd=10, command=beds).place(x=370, y=410)

    patient_info = Button(home, text='Doctor details', fg="black", font=('arial', 16, 'bold'),height =7,width = 20, padx= 5, bg='turquoise1',
                          relief='raised', bd=10, command=doc).place(x=669, y=410)

    patient_info = Button(home, text='Add New Patient', fg="black", font=('arial', 16, 'bold'),height =7,width = 20, padx= 5, bg='turquoise1',
                          relief='raised', bd=10, command=adding).place(x=970, y=410)

    home.mainloop()

