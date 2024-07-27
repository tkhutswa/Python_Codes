import sqlite3
import time

total_balance = 0
global check_balance

temp = []

# conn = sqlite3.connect('transactions.db')
# c = conn.cursor()
# c.execute("select * from funds")
# data = c.fetchall()

# print(data)
# c.execute("Insert into funds('amount') values('10')")
# # c.execute("""create table funds(
# #     amount integer
# #     )""")
# conn.commit()

def check_balance():
    balance_ = 0
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute("SELECT * FROM funds")
    balance = c.fetchall()
    for data in balance:
        temp.append(sum(data))
        total = sum(temp)
    print("Your Balance is: R{}".format(total))
    temp.clear()
    time.sleep(3)
    main_menu()

    #     temp.append(sum(data)) 
        
    #     total = sum(temp)
    #     print(total)
    #     time.sleep(3)
    #     main_menu()
    
    # total = sum(temp)
    #print("Your Balance is: R{}".format(total))
    
    
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
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute("INSERT INTO funds(amount) VALUES(?)", [deposit])
    conn.commit()
    c.execute("SELECT * FROM funds")
    balance = c.fetchall()

    for data in balance:
        temp.append(sum(data))
    
    total = sum(temp)
    print("Your Balance is: R{}".format(total))
    temp.clear()
    time.sleep(2)
    main_menu()

main_menu()

#still in progress - need to use operators to extract funds
def bet_way():
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute("SELECT * FROM funds")
    
    
    
#create a column in the db that collates and always has the total