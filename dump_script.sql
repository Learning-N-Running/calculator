BEGIN TRANSACTION;
<<<<<<< HEAD
CREATE TABLE Event(eventId INTEGER, eventName VARCHAR(30), groupId INTEGER, PRIMARY KEY(eventId));
INSERT INTO "Event" VALUES(1,'e1',1);
INSERT INTO "Event" VALUES(2,'e2',1);
INSERT INTO "Event" VALUES(3,'e3',1);
INSERT INTO "Event" VALUES(4,'aaa',1);
INSERT INTO "Event" VALUES(5,'bbb',1);
INSERT INTO "Event" VALUES(6,'33',1);
INSERT INTO "Event" VALUES(7,'e3',1);
INSERT INTO "Event" VALUES(8,'e4',1);
INSERT INTO "Event" VALUES(9,'e5',1);
INSERT INTO "Event" VALUES(10,'e6',1);
INSERT INTO "Event" VALUES(11,'e7',1);
INSERT INTO "Event" VALUES(12,'e2',3);
INSERT INTO "Event" VALUES(13,'aaaaaa',2);
CREATE TABLE Participation(groupId INTEGER, userId char(15), PRIMARY KEY(groupId, userId));
INSERT INTO "Participation" VALUES(1,'id1');
INSERT INTO "Participation" VALUES(2,'id1');
INSERT INTO "Participation" VALUES(3,'tina_id');
INSERT INTO "Participation" VALUES(4,'id1');
CREATE TABLE UserGroup(groupId INTEGER PRIMARY KEY, groupName VARCHAR(30) unique, groupPw VARCHAR(15), masterName VARCHAR(30));
INSERT INTO "UserGroup" VALUES(1,'aaa','1234','id1');
INSERT INTO "UserGroup" VALUES(2,'bbb','123','id1');
INSERT INTO "UserGroup" VALUES(3,'g1','123','tina_id');
INSERT INTO "UserGroup" VALUES(4,'ccc','123','id1');
=======
CREATE TABLE Event (eventId INTEGER, eventName VARCHAR(30), groupId INTEGER, PRIMARY KEY (eventId), CONSTRAINT fk_group2 FOREIGN KEY (groupId) REFERENCES UserGroup(groupId) ON DELETE CASCADE);
CREATE TABLE Participation (groupId INTEGER, userId char(15), PRIMARY KEY (groupId, userId), CONSTRAINT fk_group1 FOREIGN KEY (groupId) REFERENCES UserGroup(groupId) ON DELETE CASCADE);
INSERT INTO "Participation" VALUES(1,'tina_id');
CREATE TABLE UserGroup(groupId INTEGER PRIMARY KEY, groupName VARCHAR(30) unique, groupPw VARCHAR(15), masterName VARCHAR(30));
INSERT INTO "UserGroup" VALUES(1,'tina_first_group','1234','tina_id');
>>>>>>> 7d3a3ee7e5477ca7088de4d6c028b0488711e88e
CREATE TABLE UserTable(id VARCHAR(30), UserName char(5), email char(25), password char(15));
INSERT INTO "UserTable" VALUES('tina_id','tina_name','seungeun020309@gmail.com','tina_pw');
COMMIT;
