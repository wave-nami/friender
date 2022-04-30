CREATE TABLE IF NOT EXISTS userInfo(
    id int IDENTITY(1,1) PRIMARY KEY,
    f_name VARCHAR(20) NOT NULL,
    l_name VARCHAR(20) NOT NULL,
    u_name VARCHAR(20) NOT NULL,
    age int NOT NULL,
    pw VARCHAR(40) NOT NULL,
    gender VARCHAR(45) NOT NULL,
    bio VARCHAR(100) NOT NULL,
    sm VARCHAR(30)
);
CREATE TABLE IF NOT EXISTS userInterest(
    user_id int,
    i1 int,
    i2 int,
    i3 int,
    i4 int,
    i5 int,
    CONSTRAINT FK_interestID FOREIGN KEY (user_id,i1,i2,i3,i4,i5)
    REFERENCES userInfo(id,id,id,id,id,id)
);

CREATE TABLE IF NOT EXISTS interests(
    id int IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS friendRequest(
    user_id int,
    r1 int,
    r2 int,
    r3 int,
    r4 int,
    r5 int,
    CONSTRAINT FK_requestID FOREIGN KEY (user_id,r1,r2,r3,r4,r5)
    REFERENCES userInfo(id,id,id,id,id,id)
);

CREATE TABLE IF NOT EXISTS friendsList(
    user_id int,
    f1 int,
    f2 int,
    f3 int,
    CONSTRAINT FK_friendID FOREIGN KEY (user_id,f1,f2,f3)
    REFERENCES userInfo(id,id,id,id)
);