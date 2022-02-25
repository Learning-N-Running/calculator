from ast import expr_context
import encodings
from tkinter import messagebox
import sqlite3
import os


#지우면 안됨.
# cur.execute('CREATE TABLE UserTable(id char(15), UserName char(5), email char(25), password char(15))')
con = sqlite3.connect("temp.db")
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS UserGroup(groupId INTEGER PRIMARY KEY, groupName VARCHAR(30) unique, groupPw VARCHAR(15));')
cur.execute('CREATE TABLE IF NOT EXISTS Participation(groupId INTEGER, userId char(15), PRIMARY KEY(groupId, userId));')
con.commit()
con.close()

#db 초기화
def init_db_when_start():
    if os.path.isfile('login_info.txt'):
        os.remove('login_info.txt')
    if os.path.isfile("temp.db"):
        os.remove("temp.db")
    con = sqlite3.connect("temp.db")
    cur = con.cursor()
    f = open('dump_script.sql','r')
    datas = f.readlines()
    for data in datas:
        if data.startswith('INSERT INTO'):
            cur.execute(data)
        elif data.startswith('CREATE TABLE'):
            cur.execute(data)
    con.commit()
    with con:
        with open("dump_script.sql", 'w',encoding='utf-8') as f:
            for line in con.iterdump():
                f.write('%s\n' % line)
    con.close()



def userUpdate(userId, userName, sendTo, password):
    con = sqlite3.connect("temp.db")
    cur = con.cursor()
    cur.execute("INSERT INTO UserTable VALUES(?, ?, ?, ?)", (userId, userName, sendTo, password))
    # print(userId)
    con.commit()

    #확인을 위해 UserTable도 같이 불러오게 만듦. 최종적으로는 지워야 할 부분
    cur.execute("SELECT * FROM UserTable")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    #db 파일의 내용을 dump_script.sql에 저장한다는 내용
    with con:
        with open("dump_script.sql", 'w',encoding='utf-8') as f:
            for line in con.iterdump():
                f.write('%s\n' % line)

    con.close()


def confirm_id_dup(userId):
    con = sqlite3.connect("temp.db")
    cur = con.cursor()

    sen = 'Select userName From UserTable WHERE id="{}"'.format(userId)
    cur.execute(sen)
    id_dup_switch = cur.fetchone()
    if id_dup_switch == None:
        print('중복이 아닙니다.')
        con.close()
        return userId
    else:
        print('중복입니다')
        con.close()
        return False
    

def delete(userId):
    con = sqlite3.connect("temp.db")
    cur = con.cursor()
    sen = 'Delete From UserTable WHERE id= "{}"'.format(userId)
    cur.execute(sen)
    con.commit()
    with con:
        with open("dump_script.sql", 'w',encoding='utf-8') as f:
            for line in con.iterdump():
                f.write('%s\n' % line)
    con.close()


def login_check(real_userId): #아이디 비번 대조하는 것
    ready_login_check=False
    con = sqlite3.connect("temp.db")
    cur = con.cursor()
    try:
        sen = 'Select password From UserTable WHERE id="{}"'.format(real_userId)
        cur.execute(sen)
        login_password = ''.join(cur.fetchone())   ##문제 발생 가능 지점
        # print("입력하신 ID가 있군요!") #최종적으로는 지우자.
        con.close()
        ready_login_check=True

        return login_password,ready_login_check
    except TypeError:
        # print("입력하신 ID는 없습니다.")
        con.close()
        login_password= 0
        return login_password ,ready_login_check

def insertData(groupName, groupPw):
    con = sqlite3.connect("temp.db")
    cur = con.cursor()
    cur.execute("select count(*) from UserGroup")
    groupId = cur.fetchone()[0] + 1

    with open("login_info.txt", "a", encoding="utf-8") as f:
        f.write("{}\n".format(groupId))
        f.close()

    cur.execute("insert into UserGroup VALUES(?, ?, ?)", (groupId, groupName, groupPw))

    con.commit()
    insertParticipation()
    with con:
        with open("dump_script.sql", 'w',encoding='utf-8') as f:
            for line in con.iterdump():
                f.write('%s\n' % line)

    con.close()

def getGroupInfo():
    con = sqlite3.connect("temp.db")
    cur = con.cursor()
    with open("login_info.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()    
        user_id = lines[0][4:].rstrip(' \n')
        print(user_id)
        f.close()

    cur.execute('select groupName from UserGroup G where g.groupId IN(select p.groupId from Participation p where p.userId="{}")'.format(user_id))
    gName = cur.fetchall()
    
    return gName


def find_username_email(login_id):
    con = sqlite3.connect("temp.db")
    cur = con.cursor()
    sen = 'Select UserName From UserTable WHERE id="{}"'.format(login_id)
    cur.execute(sen)
    username_for_watchmyinfo = ''.join(cur.fetchone())
    sen = 'Select email From UserTable WHERE id="{}"'.format(login_id)
    cur.execute(sen)
    email_for_watchmyinfo = ''.join(cur.fetchone())
    return username_for_watchmyinfo,email_for_watchmyinfo

def change_pw(present_pw,new_pw):
    con = sqlite3.connect("temp.db")
    cur = con.cursor()
    sen = 'Update UserTable SET password="{}" WHERE password="{}"'.format(new_pw,present_pw)
    cur.execute(sen)
    con.commit()
    with con:
        with open("dump_script.sql", 'w',encoding='utf-8') as f:
            for line in con.iterdump():
                f.write('%s\n' % line)
    con.close()

def insertParticipation():
    con = sqlite3.connect("temp.db")
    cur = con.cursor()

    with open("login_info.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()    
        user_id = lines[0][4:].rstrip(" \n") 
        groupId = lines[-1]
        f.close()
    
    cur.execute("insert into Participation VALUES(?, ?)", (groupId, user_id))
    con.commit()
    con.close()

def find_user_group():
    if os.path.isfile('login_info.txt'):
        con = sqlite3.connect("temp.db")
        cur = con.cursor()
        with open('login_info.txt','r') as f:
            datas= f.readlines()
            for data in datas:
                data.strip()
                if data.startswith('id'):
                    login_id = data.split()[1]
                    break
        sen = 'Select groupId From Participation WHERE userId="{}"'.format(login_id)
        cur.execute(sen)
        group_ids = cur.fetchall()
        user_group_list= []
        for group_id in group_ids:
            sen = 'Select groupName From UserGroup WHERE groupId="{}"'.format(group_id[0])
            cur.execute(sen)
            user_group = cur.fetchone()[0]
            user_group_list.append(user_group)
        con.close()
        return user_group_list




# if __name__=='__main__':
#     con = sqlite3.connect("temp.db")
#     cur = con.cursor()
#     cur.execute("SELECT * FROM UserTable")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
#     con.close()

# login_check('tina_id')
# delete('poo_id')

# confirm_id_dup('jk_id')

find_user_group()

