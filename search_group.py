##그룹 찾기 했을 때 나오는 창
from cgitb import text
from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter.ttk import Labelframe
from tkinter.font import *
from UserInfoDB import get_all_groups,find_user_group


    


class make_search_group_class():
    def __init__(self,parent,sear_result):
        self.sear_result = sear_result
        # self.sear_result_button = Button(parent.search_group_scrollable_frame, text=self.sear_result,width=8,height= 3,command=lambda:[self.group_member_button_func(parent)]).pack()
        self.sear_result_button = Button(parent.search_group_scrollable_frame, text=self.sear_result,width=44,height= 1,font=parent.font2,command=lambda:[self.sear_result_button_func(parent)]).pack()

    def sear_result_button_func(self,parent):
        if self.sear_result in parent.user_group_list:
            msgbox.showinfo('이미 속한 그룹',"이미 속해있는 그룹입니다.")
            print("이미 속해있는 그룹입니다.")
            parent.newin.tkraise()
        else:
            print(self.sear_result)
            self.win = Toplevel(parent.newin)
            self.win.title("{} 가입".format(self.sear_result))
            self.win.geometry('400x400')





class searchgroup:
    def __init__(self,newin):
        self.newin = newin
        self.newin.title("그룹 찾기")
        self.newin.geometry("640x480")
        self.newin.resizable(False,False)

        self.all_group_list= get_all_groups()
        self.user_group_list = find_user_group()
        
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

        self.search_var.trace('w',self.callback)

        self.fourth_space_frame = Frame(self.newin,height=60)
        self.fourth_space_frame.pack(fill='x',side='top')

        self.search_setting_button = Button(self.fourth_space_frame,text="검색 설정",font=self.font2)
        self.search_setting_button.pack(pady=5)


        self.fifth_space_frame = Frame(self.newin)
        self.fifth_space_frame.pack(fill='both',side='top',expand=True,pady=5)
            # 찾은 그룹들 버튼이 나타나는 scrollable
        self.search_group_container = Frame(self.fifth_space_frame,bd=1,relief='solid')
        self.search_group_container.pack(side='left',fill='both',expand=True)

        self.search_group_canvas = Canvas(self.search_group_container) 
        self.search_group_canvas.pack(side='left',fill='both',expand=True)

        self.search_group_scrollbar = ttk.Scrollbar(self.search_group_container,orient="vertical",command=self.search_group_canvas.yview)
        self.search_group_scrollbar.pack(side='right',fill='y')
        self.search_group_scrollable_frame = ttk.Frame(self.search_group_canvas)
        self.search_group_scrollable_frame.bind(
            "<Configure>",
            lambda e: self.search_group_canvas.configure(
                scrollregion= self.search_group_canvas.bbox("all")
            )
        )
        # self.scrollable_frame.configure(bg='red')

        self.search_group_canvas.create_window((0,0),window=self.search_group_scrollable_frame,anchor='nw')
        self.search_group_canvas.configure(yscrollcommand=self.search_group_scrollbar.set)


        # for i in ['A','B','C']:
        #     # Button(self.search_group_scrollable_frame, text="Sample scrolling button{}".format(i),width=44,height= 1,font=self.font2).pack()
        #     globals()['self.{}_search_group_class'.format(i)] = make_search_group_class(self,i)
        
        for i in self.all_group_list:
            # Button(self.search_group_scrollable_frame, text="Sample scrolling button{}".format(i),width=44,height= 1,font=self.font2).pack()
            globals()['self.{}_search_group_class'.format(i)] = make_search_group_class(self,i)


    def callback(self,*args):
        try:
            self.search_group_scrollable_frame.destroy()
            self.search_group_scrollable_frame = ttk.Frame(self.search_group_canvas)
            self.search_group_scrollable_frame.bind(
                "<Configure>",
                lambda e: self.search_group_canvas.configure(
                    scrollregion= self.search_group_canvas.bbox("all")
                )
            )

            self.search_group_canvas.create_window((0,0),window=self.search_group_scrollable_frame,anchor='nw')
            self.search_group_canvas.configure(yscrollcommand=self.search_group_scrollbar.set)
        except:
            pass
        
        #검색 조건
        searstng = self.search_var.get()
        sear_result_list = []

        # #'A B'라는 이름의 그룹을 검색하려 할 때 'AB'를 입력하면 검색이 안되는 경우.
        # n = len(searstng)
        # for group in self.all_group_list:
        #     k = len(group)
        #     if k>=n:
        #         for i in range(k-n+1):
        #             if group[i:i+n]==searstng:
        #                 sear_result_list.append(group)
        #                 break

        #'A B'라는 이름의 그룹을 검색하려 할 때 'AB'or 'A  B'를 입력해도 검색이 되는 경우. 중간중간 공백이 있어도 출력이 됨.
        s = searstng.replace(" ",'')
        p = len(s)
        for group in self.all_group_list:
            t = group.replace(" ",'')
            j = len(t)
            if j>=p:
                for i in range(j-p+1):
                    if t[i:i+p]==s:
                        sear_result_list.append(group)
                        break
        
        for sear_result in sear_result_list:
            globals()['self.{}_search_group_class'.format(sear_result)] = make_search_group_class(self,sear_result)


        





if __name__ =="__main__":
    root = Tk()
    root.title('원래 거')
    root.geometry('300x300')
    win = Toplevel(root)
    sg_win = searchgroup(win)    
    root.mainloop()