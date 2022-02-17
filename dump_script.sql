BEGIN TRANSACTION;
CREATE TABLE UserTable(id char(15), UserName char(5), email char(25), password char(15));
INSERT INTO "UserTable" VALUES('tina','tina','tina','seungeun020309@gmail.com');
COMMIT;
