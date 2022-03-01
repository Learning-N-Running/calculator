from tkinter import *
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


win = Tk()
sear_result = '00그룹'
win.title("{} 가입".format(sear_result))
win.geometry('400x300')
font1=Font(family="맑은 고딕", size=30)
font2=Font(family="맑은 고딕", size=15)
font3=Font(family="맑은 고딕", size=25)
join_lab = Label(win,text="{} 가입".format(sear_result),font=font3)
join_lab.pack(side='top',pady=20)
top_space_frame = Frame(win,height=70)
top_space_frame.pack(fill='x',side='top')
pw_frame = Frame(win)
pw_frame.pack(side='top')
pw_label = Label(pw_frame,text="비밀번호: ",font=font2)
pw_label.pack(side='left',padx=10)
pw_entry = Entry(pw_frame,font=font2)
pw_entry.pack(side='left')
join_frame= Frame(win)
join_frame.pack(side='top',pady=20)
join_button = Button(join_frame,text='가입',font=font2,width=10)
join_button.pack()
win.mainloop()