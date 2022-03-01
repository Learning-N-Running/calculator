BEGIN TRANSACTION;
CREATE TABLE Event(eventId INTEGER, eventName VARCHAR(30), groupId INTEGER, PRIMARY KEY(eventId));
INSERT INTO "Event" VALUES(1,'e1',1);
INSERT INTO "Event" VALUES(2,'e2',2);
INSERT INTO "Event" VALUES(3,'e3',2);
INSERT INTO "Event" VALUES(4,'e4',3);
INSERT INTO "Event" VALUES(5,'이벤트1',4);
INSERT INTO "Event" VALUES(6,'이벤트2',4);
CREATE TABLE Participation(groupId INTEGER, userId char(15), PRIMARY KEY(groupId, userId));
INSERT INTO "Participation" VALUES(1,'id1');
INSERT INTO "Participation" VALUES(2,'id2');
INSERT INTO "Participation" VALUES(3,'id3');
INSERT INTO "Participation" VALUES(2,'id4');
INSERT INTO "Participation" VALUES(4,'tina_id');
INSERT INTO "Participation" VALUES(1,'tina_id');
INSERT INTO "Participation" VALUES(5,'tina_id');
INSERT INTO "Participation" VALUES(2,'tina_id');
INSERT INTO "Participation" VALUES(1,'mk_id');
INSERT INTO "Participation" VALUES(3,'mk_id');
INSERT INTO "Participation" VALUES(5,'mk_id');
INSERT INTO "Participation" VALUES(4,'mk_id');
INSERT INTO "Participation" VALUES(1,'jh_id');
INSERT INTO "Participation" VALUES(4,'jh_id');
INSERT INTO "Participation" VALUES(5,'jh_id');
CREATE TABLE UserGroup(groupId INTEGER PRIMARY KEY, groupName VARCHAR(30) unique, groupPw VARCHAR(15), masterName VARCHAR(30));
INSERT INTO "UserGroup" VALUES(1,'aa','1234','id1');
INSERT INTO "UserGroup" VALUES(2,'bb','1234','id2');
INSERT INTO "UserGroup" VALUES(3,'cc','1234','id3');
INSERT INTO "UserGroup" VALUES(4,'tina_first_group','1234','tina_id');
INSERT INTO "UserGroup" VALUES(5,'tina_second_group','1234','tina_id');
CREATE TABLE UserTable(id VARCHAR(30), UserName char(5), email char(25), password char(15));
INSERT INTO "UserTable" VALUES('tina_id','tina_name','seungeun020309@gmail.com','tina_pw');
INSERT INTO "UserTable" VALUES('jh_id','jh_name','seungeun020309@gmail.com','jh_pw');
INSERT INTO "UserTable" VALUES('mk_id','mk_name','seungeun020309@gmail.com','mk_pw');
INSERT INTO "UserTable" VALUES('ddur_id','ddur_name','seungeun020309@gmail.com','ddur_pw');
INSERT INTO "UserTable" VALUES('id0221','id0221','dnwlals00@gmail.com','aa');
INSERT INTO "UserTable" VALUES('id1','11','aa@gmail.com','aa');
INSERT INTO "UserTable" VALUES('id2','22','bb@gmail.com','bb');
INSERT INTO "UserTable" VALUES('id3','33','cc@gmail.com','cc');
COMMIT;
