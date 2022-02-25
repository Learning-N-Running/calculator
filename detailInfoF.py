import tkinter as tk
from tkinter import Toplevel, font as tkfont

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        
        self.geometry("600x400")
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

        tk.Label(self, text="날짜").place(x=40, y=40)
        tk.Label(self, text="장소").place(x=40, y=90)

        tk.Entry(self).place(x=80, y=40)
        tk.Entry(self).place(x=80, y=90)
        
        text = tk.Text(self, height=15, width=30)
        text.place(x=40, y=130)

        button1 = tk.Button(self, text="모임원 추가", width=25,
                            command=lambda: controller.add_member())
        button2 = tk.Button(self, text="일정관리", width=25,
                            command=lambda: controller.show_frame("Schedule"))
        button3 = tk.Button(self, text="소비내역", width=25,
                            command=lambda: controller.show_frame("Amount"))

        button1.place(x=40, y=350)
        button2.place(x=200, y=350)
        button3.place(x=360, y=350)

        listbox = tk.Listbox(self, selectmode="extended", width=30, height=18)
        listbox.insert(0, "1")
        listbox.insert(1, "2")
        listbox.insert(2, "3")
        listbox.insert(3, "4")
        listbox.place(x=330, y=40)


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
    app = SampleApp()
    app.mainloop()
