import csv
import sqlite3

engineers = []

def one_click():
    with open('data.csv', 'r') as file:
        for i in file:
            sorted = i.split(";")
            engineers = (sorted[0])
            date = (sorted[1])
            case_numbers = (sorted[2])
            status = (sorted[3])
            customers = (sorted[4])



            #write data columns to DB-Sqlite3
            # db_name = str(input("Enter Database name: \n"))
            # db_table = str(input("Enter Table name: \n"))
            # xcon = sqlite3.connect(db_name)

            # cur = xcon.cursor()
            # cur.execute(f"""CREATE TABLE {db_table}(
            #             engineers text,
            #             case_number integer,
            #             status text,
            #             customers text
            #      )""")
            # # xcon.commit()
            
            # cur.close()
            # xcon.close()
            # print("Database created successfully")
            xcon = sqlite3.connect('kpi')
            xcon = sqlite3.connect('python')
            x = xcon.cursor()
            x.execute("INSERT INTO kpi ('engineers','case_number','status','customers') VALUES(?,?,?,?)", ((sorted[0]), (sorted[2]), (sorted[3]), sorted[4]))
            xcon.commit()
            x.close()
            xcon.close()
            print("Success written to db")

# def db_write():
#     global sorted
#     xcon = sqlite3.connect('python')
#     x = xcon.cursor()
#     x.execute("INSERT INTO kpi ('engineers','case_number','status','customers') VALUES(?,?,?,?)", ((sorted), (sorted[2]), (sorted[3]), sorted[4]))
#     xcon.commit()
#     x.close()
#     xcon.close()
#     print("Success written to db")

one_click()

        
