from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter.font import *

# all_group_list = ['얄라얄라','숭숭','얄라리','송얄라','안녕 클레오파트라 세상에서 제일 가는 포테이토칩']
# searstng = str(input())

# #정직하게
# n = len(searstng)
# sear_result_list = []
# # for group in all_group_list:
# #     k = len(group)
# #     if k>=n:
# #         for i in range(k-n+1):
# #             if group[i:i+n]==searstng:
# #                 sear_result_list.append(group)
# #                 break

# #검색어에서 공백을 빼자
# s = searstng.replace(" ",'')
# p = len(s)
# for group in all_group_list:
#     t = group.replace(" ",'')
#     j = len(t)
#     if j>=p:
#         for i in range(j-p+1):
#             if t[i:i+p]==s:
#                 sear_result_list.append(group)
#                 break

# print(sear_result_list)


# win = Tk()
# sear_result = '00그룹'
# win.title("{} 가입".format(sear_result))
# win.geometry('400x300')
# font1=Font(family="맑은 고딕", size=30)
# font2=Font(family="맑은 고딕", size=15)
# font3=Font(family="맑은 고딕", size=25)
# join_lab = Label(win,text="{} 가입".format(sear_result),font=font3)
# join_lab.pack(side='top',pady=20)
# top_space_frame = Frame(win,height=70)
# top_space_frame.pack(fill='x',side='top')
# pw_frame = Frame(win)
# pw_frame.pack(side='top')
# pw_label = Label(pw_frame,text="비밀번호: ",font=font2)
# pw_label.pack(side='left',padx=10)
# pw_entry = Entry(pw_frame,font=font2)
# pw_entry.pack(side='left')
# join_frame= Frame(win)
# join_frame.pack(side='top',pady=20)
# join_button = Button(join_frame,text='가입',font=font2,width=10)
# join_button.pack()
# win.mainloop()

window = tk.Tk()
window.title("계산기")
window.geometry("640x480")
import tkinter.messagebox as msgbox
import email_test as et

#여기서부터 다른 점
from UserInfoDB import find_id

window.title("비밀번호 찾기")
window.geometry("310x300")
find_pw_frame = Frame(window)
find_pw_frame.pack()
font1=Font(family="맑은 고딕", size=30)
font2=Font(family="맑은 고딕", size=15)

Label(find_pw_frame,text="비밀번호 찾기",font=font1).pack(pady=10)

find_pw_inputid_frame = Frame(find_pw_frame)
find_pw_inputid_frame.pack(padx=10)

Label(find_pw_inputid_frame,text="ID:",font=font2).pack(pady=10,side='left')

find_pw_inputid_entry = Entry(find_pw_inputid_frame,font=font2,width=20)
find_pw_inputid_entry.pack(padx=5,side='left')

find_pw_find_button = Button(find_pw_frame,text="찾기",font=font2,command=lambda:[find_id_find_button_func()],width=10)
find_pw_find_button.pack(pady=10)

go_back_button = Button(find_pw_frame,text="이전으로",font=font2)
go_back_button.pack(pady=10, side="left",fill='x',expand=True)

def find_id_find_button_func():
    id_list = find_id(find_pw_inputid_entry.get())
    blank_list = [' '*n for n in range(1,11)]
    blank_list.append('')
    if find_pw_inputid_entry.get() in blank_list:
        msgbox.showwarning("빈칸 입력","등록하신 이메일을 입력하세요.")
    else:
        if id_list==[]:
            msgbox.showwarning("등록되지 않은 이메일","등록되지 않은 이메일입니다.")
            print("등록되지 않은 이메일입니다.")
        else:
            msgbox.showinfo("ID 전송","{}로 ID를 보냈습니다.\n확인해주세요.".format(find_pw_inputid_entry.get()))
            et.sendEmail_find_id(find_pw_inputid_entry.get(),id_list)
window.mainloop()