BEGIN TRANSACTION;
CREATE TABLE UserTable(id char(15), UserName char(5), email char(25), password char(15));
INSERT INTO "UserTable" VALUES('tina_id','tina_name','seungeun020309@gmail.com','tina_pw');
INSERT INTO "UserTable" VALUES('jh_id','jh_name','seungeun020309@gmail.com','jh_pw');
INSERT INTO "UserTable" VALUES('mk_id','mk_name','seungeun020309@gmail.com','mk_pw');
INSERT INTO "UserTable" VALUES('ddur_id','ddur_name','seungeun020309@gmail.com','ddur_pw');
INSERT INTO "UserTable" VALUES('id0221','id0221','dnwlals00@gmail.com','aa');
CREATE TABLE UserGroup(groupId INTEGER PRIMARY KEY, groupName TEXT, groupSite CHAR(25), groupPw VARCHAR(15));

COMMIT;
