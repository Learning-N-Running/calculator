from cgitb import text
import tkinter as tk
from tkinter import StringVar, Toplevel, font as tkfont
from tkcalendar import DateEntry 

from UserInfoDB import insertEventInfo

class SampleApp(tk.Tk):

    def __init__(self,event,groupName, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        
        self.geometry("640x480")

        self.event = event
        self.groupName = groupName

        self.title('[{}] - [{}]'.format(self.groupName,self.event))

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Home, Schedule, Amount):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def add_member(self):
        add_member = Toplevel(self)
        add_member.geometry("400x380")
        add_member.title("모임원을 추가합니다.")

        tk.Label(add_member, text="ID").pack()
        tk.Entry(add_member).pack()
        tk.Button(add_member, text="찾기").pack()



class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.event_site = StringVar()
        self.event_date = StringVar()
        self.event_memo = StringVar()

        tk.Label(self, text="날짜").place(x=50, y=50)
        tk.Label(self, text="장소").place(x=50, y=100)

        self.eventSite = tk.Entry(self, textvariable=self.event_site)
        self.eventSite.place(x=90, y=50)

        self.eventMemo = tk.Text(self, height=10, width=30)
        self.eventMemo.place(x=50, y=170)

        eventDate=DateEntry(self,selectmode='day', textvariable=self.event_date)
        eventDate.place(x=90, y=100)

        self.dateBtn = tk.Button(self, text="확인", command=self.date_upd)
        self.dateBtn.place(x=220, y=100)

        self.dateLb = tk.Label(self, text="")
        self.dateLb.place(x=200, y=135)
        
        button1 = tk.Button(self, text="모임원 추가", width=25,
                            command=lambda: controller.add_member())
        button2 = tk.Button(self, text="일정관리", width=25,
                            command=lambda: controller.show_frame("Schedule"))
        button3 = tk.Button(self, text="소비내역", width=25,
                            command=lambda: controller.show_frame("Amount"))
        button4 = tk.Button(self, text="저장", width=25, command=self.insert_eventInfo)


        button1.place(x=50, y=360)
        button2.place(x=210, y=360)
        button3.place(x=370, y=360)
        button4.place(x=370, y = 400)

        listbox = tk.Listbox(self, selectmode="extended", width=30, height=18)
        listbox.insert(0, "1")
        listbox.insert(1, "2")
        listbox.insert(2, "3")
        listbox.insert(3, "4")
        listbox.place(x=340, y=50)
    
    def date_upd(self):
        self.dateLb.config(text=self.event_date.get())

    def callback(*args, sv):
        pass
    
    def insert_eventInfo(self):
        self.event_site.trace('w', self.callback(sv = self.eventSite))
        self.event_memo.trace('w', self.callback(sv = self.eventMemo))

        insertEventInfo(self.event_site.get(), self.event_date.get(), self.eventMemo.get("1.0", "end-1c"))

class Schedule(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="일정관리", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="모임원 추가", width=25,
                            command=lambda: controller.add_member())
        button2 = tk.Button(self, text="홈", width=25,
                            command=lambda: controller.show_frame("Home"))
        button3 = tk.Button(self, text="소비내역", width=25,
                            command=lambda: controller.show_frame("Amount"))

        button1.place(x=40, y=350)
        button2.place(x=200, y=350)
        button3.place(x=360, y=350)


class Amount(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="소비내역", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="모임원 추가", width=25,
                            command=lambda: controller.add_member())
        button2 = tk.Button(self, text="홈", width=25,
                            command=lambda: controller.show_frame("Home"))
        button3 = tk.Button(self, text="일정관리", width=25,
                            command=lambda: controller.show_frame("Schedule"))

        button1.place(x=40, y=350)
        button2.place(x=200, y=350)
        button3.place(x=360, y=350)


if __name__ == "__main__":
    app = SampleApp('event','groupname')
    app.mainloop()
