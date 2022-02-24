from a import *

f = open('a.py','w')
f.write("a=[1,2,3,4,5]")
f.close()

print(a)
# datas = f.readlines()
# for data in datas:
#     data = data.strip()
#     strlist = data.split()[1]
#     strlist = strlist.replace('[','')
#     strlist = strlist.replace(']','')
#     list = strlist.split(',')
#     print(list)