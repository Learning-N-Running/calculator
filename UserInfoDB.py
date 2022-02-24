from ast import expr_context
import sqlite3
import os

#지우면 안됨.
# cur.execute('CREATE TABLE UserTable(id char(15), UserName char(5), email char(25), password char(15))')
# CREATE TABLE UserGroup(groupId INTEGER PRIMARY KEY, groupName TEXT, groupSite CHAR(25), groupPw VARCHAR(15));


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

def insertData(groupName, groupSite, groupPw):
    con = sqlite3.connect("temp.db")
    cur = con.cursor()
    cur.execute("select count(*) from UserGroup")
    groupId = cur.fetchone()[0] + 1

    cur.execute("INSERT INTO UserGroup VALUES(?, ?, ?, ?)", (groupId, groupName, groupSite, groupPw))
    con.commit()

    #확인을 위해 UserGroup도 같이 불러오게 만듦. 최종적으로는 지워야 할 부분
    cur.execute("SELECT * FROM UserGroup")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    with con:
        with open("dump_script.sql", 'w',encoding='utf-8') as f:
            for line in con.iterdump():
                f.write('%s\n' % line)

    con.close()

def getGroupInfo():
    con = sqlite3.connect("temp.db")
    cur = con.cursor()
    cur.execute("select groupName from UserGroup")
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
confirm_id_dup('jk_id')

