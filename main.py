from tkinter import *
from tkinter import messagebox
import home_page
from PIL import Image, ImageTk


main=Tk()
main.title("Hospital Management System")
main.geometry("1550x900")


photo = PhotoImage(file="ADMINLOGIN.png")
label = Label(main, image=photo)
label.place(x=0,y=0, relwidth=1, relheight=1,)

user= StringVar()
password= StringVar()
setting = 0
def check():
    username= user.get()
    passwords= password.get()
    global setting

    if(username == "Hospital" and passwords == "12345"):
        main.destroy()
        setting = 1
        user.set("")
        password.set("")

    else:
        messagebox.showinfo("Alert","Invalid Credentials")
        user.set("")
        password.set("")

user_label = Label(main,text="Username",background="snow2",font=('arial',16,'bold'), fg='cyan').place(x=640,y=200)
user_text =  Entry(main,textvariable = user, bd= 10, width= 40, justify= 'right', bg='cyan',font=('Times', 14)).place(x=520,y=240)

pass_label = Label(main,text="Password",background="snow2",font=('arial',16,'bold'), fg='cyan').place(x=640,y=300)
pass_text =  Entry(main,textvariable = password, bd= 10, width= 40, justify= 'right', bg='cyan', show='*',font=(14)).place(x=520,y=340)

login_btn = Button(main, text= 'Login', bg="white",font=('arial',16,'bold'),width=10, fg='cyan',relief='raised', bd=10, command= check).place(x=630,y=400)

main.mainloop()
#print(setting)
if(setting == 1):
    home_page.input()