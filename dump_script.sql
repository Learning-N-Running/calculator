BEGIN TRANSACTION;
CREATE TABLE Participation(groupId INTEGER, 
                            id char(15), 
                            PRIMARY KEY(groupId, id),
                            FOREIGN KEY(groupId) REFERENCES'UserGroup'('groupId'), 
                            FOREIGN KEY(id) REFERENCES'UserTable'('id'));
CREATE TABLE UserGroup(groupId INTEGER PRIMARY KEY, groupName VARCHAR(30) unique, groupPw VARCHAR(15));
INSERT INTO "UserGroup" VALUES(1,'a','123');
INSERT INTO "UserGroup" VALUES(2,'b','123');
CREATE TABLE UserTable(id char(15), UserName char(5), email char(25), password char(15));
INSERT INTO "UserTable" VALUES('tina_id','tina_name','seungeun020309@gmail.com','tina_pw');
INSERT INTO "UserTable" VALUES('jh_id','jh_name','seungeun020309@gmail.com','jh_pw');
INSERT INTO "UserTable" VALUES('mk_id','mk_name','seungeun020309@gmail.com','mk_pw');
INSERT INTO "UserTable" VALUES('ddur_id','ddur_name','seungeun020309@gmail.com','ddur_pw');
INSERT INTO "UserTable" VALUES('id0221','id0221','dnwlals00@gmail.com','aa');
INSERT INTO "UserTable" VALUES('id1','11','aa@gmail.com','aa');
INSERT INTO "UserTable" VALUES('id2','22','bb@gmail.com','bb');




COMMIT;
