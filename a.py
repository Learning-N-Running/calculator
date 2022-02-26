all_group_list = ['얄라얄라','숭숭','얄라리','송얄라','안녕 클레오파트라 세상에서 제일 가는 포테이토칩']
searstng = str(input())

#정직하게
n = len(searstng)
sear_result_list = []
# for group in all_group_list:
#     k = len(group)
#     if k>=n:
#         for i in range(k-n+1):
#             if group[i:i+n]==searstng:
#                 sear_result_list.append(group)
#                 break

#검색어에서 공백을 빼자
s = searstng.replace(" ",'')
p = len(s)
for group in all_group_list:
    t = group.replace(" ",'')
    j = len(t)
    if j>=p:
        for i in range(j-p+1):
            if t[i:i+p]==s:
                sear_result_list.append(group)
                break

print(sear_result_list)