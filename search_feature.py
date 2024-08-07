import pandas as pd
import string
import datetime
from datetime import time
count = 0
array = []

new_array = []
with open('data.txt') as file:
    text = file.readlines()
    for data in text:
        array.append(data.replace(" ", ",").split(","))
        

        
    #user = str(input("enter search phrase:\n"))
    # for i in array[0]:
        
    #     if user in i:
    #         count += 1
    #         print(f"Found {user} {count} time(s)")
    #         break
            
    #     else:
    #         print('not found')
                
        # for i in array[0]:
        
        #     user = str(input("enter search phrase:\n"))
        #     if user in i:
        #         count += 1
                
        #         print(f"Found {user} {count} time(s)")
            
        #     else:
        #         print('not found')
    

