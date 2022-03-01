BEGIN TRANSACTION;
CREATE TABLE Event(eventId INTEGER, eventName VARCHAR(30), groupId INTEGER, PRIMARY KEY(eventId));
CREATE TABLE Participation(groupId INTEGER, userId char(15), PRIMARY KEY(groupId, userId));
CREATE TABLE UserGroup(groupId INTEGER PRIMARY KEY, groupName VARCHAR(30) unique, groupPw VARCHAR(15), masterName VARCHAR(30));
CREATE TABLE UserTable(id VARCHAR(30), UserName char(5), email char(25), password char(15));
COMMIT;
