BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS uksongs (
	songid	BIGINT(255) NOT NULL AUTO_INCREMENT UNIQUE,
	songname	VARCHAR(255) NOT NULL,
	artistname VARCHAR(255) NOT NULL,
	PRIMARY KEY (songid)
);
INSERT INTO "uksongs" ("songid","songname","artistname") VALUES (1,'Tipsy','J-Kwon'),
 (2,'Tipsy','J-Kwon'),
 (3,'Tipsy','J-Kwon');
COMMIT;
