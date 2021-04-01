# Author Om Rawal
# 01/04/2021 09:22

import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from chatbot_api import *


def query_transact(win, cb, query, qe):
    response = cb.query(query)
    qe.delete(0, tk.END)
    if('Thanks.'in response):
        messagebox.showinfo('Success',
                            response)
        ans = []
        if(cb.flow == 1):
            ans.append('Flight details are:\n')
            ans.append('Source: '+cb.source1+'\n')
            ans.append('Destination: '+cb.dest1+'\n')
            ans.append('Date: '+cb.date1+'\n')
        elif(cb.flow == 2):
            ans.append('Hotel details are:\n')
            ans.append('Destination: '+cb.dest2+'\n')
            ans.append('Date: '+cb.date2+'\n')
            ans.append('Duration: '+cb.duration2+'\n')
        elif(cb.flow == 3):
            ans.append('Cab details are:\n')
            ans.append('Source: '+cb.source3+'\n')
            ans.append('Destination: '+cb.dest3+'\n')
            ans.append('Date: '+cb.date3+'\n')
            ans.append('Duration: '+cb.duration3+'\n')
        text = "".join(ans)
        messagebox.showinfo('Success',
                            text)
    else:
        messagebox.showinfo('Success',
                            response)


cb = Chatbot()
root = tk.Tk()
root.title("Travel Booking Chatbot")
root.geometry("300x300")
greeting_label = tk.Label(
    root, text="Please type your Query below!", font=10)
greeting_label.place(x=10, y=50)

query_entry = tk.Entry(root, font=10)
query_entry.place(x=50, y=100)
query_button = tk.Button(
    root, text="Send", font=10, command=lambda: query_transact(win=root, cb=cb, query=query_entry.get(), qe=query_entry))
query_button.place(x=120, y=200)

root.mainloop()
