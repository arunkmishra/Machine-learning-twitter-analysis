import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE if not exists dost
       (username CHAR(20) PRIMARY KEY     NOT NULL,
       name           TEXT    NOT NULL,
       age           INT     NOT NULL,
       password        CHAR(50),
       dob         DATE);''')
print "Table created successfully";

#conn.execute("insert into dost(username,name,age,password,dob) values ('arun','arun',21,'pass',1995-07-13)");

conn.commit()

cursor = conn.execute("SELECT username, name, age, password , dob  from dost")
for row in cursor:
   print "Username = ", row[0]
   print "NAME = ", row[1]
   print "Age = ", row[2]
   print "Password = ", row[3]
   print "dob = ", row[4],"\n"

conn.close()
