#Access_control_v2

#Access Control System - Developed by T@.com
import random
import tkinter as Tk
import time
from random import randint
import csv
from threading import Timer
import time
from datetime import datetime
from datetime import date
import dotenv
from dotenv import load_dotenv
import os
from tkinter import messagebox
from time import strftime
import pytz
import sqlite3

c_time = strftime('%H:%M:%S: %p')
# after(1000,c_time)
print(c_time)

c_time = datetime.now(pytz.timezone('Africa/Johannesburg'))

load_dotenv('env')

user_name: str = os.getenv('USERNAME')
pass_name: str = os.getenv('PASSWORD')

now = datetime.now()

print("Access Control System - {}".format(c_time))

logs = []
keys = []
token = False
secret_key = randint(10000, 99999)
house_key = secret_key
house_numbers = []
max_length = 5
for i in range(6600, 7000, 1):
    house_numbers.append(i)

def main_menu():           #print("token:", token)
    global house_num
    print(1, "Enter House Number - 6600 - 6999")
    print(2, "Generate Code")
    print(3, "Help")
    option = int(input("\n"))
    match option:
        case 1:
            print("Enter House Number")
            house_num = int(input(" \n"))
            print("Loading....")
            time.sleep(3)
            code_gen()
        case 2:
            num_days()
        case 3:
            print("Please contact us on 08600 3344 333 or email us at entry@devdigital.co.za")

def sign_up():
    global pass_c
    global surname
    global emailaddr
    global pass_w
    global pass_c
    try:
        usrname = str(input("Please Enter Your Name: \n"))
        surname = str(input("Enter Your Surname: \n"))
    except:
        print("Only letters allowed")

    emailaddr = str(input("email: \n"))
    pass_w = str(input("Password: \n"))
    pass_c = str(input("Confirm Password: \n"))
    if pass_w != pass_c:
        messagebox.showerror(title="Match Error", message="Password Does not Match")

    else:

        conn = sqlite3.connect('users')
        x = conn.cursor()
        print("wait while we commiting to the database...")
        time.sleep(2)
        x.execute("INSERT INTO users ('username','password') VALUES (?,?)", (usrname,pass_c))
        conn.commit()
        print("commit successful!")
        x.execute("SELECT * FROM users")        
        time.sleep(1)

        x.close()
        conn.close()
            
def usr_write():
    conek = sqlite3.connect('sql_logs')
    c = conek.cursor()

    c.execute("""CREATE TABLE main (
                name text,
                surname text,
                email text,
                password text,
                confirm_password text
              )""")
    print("Creating database, Please be patient...")
    time.sleep(3)
    print("Database created successfully")
    time.sleep(2)
    conek.commit()

    c.execute("INSERT INTO main ('','','','',) VALUES(?,?,?,?,?)", (user_name,surname,emailaddr,pass_w, pass_c))
    print("Successfully parsed onto main sqlite3 database")
    conek.commit()

    c.execute("SELECT * FROM main")
    print(c.fetchall())
    conek.close()


    with open('usrnames.txt', 'a') as db1:
        db1.write("\n")
        db1.write(creds)
        db1.write(pass_c)
        db1.write("\n")
        menu()

def code_gen():
    
    for i in range(6000, 7000, 1):
        if house_num in house_numbers:
            print("Your Boom pass been generated: ", house_key)
            with open('logs.txt', 'a') as log:
                log.write("\nUnique Code: ")
                log.write(str(house_key))
            verific()
            #access_code = randint(20000, 99999)
            # print(access_code)
            break
        else:
            print("House Not Found!")
            break

def log_read():
    with open('logs.txt', 'r') as logs:
        print(logs.read())


def user_menu():
    print(1, "Request Code")
    print(2, "Access History")
    select = int(input(""))
    match select:
        case 1:
            print("Valid for how many days?")
            time.sleep(2)
            num_days()
def num_days():
    time.sleep(1)
    print("Valid for how many days? ")
    print(1, "Today")
    print(2, "Tomorrow")
    print(3, "Custom")
    print(4, "History")
    nr_days = int(input(""))
    #print("Requesting Code.....Please be patient")
    time.sleep(4)
    # access_code = randint(20000, 99999)
    if nr_days == 1:
        print("Generating code....")
        time.sleep(2)
        print("Your Code has been generated: ", secret_key, "on {}".format(now), "This will be valid till 23:59 today")
        with open('logs_clicksys.txt', 'a') as log:
            log.write("\n")
            log.write("App Generated - Unique Code {C} - Generated at: {time} ".format(C=secret_key, time=now))

    elif nr_days == 2:
        print("Generating code....")
        time.sleep(2)
        print("Your Access Code is: ", secret_key, "This will be valid till tomorrow 23:59")
        with open('logs.txt', 'a') as log:
            for i in log:
                log.write("App Generated - Unique Code {C} - Generated at: {time} ".format(C=secret_key, time=now))
                break
            
        #elif nr_days == 2:
            #print("Your Access Code is: ", access_code, "Valid till tomorrow 23:59")
    elif nr_days == 4:
        print("fetching data....")
        time.sleep(2)
        log_read()
    else:
        if nr_days == 3:
            print("Specify timeline in 'days' between 3 - 5 days")
            custom_days = int(input(""))
            formula = custom_days * 1
            print("Your Code has been generated: ", secret_key, "This will be valid till 23:59 on the {} day from today".format(formula))

def menu():

    print(1, "Login")
    print(2, "Sign Up")
    print(3, "Help")
    opt = int(input("\n"))

    match opt:
        case 1:
            auth()
        case 2:
            print("Redirecting to sign page")
            time.sleep(2)
            sign_up()
        case 3:
            print("Please contact us on 08600 3344 333 or email us at entry@devdigital.co.za")


def auth():

    try:
        value1 = str(input("Enter Username: \n"))
    except:
        print("Username in letters Only")

    value2 = str(input("Enter Password: \n"))

    print("connecting to sqlite database....")
    time.sleep(2)
    print("Resolving DNS to sqlite3_Users.db....")
    time.sleep(2)
    conn = sqlite3.connect('users')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    verify = c.fetchall()
    #print(verify)
    for i in verify:
        #print(i)
        if value1 in i and value2 in i:
            print("Initializing....")
            time.sleep(3)
            print("connecting to sqlite database....")
            time.sleep(2)
            print("Verifying details....")
            time.sleep(3)
            print("Successfully Logged In")
            time.sleep(2)
            main_menu()
            break
        else:
            print("Invalid User or Password")
            break
    
    # if value1 == user_name and value2 == pass_name:
    #     print("Initializing....")
    #     time.sleep(3)
    #     print("Verifying details....")
    #     time.sleep(3)
    #     print("Successfully Logged In")
    #     time.sleep(2)
    #     main_menu()
    # else:
    #     print("Incorrect username or Password")

def verific():
    time.sleep(2)
    boom_pass = int(input("Enter Your Boom Pass: \n"))

    if boom_pass > max_length and boom_pass < 5:
        print("Max 5 characters allowed, Please try again")
        boom_pass = int(input("Enter Your Boom Pass:1 \n"))

    else:
        if boom_pass == house_key:
                print("Please wait while we verify your Boom Pass......")
                time.sleep(5)
                print("Boom successfully Opened")
                token = True
                time.sleep(2)
                print("Token: ", token)
        else:
            print("Unable to Verify your boom pass!")

#write a log file to capture entries
access_code = randint(20000, 99999)
# with open('logs.txt', 'a') as log:
#     log.write("Unique Code {C} - Generated at: {time} ".format(C=access_code, time=now))
def read_logs():
    with open('logs.txt', 'r') as log:
        print(log.read())

menu()
