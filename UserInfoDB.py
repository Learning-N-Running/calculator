import sqlite3

#지우면 안됨.
# cur.execute('CREATE TABLE UserTable(id char(15), UserName char(5), email char(25), password char(15))')
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

if __name__=='__main__':
    con = sqlite3.connect("temp.db")
    cur = con.cursor()
    # cur.execute('CREATE TABLE UserTable(id char(15), UserName char(5), email char(25), password char(15))')
    cur.execute("SELECT * FROM UserTable")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    con.close()
