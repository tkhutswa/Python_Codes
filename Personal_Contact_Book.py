#new contact, edit, or delete existing contacts and view the details of all their contacts.

import time
import sqlite3
from time import strftime

current_time = strftime('%H:%M:%S: %p')

def main_menu():
    global username
    print("Welcome to StoreBook", current_time, "-", "Please select an option")
    print(1, "Login")
    print(2, "Sign Up")
    option = int(input(""))
    match option:
        case 1:
            auth()
        case 2:
            user_reg()

def auth():
    global username
    try:
        username = str(input("Enter Username (name): \n"))
    except:
        print("Username in letters Only")

    password = str(input("Enter Password: \n"))

    print("connecting to sqlite database....")
    time.sleep(2)
    print("Resolving DNS to sqlite3_Users.db....")
    time.sleep(2)
    conn = sqlite3.connect('contact_book')
    print("Successfully connected to DB")
    c = conn.cursor()
    c.execute("SELECT * FROM contact_book")
    verify = c.fetchall()
    
    print("Reading from database....")
    time.sleep(2)
    # print(verify)
    for i in verify:
        if username in i and password in i:
            print("Initializing....")
            time.sleep(3)
            print("connecting to sqlite database....")
            time.sleep(2)
            print("Verifying details....")
            time.sleep(3)
            print("Successfully Logged In")
            time.sleep(2)
            user_menu()
        else:
            print("Invalid User or Password")

def user_menu():
    print("Welcome {}! - Please select an option".format(username))
    time.sleep(3)
    print(1, "View")
    print(2, "Edit")
    print(3, "Delete")
    print(4, "Sign Out")
    opt = int(input("\n"))

    match opt:
        case 1:
            view_db()
        case 2:
            edit_menu()
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass

def edit_menu():
    print("Please select a column you wnat to update: ")
    time.sleep(2)
    print(1, "Edit Name")
    print(2, "Edit Surname")
    print(3, "Edit Email")
    print(4, "Edit Number")
    print(5, "Edit Password")
    opt = int(input("\n"))

    match opt:
        case 1:
            edit_name()
        case 2:
            edit_surname()
        case 3:
            edit_email()
        case 4:
            edit_number()
        case 5:
            edit_password()

    

def view_db():
    conn = sqlite3.connect('contact_book')
    c = conn.cursor()
    c.execute("SELECT * FROM contact_book")
    view_all = c.fetchall()
    print(view_all)
    time.sleep(4)
    print(1, "Back")
    print(2, "Edit")
    print(3, "Delete")
    print(4, "Sign Out")
    opt = int(input("\n"))

    match opt:
        case 1:
            user_menu()
        case 2:
            edit_db()
        case 3:
            delete()
        case 4:
            main_menu()

def edit_db():
    print(1, "Edit Name")
    print(2, "Edit Surname")
    print(3, "Edit Email")
    print(4, "Edit Number")
    print(5, "Change Password")
    opt = int(input("\n"))

    match opt:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass

def edit_name():
    print("New Name: \n")
    time.sleep(2)
    rename = str(input("\n"))
    conn = sqlite3.connect('contact_book')
    c = conn.cursor()
    c.execute("SELECT * FROM 'contact_book'")
    c.execute("UPDATE contact_book SET name = '{}' ".format(rename))
    print("Successfully Updated")
    time.sleep(3)
    user_menu()

def edit_surname():
    print("New Surname: \n")
    time.sleep(2)
    rename = str(input("\n"))
    conn = sqlite3.connect('contact_book')
    c = conn.cursor()
    c.execute("SELECT * FROM 'contact_book'")
    c.execute("UPDATE contact_book SET surname = '{}' ".format(rename))
    print("Successfully Updated")
    time.sleep(3)
    user_menu()

def edit_email():
    print("New Email: \n")
    time.sleep(2)
    rename = str(input("\n"))
    conn = sqlite3.connect('contact_book')
    c = conn.cursor()
    c.execute("SELECT * FROM 'contact_book'")
    c.execute("UPDATE contact_book SET email = '{}' ".format(rename))
    print("Successfully Updated")
    time.sleep(3)
    user_menu()

def edit_number():
    print("New Number: \n")
    time.sleep(2)
    rename = int(input("\n"))
    conn = sqlite3.connect('contact_book')
    c = conn.cursor()
    c.execute("SELECT * FROM 'contact_book'")
    c.execute("UPDATE contact_book SET number = '{}' ".format(rename))
    print("Successfully updated")
    time.sleep(3)
    user_menu()

def edit_password():
    print("New Password: \n")
    time.sleep(2)
    pass_ = input("Enter New Password")
    c_pass = input("Confirm Password")
    conn = sqlite3.connect('contact_book')
    c = conn.cursor()
    c.execute("SELECT * FROM 'contact_book'")
    c.execute("UPDATE contact_book SET password = '{}' ".format(c_pass))
    print("Successfully Updated")
    time.sleep(3)
    user_menu()

def delete():
    pass

def user_reg():
    name = str(input("Enter Name: \n"))
    surname = str(input("Enter Surname: \n"))
    email = input("Enter Email address; \n")
    number = int(input("Enter Number: \n"))
    password = str(input("Enter Password: \n"))
    c_password = str(input("Confirm Password: \n"))

    # for i in range(0, 1):
    #     if password != confirm_password:
    #         print("Password do not match try again")
    #         break
    print("Connecting to db, Please be patient...")
    time.sleep(2)
    conn = sqlite3.connect('contact_book')
    print("Successfully Connected >>> contact_book Database")
    print("writing to main db...")
    time.sleep(3)
    c = conn.cursor()
    c.execute("INSERT INTO 'contact_book' ('name','surname','email','number','password') VALUES (?,?,?,?,?)", (name,surname,email,number,password))
    conn.commit()
    print("Successfully Registered")
    c.execute("SELECT * FROM contact_book")
    conn.close()
    main_menu()
    
main_menu()
