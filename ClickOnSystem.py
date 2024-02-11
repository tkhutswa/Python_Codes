#Incoperate the clickOn system security control
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

c_time = strftime('%H:%M:%S: %p')
# after(1000,c_time)
print(c_time)


load_dotenv('env')

user_name: str = os.getenv('USERNAME')
pass_name: str = os.getenv('PASSWORD')


now = datetime.now()

print("WELCOME TO THE CLICK-ON SYSTEM - {}".format(c_time))

logs = []
keys = []
token = False
secret_key = randint(10000, 99999)
house_key = secret_key
house_numbers = []
max_length = 5
for i in range(6600, 7000, 4):
    house_numbers.append(i)
def code_gen():
    for i in range(6000, 7000, 4):
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
    nr_days = int(input(""))
    print("Requesting Code.....Please be patient")
    time.sleep(4)
    # access_code = randint(20000, 99999)
    if nr_days == 1:
        time.sleep(2)
        print("Your Code has been generated: ", secret_key, "on {}".format(now), "This will be valid till 23:59 today")
        with open('logs.txt', 'a') as log:
            log.write("\n")
            log.write("App Generated - Unique Code {C} - Generated at: {time} ".format(C=secret_key, time=now))

    elif nr_days == 2:
        time.sleep(2)
        print("Your Access Code is: ", secret_key, "This will be valid till tomorrow 23:59")
        with open('logs.txt', 'a') as log:
            log.write("App Generated - Unique Code {C} - Generated at: {time} ".format(C=secret_key, time=now))
        #elif nr_days == 2:
            #print("Your Access Code is: ", access_code, "Valid till tomorrow 23:59")
    else:
        if nr_days == 3:
            print("Specify timeline in 'days' between 3 - 5 days")
            custom_days = int(input(""))
            formula = custom_days * 1
            print("Your Code has been generated: ", secret_key, "This will be valid till 23:59 on the {} day from today".format(formula))

def log_usr():
    try:
        value1 = str(input("Enter Username: \n"))
    except:
        print("Username in letters Only")

    value2 = str(input("Enter Password: \n"))
    
    if value1 in user_name and value2 in pass_name:
        print("Initializing....")
        time.sleep(3)
        print("Verifying details....")
        time.sleep(3)
        print("Successfully Logged In")
        time.sleep(2)
        num_days()
    else:
        print("Incorrect username or Password")

def verific():
    time.sleep(2)
    boom_pass = int(input("Enter Your Boom Pass: \n"))

    if boom_pass >= max_length or boom_pass < 5:
        print("Max 5 characters allowed, Please try again")
        boom_pass = int(input("Enter Your Boom Pass: \n"))


    if boom_pass == house_key:
            print("Please wait while we verify your Boom Pass......")
            time.sleep(5)
            print("Boom successfully Opened")
            token = True
            time.sleep(2)
            print("Token: ", token)
    else:
        print("Unable to Verify your boom pass!")
            #print("token:", token)
print(1, "Enter House Number")
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
        log_usr()
    case 3:
        print("Please contact us on 08600 3344 333 or email us at entry@devdigital.co.za")
#write a log file to capture entries
access_code = randint(20000, 99999)
# with open('logs.txt', 'a') as log:
#     log.write("Unique Code {C} - Generated at: {time} ".format(C=access_code, time=now))


def read_logs():
    with open('logs.txt', 'r') as log:
        print(log.read())





