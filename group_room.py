#방 만들고 들어갔을 때 
from cProfile import label
from cgitb import text
from textwrap import fill
from tkinter import *
from tkinter.font import *
import tkinter.messagebox as msgbox

def openFrame(frame):
    frame.tkraise()

class grouproom:
    def __init__(self):
        self.window = Tk()
        self.group_name = "00그룹"  #여기다가 모임 이름 넣으면 좋을 듯
        self.window.title(self.group_name)  
        self.window.geometry("640x480")
        self.window.resizable(False,False)

        self.font1=Font(family="맑은 고딕", size=30)
        self.font2=Font(family="맑은 고딕", size=15)

        # self.top_space_label = Label(self.window,text="",padx=320)
        # self.top_space_label.pack()
        # self.top_space_label.configure(bg = 'blue')

        self.group_name_label = Label(self.window, text=self.group_name, font=self.font1)
        self.group_name_label.pack(pady=20)

        self.left_space_label = Label(self.window,text="")
        self.left_space_label.pack(ipadx=20,ipady=220,side="left")
        # self.left_space_label.configure(bg= 'red')  #마지막에는 지워.

        self.right_space_label = Label(self.window,text="")
        self.right_space_label.pack(ipadx=20,ipady=220,side="right")
        # self.right_space_label.configure(bg= 'green') #마지막에는 지워

        self.bottom_space_label = Label(self.window,text="")
        self.bottom_space_label.pack(ipadx=270,ipady=10,side="bottom")
        # self.bottom_space_label.configure(bg="yellow")  #마지막에는 지워

        #모임참여자, entry,추가, 제거가 들어갈 프레임
        self.group_member_frame = Frame(self.window)
        self.group_member_frame.pack(side='top',ipadx=280,ipady=5)

        self.group_member_label = Label(self.group_member_frame,text="참여자:", font=self.font2)
        self.group_member_label.pack(side='left')


            #이건 db에서 갖고 와서 넣어줘야 함
        self.group_member_list_label = Label(self.group_member_frame,text='멤버들 이름',font=self.font2)
        self.group_member_list_label.pack(side='left',padx=5)

        self.group_member_delete_button = Button(self.group_member_frame,text="삭제",font=self.font2)
        self.group_member_delete_button.pack(side='right',ipadx=2)

        self.group_member_add_button = Button(self.group_member_frame,text="추가",font=self.font2)
        self.group_member_add_button.pack(side='right',ipadx=2)


        #이벤트 추가 프레임
        self.add_event_frame = Frame(self.window)
        self.add_event_frame.pack(side='top',ipadx=280,ipady=0) 

        self.add_event_button = Button(self.add_event_frame, text='이벤트 추가',font=self.font2)
        self.add_event_button.pack(side='left',ipadx=5)

        #이벤트 프레임
        self.event_frame = Frame(self.window,bd=1,relief='solid')
        self.event_frame.pack(side='top',ipadx=280,ipady=120,pady=5)  

a = grouproom()
a.window.mainloop()