#방 만들고 들어갔을 때 
from tkinter import *
from tkinter.font import *
import tkinter.messagebox as msgbox
from tkinter import ttk

def openFrame(frame):
    frame.tkraise()

class grouproom:
    def __init__(self,groupName):
        self.window = Tk()
        self.groupName = groupName  #여기다가 모임 이름 넣으면 좋을 듯
        self.window.title(self.groupName)  
        self.window.geometry("640x480")
        self.window.resizable(False,False)

        self.font1=Font(family="맑은 고딕", size=30)
        self.font2=Font(family="맑은 고딕", size=15)
        
        self.group_name_label = Label(self.window, text=self.groupName, font=self.font1)
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
        self.group_member_frame = Frame(self.window,width=560,height=30)
        self.group_member_frame.pack(side='top')
        self.group_member_label = Label(self.group_member_frame,text="참여자:", font=self.font2)
        self.group_member_label.pack(side='left')


            #이건 db에서 갖고 와서 넣어줘야 함

            #모임 참여자 scrollable frame
        self.group_member_container = Frame(self.group_member_frame,width=320,height=40)
        self.group_member_container.pack(side='left',fill='both', expand=True,padx=5)
        self.group_member_container.configure(bg='red')

        self.group_member_canvas = Canvas(self.group_member_container,width=320,height=40)
        self.group_member_canvas.pack(side='top',fill='both',expand=True)
        self.group_member_canvas.configure(bg='green')


        self.group_member_scrollbar = ttk.Scrollbar(self.group_member_container,orient="horizontal",command=self.group_member_canvas.xview)
        self.group_member_scrollbar.pack(side='bottom',fill='x')
        self.group_member_scrollable_frame = ttk.Frame(self.group_member_canvas)

        self.group_member_scrollable_frame.bind(
            "<Configure>",
            lambda e: self.group_member_canvas.configure(
                scrollregion= self.group_member_canvas.bbox("all")
            )
        )
        self.group_member_canvas.create_window((0,0),window=self.group_member_scrollable_frame,anchor='n')
        self.group_member_canvas.configure(xscrollcommand=self.group_member_scrollbar.set)

        for i in range(10):
            line = Button(self.group_member_scrollable_frame, text="이름{}".format(i),width=8,height= 3)
            globals()['self.button{}.format(i)'] = line
            globals()['self.button{}.format(i)'].pack(side='left')
        
            #그룹 멤버 추가, 삭제 버튼
        self.group_member_delete_button = Button(self.group_member_frame,text="삭제",font=self.font2,width=4)
        self.group_member_delete_button.pack(side='right',ipadx=2,padx=2)
        self.group_member_delete_button.configure(fg='red')

        self.group_member_add_button = Button(self.group_member_frame,text="추가",font=self.font2,width=4)
        self.group_member_add_button.pack(side='right',ipadx=2)
        self.group_member_add_button.configure(fg='green')



        #이전으로 ,이벤트 추가 프레임
        self.add_event_frame = Frame(self.window)
        self.add_event_frame.pack(side='top',ipadx=280,ipady=0) 

        self.go_back_button = Button(self.add_event_frame, text='이전으로',font=self.font2)
        self.go_back_button.pack(side='left',ipadx=5)

        self.add_event_button = Button(self.add_event_frame, text='이벤트 추가',font=self.font2)
        self.add_event_button.pack(side='right',ipadx=5)

            #이벤트 버튼 scrollable frame
        self.add_event_container = Frame(self.window,bd=1,relief='solid')
        self.add_event_container.pack(side='left',fill='both',expand=True,pady=5)

        self.add_event_canvas = Canvas(self.add_event_container) 
        self.add_event_canvas.pack(side='left',fill='both',expand=True)

        self.add_event_scrollbar = ttk.Scrollbar(self.add_event_container,orient="vertical",command=self.add_event_canvas.yview)
        self.add_event_scrollbar.pack(side='right',fill='y')

        self.add_event_scrollable_frame = Frame(self.add_event_canvas)

        self.add_event_scrollable_frame.bind(
            "<Configure>",
            lambda e: self.add_event_canvas.configure(
                scrollregion= self.add_event_canvas.bbox("all")
            )
        )

        self.add_event_canvas.create_window((0,0),window=self.add_event_scrollable_frame,anchor='nw',width=560)
        self.add_event_canvas.configure(yscrollcommand=self.add_event_scrollbar.set)

        for i in range(10,0,-1):
            Button(self.add_event_scrollable_frame, text="Sample scrolling button{}".format(i),width=80,height= 7).pack()
            
if __name__=='__main__':
    a = grouproom()
    a.window.mainloop()