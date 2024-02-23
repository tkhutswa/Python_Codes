import sqlite3
import time
total_balance = 0
global check_balance

temp = []

def check_balance():
    conn = sqlite3.connect('transactions')
    c = conn.cursor()
    c.execute("SELECT * FROM amount")
    balance = c.fetchall()
    for data in balance:
        temp.append(sum(data))
        total = sum(temp)
        print(total)
        time.sleep(3)
        main_menu()
    
    total = sum(temp)
    print("Your Balance is: R{}".format(total))
def main_menu():
    print("Welcome to Supabet - Please select an option")
    print(1, "Bet")
    print(2, "Deposit funds")
    print(3, "Check funds")
    opt = int(input("\n"))

    match opt:
        case 1:
            pass
        case 2:
            depo_funds()
        case 3:
            check_balance()

def depo_funds():
    global total
    global total_balance
    deposit = int(input("Enter Your Amount to Deposit: \n"))
    conn = sqlite3.connect('transactions')
    c = conn.cursor()
    c.execute("INSERT INTO amount VALUES(?)", [deposit])
    conn.commit()
    c.execute("SELECT * FROM amount")
    balance = c.fetchall()

    for data in balance:
        temp.append(sum(data))
    
    total = sum(temp)
    print("Your Balance is: R{}".format(total))
    time.sleep(2)
    main_menu()

main_menu()
