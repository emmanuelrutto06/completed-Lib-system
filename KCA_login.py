from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
# from . LMS import*
def main():
    root = Tk()
    app = KCALogin(root)

class KCALogin:
    def __init__(self, master):
        self.master = master
        self.master.title("KCA Library Management Login System")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg='Cadet blue')
        self.frame = Frame(self.master, bg='cyan')
        self.frame.pack()
        
        self.username = StringVar()
        self.password = StringVar()
        
        self.lblTitle = Label(self.frame, text = "KCA Library Management System", font=('arial', 60, 'bold'), bg="cyan", fg="Cornsilk")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=20)
        #===============================================================================================================================
        self.LoginFrame1 = LabelFrame(self.frame, width=1300, height=300, font=('arial', 20,'bold'),relief=RIDGE,bg='cadet blue', text="Login", bd=40)
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=1000, height=200,font=('aral', 20,'bold'),relief=RIDGE, bg='cadet blue', text="Log",bd=40)
        self.LoginFrame2.grid(row=2, column=0)

        #===============================================================================================================================
        self.lblusername = Label(self.LoginFrame1, text = "Username", font=('arial', 30, 'bold'),bd=22,bg='cadet blue',fg='Cornsilk')
        self.lblusername.grid(row=0, column=0)

        self.txtusername = Entry(self.LoginFrame1,font=('arial',30, 'bold'), bd=7, textvariable=self.username, width=33)
        self.txtusername.grid(row=0, column=1,padx=88)

        self.lblpassword = Label(self.LoginFrame1, text = "Password", font=('arial', 30, 'bold'),bd=22,bg='cadet blue',fg='Cornsilk')
        self.lblpassword.grid(row=1, column=0)

        self.txtpassword = Entry(self.LoginFrame1,font=('arial',30, 'bold'), show='*', bd=7, textvariable=self.password, width=33)
        self.txtpassword.grid(row=1, column=1,padx=30)


        #===============================================================================================================================
        self.btnLogin = Button(self.LoginFrame2,text="Login", width=15,font=('arial',30, 'bold'),bg='cadet blue',fg='Cornsilk', command=self.Login_system)
        self.btnLogin.grid(row=3,column=0,pady=20,padx=8)

        self.btnReset = Button(self.LoginFrame2,text="Reset", width=15,font=('arial',30, 'bold'),bg='cadet blue',fg='Cornsilk', command=self.IReset)
        self.btnReset.grid(row=3,column=1,pady=20,padx=8)

        self.btnExit = Button(self.LoginFrame2,text="Exit", width=15,font=('arial',30, 'bold'),bg='cadet blue',fg='Cornsilk', command=self.iExit)
        self.btnExit.grid(row=3,column=2,pady=20,padx=8)

        #===============================================================================================================================
    
    def Login_system(self):
        user = (self.username.get())
        pas = (self.password.get())
        if(user == str(963852) and pas ==str(123456)):
            self.Login_Window()
        else:
            tkinter.messagebox.askyesno("KCA Library Management Login Sytem", "invalid Login Details")
            self.username.set("")
            self.password.set("")

    def IReset(self):
        self.username.set("")
        self.password.set("")
    
    def iExit(self):
            self.iExit = tkinter.messagebox.askyesno("KCA Login Systems", "Confirm if you want to exit")
            if self.iExit > 0:
                self.master.destroy()
                return
            
    def Login_Window(self):
        self.LoginWindow = Toplevel(self.master)
        self.app = KCAManagement(self.LoginWindow)



class KCAManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("KCA Library Management Login System")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg='cyan')
        self.frame = Frame(self.master, bg='cyan')
        self.frame.pack()


if __name__=='__main__':
    root = Tk()
    app = KCALogin(root)
    root.mainloop()