from ast import expr_context
import encodings
from tkinter import messagebox
import sqlite3
import os



#db 초기화
def init_db_when_start():
    if os.path.isfile('login_info.txt'):
        os.remove('login_info.txt')
    if os.path.isfile("temp.db"):
        os.remove("temp.db")
    con = sqlite3.connect("temp.db")
    cur = con.cursor()

    # 테이블 추가할 때마다 여기에 넣어주기
    cur.execute('CREATE TABLE IF NOT EXISTS UserTable(id VARCHAR(30), UserName char(5), email char(25), password char(15))')
    cur.execute('CREATE TABLE IF NOT EXISTS UserGroup(groupId INTEGER PRIMARY KEY, groupName VARCHAR(30) unique, groupPw VARCHAR(15), masterName VARCHAR(30));')
    # cur.execute('CREATE TABLE IF NOT EXISTS Participation(groupId INTEGER, userId char(15), PRIMARY KEY(groupId, userId));')
    cur.execute('CREATE TABLE IF NOT EXISTS Participation (groupId INTEGER, userId char(15), PRIMARY KEY (groupId, userId), CONSTRAINT fk_group1 FOREIGN KEY (groupId) REFERENCES UserGroup(groupId) ON DELETE CASCADE);')
    cur.execute('CREATE TABLE IF NOT EXISTS Event (eventId INTEGER, eventName VARCHAR(30), groupId INTEGER, PRIMARY KEY (eventId), CONSTRAINT fk_group2 FOREIGN KEY (groupId) REFERENCES UserGroup(groupId) ON DELETE CASCADE);')

    if os.path.isfile('dump_script.sql'):
        f = open('dump_script.sql','r',encoding='utf-8')
        datas = f.readlines()
        for data in datas:
            if data.startswith('INSERT INTO'):
                cur.execute(data)
            # elif data.startswith('CREATE TABLE'):
            #     cur.execute(data)
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

    # with open("login_info.txt", "a", encoding="utf-8") as f:
    #     f.write("{}\n".format(groupId))
    #     f.close()

    with open('login_info.txt','r',encoding='utf-8') as f:
        datas= f.readlines()
        for data in datas:
            data.strip()
            if data.startswith('id'):
                login_id = data.split()[1]
            elif data.startswith('pw'):
                login_password = data.split()[1]
                break

    cur.execute("insert into UserGroup VALUES(?, ?, ?,?)", (groupId, groupName, groupPw,login_id))
    con.commit()
    # insertParticipation()
    with con:
        with open("dump_script.sql", 'w',encoding='utf-8') as f:
            for line in con.iterdump():
                f.write('%s\n' % line)

    con.close()
    insertParticipation(groupId)

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
    
    con.close()
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
    con.close()
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

def insertParticipation(groupId):
    con = sqlite3.connect("temp.db")
    cur = con.cursor()

    with open("login_info.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()    
        user_id = lines[0][4:].rstrip(" \n") 
        # groupId = lines[-1]
        # f.close()
    
    cur.execute("insert into Participation VALUES(?, ?)", (groupId, user_id))
    con.commit()
    with con:
        with open("dump_script.sql", 'w',encoding='utf-8') as f:
            for line in con.iterdump():
                f.write('%s\n' % line)
    con.close()

def find_user_group():  #로그인한 유저가 속해있는 그룹들을 리스트로 return해주는 함수
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

def find_group_members(groupName): #그룹의 멤버들을 리스트로 반환해주는 함수
    con = sqlite3.connect("temp.db")
    cur = con.cursor()
    sen = 'Select groupId From UserGroup WHERE groupName="{}"'.format(groupName)
    cur.execute(sen)
    group_id = cur.fetchone()[0]
    sen = 'Select userId From Participation WHERE groupId={}'.format(group_id)
    cur.execute(sen)
    group_members = cur.fetchall()
    group_member_list = []
    for group_member in group_members:
        gm = group_member[0]
        group_member_list.append(gm)
    con.close()
    return group_member_list

def get_all_groups(): #모든 그룹들을 리스트로 반환해주는 함수
    con = sqlite3.connect("temp.db")
    cur = con.cursor()
    sen = 'Select groupName From UserGroup'
    cur.execute(sen)
    all_groups_bfedit = cur.fetchall()
    all_group_list = []
    for i in all_groups_bfedit:
        all_group_list.append(i[0])
    con.close()
    return all_group_list

def join_group(groupName):  #그룹찾기에서 그룹 가입할 때 실행되는 함수
    con = sqlite3.connect("temp.db")
    cur = con.cursor()
    sen = 'Select groupId From UserGroup WHERE groupName="{}"'.format(groupName)
    cur.execute(sen)
    group_id = cur.fetchone()[0]
    con.close()
    insertParticipation(group_id)
    print("{}에 가입되었습니다.".format(groupName))


# -- Event
def getEventInfo():
    con = sqlite3.connect("temp.db")
    cur = con.cursor()
    sen = 'select eventName from Event'
    cur.execute(sen)

    event_list = cur.fetchall()
    con.close()
    return event_list

def getGroupId(groupName):
    con = sqlite3.connect("temp.db")
    cur = con.cursor()
    sen = 'SELECT groupId FROM UserGroup WHERE groupName="{}"'.format(groupName)
    cur.execute(sen)
    groupId = cur.fetchone()[0]
    print(groupId)
    return groupId
    cur.close()

def updateEvent(groupId, eventName):
    con = sqlite3.connect("temp.db")
    cur = con.cursor()

    cur.execute("select count(*) from Event")
    eventId = cur.fetchone()[0] + 1

    cur.execute("INSERT INTO Event VALUES(?, ?, ?);",(eventId, eventName, groupId))
    
    con.commit()   
    with con:
        with open("dump_script.sql", 'w',encoding='utf-8') as f:
            for line in con.iterdump():
                f.write('%s\n' % line)
    con.close()


def find_events(groupName):  #어떤 그룹의 이벤트리스트를 반환해주는 함수
    con = sqlite3.connect("temp.db")
    cur = con.cursor()
    sen = 'Select groupId From UserGroup WHERE groupName="{}"'.format(groupName)
    cur.execute(sen)
    group_id = cur.fetchone()[0]
    sen = 'Select eventName From Event WHERE groupId="{}"'.format(group_id)
    cur.execute(sen)
    event_names_bfedit = cur.fetchall()
    event_list = []
    for event in event_names_bfedit:
        event_list.append(event[0])
    con.close()
    return event_list

def find_groupPw(groupName):
    con = sqlite3.connect("temp.db")
    cur = con.cursor()
    sen = 'Select groupPw From UserGroup WHERE groupName="{}"'.format(groupName)
    cur.execute(sen)
    groupPw = cur.fetchone()
    groupPw = groupPw[0]
    con.close()
    return groupPw

# if __name__=='__main__':
#     con = sqlite3.connect("temp.db")
#     cur = con.cursor()
#     cur.execute('CREATE TABLE IF NOT EXISTS UserTable(id char(15), UserName char(5), email char(25), password char(15))')
#     cur.execute('CREATE TABLE IF NOT EXISTS UserGroup(groupId INTEGER PRIMARY KEY, groupName VARCHAR(30) unique, groupPw VARCHAR(15));')
#     cur.execute('CREATE TABLE IF NOT EXISTS Participation(groupId INTEGER, userId char(15), PRIMARY KEY(groupId, userId));')
#     con.commit()
#     con.close()

#     con = sqlite3.connect("temp.db")
#     cur = con.cursor()
#     cur.execute("SELECT * FROM UserTable")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
#     con.close()

# login_check('tina_id')
# delete('poo_id')

# print(find_group_members('tina_first_group'))
# find_events('tina_first_group')
# find_events('bb')
# find_groupPw('tina_first_group')