from tkinter import *
from tkinter import messagebox
import GUI
import Instrument

def pharma():
    home = Tk()
    home.geometry("1550x900")
    home.config(bg='snow2')
    home.title("Pharmacy")

    def go_back():
        home.destroy()

    back = Button(home, text='Back', fg='black', font=('arial', 16, 'bold'), bg='turquoise1',
                  relief='raised', bd=10, command=go_back).place(x=1260, y=625)


    def add():
        GUI.doctor()

    def delete():
        Instrument.doctor()

    head_label = Label(home, text="PHARMACY", background="turquoise1", foreground="white",
                       font=('Times', 50, 'bold'), width=35).place(x=0, y=30)

    head_label = Label(home, text="Choose Below", foreground="turquoise1",
                       font=('Times', 20, 'bold'), width=35).place(x= 430, y=200)

    add_btn = Button(home, text='MEDICINE', fg="black", font=('arial', 16, 'bold'), width=20, padx=5,
                     bg='turquoise1',
                     relief='raised', bd=10, command=add).place(x=550, y=300)
    del_btn = Button(home, text='INSTRUMENTS', fg="black", font=('arial', 16, 'bold'), width=20, padx=5, bg='turquoise1',
                     relief='raised', bd=10, command=delete).place(x=550, y=400)

    home.mainloop()