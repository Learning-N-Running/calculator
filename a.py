all_group_list = ['얄라얄라','숭숭','얄라리','송얄라']
searstng = str(input())
n = len(searstng)
sear_result_list = []
for group in all_group_list:
    k = len(group)
    if k>=n:
        for i in range(k-n+1):
            if group[i:i+n]==searstng:
                sear_result_list.append(group)
                break
print(sear_result_list)