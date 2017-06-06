CREATE TABLE User(
    id       CHAR(10),
    name     CHAR(10),
    passed   CHAR(10),
    best     CHAR(10),
    reportId CHAR(10)
);

INSERT INTO User(id,name,passed,best,reportId) values("0","root","root","-1","-1");

INSERT INTO User(id,name,passed,best,reportId) values("1","User","User","0","0");

