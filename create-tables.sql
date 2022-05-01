DROP TABLE IF EXISTS userInfo;
DROP TABLE IF EXISTS userInterest;
DROP TABLE IF EXISTS interests;
DROP TABLE IF EXISTS friendRequest;
DROP TABLE IF EXISTS friendsList;
CREATE TABLE IF NOT EXISTS userInfo(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    f_name VARCHAR(20) NOT NULL,
    l_name VARCHAR(20) NOT NULL,
    u_name VARCHAR(20) NOT NULL UNIQUE,
    age INTEGER NOT NULL,
    pw VARCHAR(40) NOT NULL,
    pronouns VARCHAR(45) NOT NULL,
    bio VARCHAR(100) NOT NULL,
    sm VARCHAR(30)
);
CREATE TABLE IF NOT EXISTS userInterest(
    user_id INTEGER,
    i1 INTEGER,
    i2 INTEGER,
    i3 INTEGER,
    i4 INTEGER,
    i5 INTEGER,
    CONSTRAINT FK_interestID FOREIGN KEY (user_id,i1,i2,i3,i4,i5)
    REFERENCES userInfo(id,id,id,id,id,id)
);

CREATE TABLE IF NOT EXISTS interests(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS friendRequest(
    userId INTEGER,
    otherId INTEGER,
    CONSTRAINT FK_requestID FOREIGN KEY (userId,otherId)
    REFERENCES userInfo(id,id)
);

CREATE TABLE IF NOT EXISTS friendsList(
    user_id INTEGER,
    f1 INTEGER,
    f2 INTEGER,
    f3 INTEGER,
    CONSTRAINT FK_friendID FOREIGN KEY (user_id,f1,f2,f3)
    REFERENCES userInfo(id,id,id,id)
);

INSERT INTO friendsList(user_id,f1,f2,f3) VALUES (1,2,3,4);

INSERT INTO interests(name) VALUES
('Literature'),
('Music'),
('Sports'),
('Foodies'),
('Meditating'),
('Hiking'),
('Games'),
('Art'),
('Plants'),
('Pets'),
('Knitting'),
('Cars'),
('Traveling'),
('Dance'),
('Productivity'),
('Fashion'),
('Home Decor'),
('Movies and TV shows'),
('Family'),
('Fitness');