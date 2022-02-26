##그룹 찾기 했을 때 나오는 창
from cgitb import text
from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter.ttk import Labelframe
from tkinter.font import *
from UserInfoDB import get_all_groups




class searchgroup:
    def __init__(self,newin):
        self.newin = newin
        self.newin.title("그룹 찾기")
        self.newin.geometry("640x480")
        self.newin.resizable(False,False)

        all_group_list= get_all_groups()

        self.font1=Font(family="맑은 고딕", size=30)
        self.font2=Font(family="맑은 고딕", size=15)

        self.left_space_frame = Frame(self.newin,width=60)
        self.left_space_frame.pack(fill='y',side='left')

        self.right_space_frame = Frame(self.newin,width=60)
        self.right_space_frame.pack(fill='y',side='right')
        
        self.top_space_frame = Frame(self.newin,height=30)
        self.top_space_frame.pack(fill='x',side='top')


        self.second_space_frame = Frame(self.newin,height=60)
        self.second_space_frame.pack(fill='x',side='top')        

        Label(self.second_space_frame,text='그룹 이름으로 검색하세요.',font=self.font2).pack()


        self.third_space_frame = Frame(self.newin,height=60)
        self.third_space_frame.pack(fill='x',side='top') 

        self.search_var = StringVar()
        self.search_bar_entry = Entry(self.third_space_frame,width=30,font=self.font2,textvariable=self.search_var)
        self.search_bar_entry.pack(pady=10)


        self.fourth_space_frame = Frame(self.newin,height=60)
        self.fourth_space_frame.pack(fill='x',side='top')

        self.search_setting_button = Button(self.fourth_space_frame,text="검색 설정",font=self.font2)
        self.search_setting_button.pack(pady=5)


        self.fifth_space_frame = Frame(self.newin)
        self.fifth_space_frame.pack(fill='both',side='top',expand=True)
            # 찾은 그룹들 버튼이 나타나는 scrollable
        self.container = Frame(self.fifth_space_frame,bd=1,relief='solid')
        self.container.pack(side='left',fill='both',expand=True)

        self.canvas = Canvas(self.container) 
        self.canvas.pack(side='left',fill='both',expand=True)

        self.scrollbar = ttk.Scrollbar(self.container,orient="vertical",command=self.canvas.yview)
        self.scrollbar.pack(side='right',fill='y')
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion= self.canvas.bbox("all")
            )
        )
        # self.scrollable_frame.configure(bg='red')

        self.canvas.create_window((0,0),window=self.scrollable_frame,anchor='nw')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)


        for i in range(7,0,-1):
            Button(self.scrollable_frame, text="Sample scrolling button{}".format(i),width=44,height= 1,font=self.font2).pack()





if __name__ =="__main__":
    root = Tk()
    root.title('원래 거')
    root.geometry('300x300')
    win = Toplevel(root)
    sg_win = searchgroup(win)    
    root.mainloop()