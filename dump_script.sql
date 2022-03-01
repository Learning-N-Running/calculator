BEGIN TRANSACTION;
CREATE TABLE Event (eventId INTEGER, eventName VARCHAR(30), groupId INTEGER, PRIMARY KEY (eventId), CONSTRAINT fk_group2 FOREIGN KEY (groupId) REFERENCES UserGroup(groupId) ON DELETE CASCADE);
CREATE TABLE Participation (groupId INTEGER, userId char(15), PRIMARY KEY (groupId, userId), CONSTRAINT fk_group1 FOREIGN KEY (groupId) REFERENCES UserGroup(groupId) ON DELETE CASCADE);
INSERT INTO "Participation" VALUES(1,'tina_id');
CREATE TABLE UserGroup(groupId INTEGER PRIMARY KEY, groupName VARCHAR(30) unique, groupPw VARCHAR(15), masterName VARCHAR(30));
INSERT INTO "UserGroup" VALUES(1,'tina_first_group','1234','tina_id');
CREATE TABLE UserTable(id VARCHAR(30), UserName char(5), email char(25), password char(15));
INSERT INTO "UserTable" VALUES('tina_id','tina_name','seungeun020309@gmail.com','tina_pw');
COMMIT;
