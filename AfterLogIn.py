from tkinter import *
import tkinter.messagebox as msgbox
from tkinter.ttk import Labelframe

window = Tk()
window.title("계산기")
window.geometry("640x480")

menu = Menu(window)

#함수 정리
def CheckMyInfo():
    print("내 정보를 확인합니다.")

def ChangePW():
    response = msgbox.askokcancel("비밀번호 변경 확인","비밀번호를 변경하시겠습니까?")
    if response==1: #확인
        print("비밀번호를 변경합니다.")

def AddGroup():
    print("그룹을 추가합니다.")

def SearchGroup():
    print("그룹을 찾습니다")

#메뉴 
menu_info = Menu(menu,tearoff=0)
menu_info.add_command(label="내 정보 확인",command=CheckMyInfo)
menu_info.add_command(label="비밀번호 변경",command=ChangePW)
menu.add_cascade(label="내정보",menu=menu_info)

#그룹 추가, 찾기 프레임
frame_addsearch_group = Frame(window)
frame_addsearch_group.pack(fill="x",padx = 5,pady=10)

btn_add_group=Button(frame_addsearch_group,padx=5,pady=5,width=12,text="그룹 추가",command=AddGroup)
btn_add_group.pack(side="left")

btn_search_group=Button(frame_addsearch_group,padx=5,pady=5,width=12,text="그룹 찾기",command=SearchGroup)
btn_search_group.pack(side="right")

#그룹들 프레임
frame_group = LabelFrame(window,text="내 그룹",relief="solid",bd=1)
frame_group.pack(fill='both',expand=True,padx=10,pady=10)

group_scrollbar = Scrollbar(frame_group)
group_scrollbar.pack(side='right',fill='y')

group_list = Listbox(frame_group,selectmode='single',yscrollcommand=group_scrollbar.set)
#height값을 줘야할지 말아야할지 고민
group_list.pack(side='left', fill='both',expand=True)

group_scrollbar.config(command=group_list.yview)



window.config(menu=menu)
window.mainloop()