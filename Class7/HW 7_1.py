import pygsheets
from tkinter import *
import pandas as pd
root=Tk()
root.title("Google Sheet API")
root.geometry("400x500")

gc = pygsheets.authorize(service_file="Project/causal-scarab-383206-d3edf987cf5e.json")
sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/1mpgr_6vPS_pSIxFawYWXU9czJPpZq4Q-c9j7y5wlYHM/edit#gid=0")
ws = sht[0]
ws = sht.worksheet_by_title("Homework 7_1")
i = 1
def add_customer():
    global i
    i += 1
    ws.update_value("A"+str(i), name_entry.get())
    ws.update_value("B"+str(i), email_entry.get())
    ws.update_value("C"+str(i), password_entry.get())
    ws.update_value("D"+str(i), phone_entry.get())

name_label = Label(root, text='姓名：')
name_label.grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)
email_label = Label(root, text='電子郵件：')
email_label.grid(row=1, column=0)
email_entry = Entry(root)
email_entry.grid(row=1, column=1)
password_label = Label(root, text='密碼：')
password_label.grid(row=2, column=0)
password_entry = Entry(root, show='*')
password_entry.grid(row=2, column=1)
phone_label = Label(root, text='電話號碼：')
phone_label.grid(row=3, column=0)
phone_entry = Entry(root)
phone_entry.grid(row=3, column=1)
submit_button = Button(root, text='註冊', command=add_customer)
submit_button.grid(row=4, column=1)
result_label = Label(root)
result_label.grid(row=5, column=1)


root.mainloop()