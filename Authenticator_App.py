import tkinter as tk
from tkinter import *
import random
from random import randint
import time
from tkinter import messagebox
from datetime import datetime
from datetime import date
import os
import socket



hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

time_stamp = datetime.now()

access_codes = randint(10000, 99999)            

root = Tk()
root.title('Logic Tech Hub')

root.iconbitmap('size.ico')

#bg = PhotoImage(file='dark.png')
#my_label=Label(root, image=bg)
#my_label.place(x=0, y=0, relwidth=1, relheight=1)


def pass_logger():
    with open('logs.txt', 'a') as log:
        log.write("\n")
        log.write("User: {u} with Password: {p} has generated an OTP: {o} at {t} source: {y}".format(u=name_entry.get(),p=pass_entry.get(),o=access_codes, t=time_stamp, y=ip_address))

def fail_logger():
    with open('logs.txt', 'a') as log:
        log.write("\n")
        log.write("IP: {i} User: {u} with Password: {p} has no account, attempt at: {t}".format(u=name_entry.get(),p=pass_entry.get(), t=time_stamp, i=ip_address))

def code_gen():
    #with open('user_doc.txt') as file, open('pass_doc.txt') as file1:
        #print(file1.read())
        if name_entry.get() == "Themba" and pass_entry.get() == "Password":
            time.sleep(3)
            messagebox.showinfo(title='Your Code', message='OTP: {}'.format(access_codes))
            pass_logger()
            otp_view=Label(root, text=code_gen)
            
            print(access_codes)
        
        else:
            messagebox.showinfo("Access Denied", "User Not Found!")
            fail_logger()

#create
name_user=Label(text="Username", font=("Arial", 15))
name_pass=Label(text="Password", font=("Arial", 15))

name_entry=Entry()
pass_entry=Entry(show="*")

main=Label(root, text="Login", font=("Arial", 19), fg="White")
click_gen=Button(text='Generate', command=code_gen, font=("Arial", 13), fg="Black")
sign_user=Button(text='Sign Up')
exit_button=Button(text="Exit", command=root.destroy, bg="Black", fg="Black")

otp_view=Label(root, text=code_gen)

#append to root
main.grid(row=0, column=4, pady=10)

name_user.grid(row=1, column=3,pady=5)
name_entry.grid(row=1, column=4, pady=5)

name_pass.grid(row=2, column=3, pady=5)
pass_entry.grid(row=2, column=4, pady=5)

click_gen.grid(row=4, column=4, pady=5)
exit_button.grid(row=5, column=4, pady=5)
sign_user.grid(row=6, column=4)

# otp_view.grid(row=8, column=2)

root.geometry('330x350')

#root.configure(bg="light grey")

root.mainloop()




