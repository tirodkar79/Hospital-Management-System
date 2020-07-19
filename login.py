from tkinter import *
from tkinter import messagebox
import home_page

def doing():

    home = Tk()
    home.title("Hospital Management System")
    home.geometry("1550x900")
    head_label = Label(home, text="Jeevan Vaatika Hospital", background="turquoise1", foreground="white",
                       font=('Times', 50, 'bold'), width=35).place(x=0, y=30)

    user = StringVar()
    password = StringVar()


    def check():
        username = user.get()
        passwords = password.get()


        if (username == "Hospital" and passwords == "12345"):
            user.set("")
            password.set("")
            home_page.inputs()

        else:
            messagebox.showinfo("Alert", "Invalid Credentials")
            user.set("")
            password.set("")

    user_label = Label(home, text="Username", background="snow2", foreground="black", font=('arial', 16, 'bold')).place(
        x=640, y=200)
    user_text = Entry(home, textvariable=user, bd=10, width=40, justify='right', bg='cyan').place(x=570, y=240)

    pass_label = Label(home, text="Password", background="snow2", foreground="black", font=('arial', 16, 'bold')).place(
        x=640, y=300)
    pass_text = Entry(home, textvariable=password, bd=10, width=40, justify='right', bg='cyan', show='*').place(x=570,
                                                                                                                y=340)

    login_btn = Button(home, text='Login', fg="black", font=('arial', 16, 'bold'), width=10, bg='Cyan', relief='raised',
                       bd=10, command=check).place(x=630, y=400)

    home.mainloop()

doing()