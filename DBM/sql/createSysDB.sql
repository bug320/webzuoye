CREATE TABLE SYS(
    loopSize CHAR(2),
    lengthSize CHAR(2),
    PRIMARY KEY(loopSize,lengthSize)
);

#CONSTRAINT pk_PersonID PRIMARY KEY (P_Id,LastName)

INSERT INTO SYS(loopSize,lengthSize) VALUES ("7","4");

