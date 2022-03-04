# with open("login_info.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()    
#     user_id = lines[0][4:]
#     group_id = lines[2]
#     print(group_id)
#     f.close()

# import calendar
# import tkinter as tk

# c = calendar.TextCalendar()
# m = c.formatmonth(2021, 3)

# root = tk.Tk()
# t = tk.Text(root, height=7, width=20)
# t.insert(tk.END, m)
# t.pack()
# tk.mainloop()

import tkinter  as tk 
from tkcalendar import DateEntry 
my_w = tk.Tk()
my_w.geometry("380x220")  

cal=DateEntry(my_w,selectmode='day')
cal.grid(row=1,column=1,padx=20,pady=30)

def my_upd(): # triggered on Button Click
    l1.config(text=cal.get_date()) # read and display date

l1=tk.Label(my_w,text='data',bg='yellow')  # Label to display date 
l1.grid(row=1,column=3)

b1=tk.Button(my_w,text='Read', command=lambda:my_upd())
b1.grid(row=1,column=2)
my_w.mainloop()