import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Mimecast API Token Generator")
root.geometry("350x150")
#Funtions
def request():
  url = "https://api.services.mimecast.com/oauth/token"
  #this is where we add our mimecast_IDs
  client_ID = entry1.get()
  secret_key = entry2.get()
  payload = f'client_id={client_ID}&client_secret={secret_key}&grant_type=client_credentials'
  headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
  }
  response = requests.request("POST", url,headers=headers, data=payload)
  messagebox.showwarning(title="Results", message=response)
  
def execute():
  global response
  requestUrl = "https://api.services.mimecast.com/api/audit/get-audit-events"
  requestBody = {}
  requestHeaders = {
    "Authorization": "Bearer " + input("Enter your access_token:\n"),
    "Accept": "application/json",
    "Content-Type": "application/json"
  }

  response = requests.post(requestUrl, headers=requestHeaders, json=requestBody)

  print(response)

  if __name__ == "__main__":
    execute()
    
#Gui labels
menu = Label(root, text="API Token Generator", font=("Calibri", 18, "bold"))

lable1 = Label(root, text="Enter Your client_ID:")
lable2 = Label(root, text="Enter Your secret_ID:")
button1 = Button(root,text="Generate", command=request)
exit_button=Button(text="Exit", command=root.destroy)

#Gui Entries
entry1 = Entry()
entry2 = Entry()
#Gui Positions
menu.grid(row=0, column=3)
lable1.grid(row=4,column=2)
lable2.grid(row=6, column=2)
entry1.grid(row=4,column=3)
entry2.grid(row=6,column=3)
button1.grid(row=8, column=3)
exit_button.grid(row=9, column=3)

root.mainloop()