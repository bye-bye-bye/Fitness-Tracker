from Tkinter import *
import sqlite3
from random import *
con=sqlite3.Connection('quiz.db')
cur=con.cursor()
cur.execute("create table if not exists question(sno number(3),ques varchar(100),a varchar(3),b varchar(2),correct varchar(3))")
cur.execute("insert into question(sno,ques,a,b,correct) values(1,'Do you regularly workout?','Yes','No','Yes')")
cur.execute("insert into question(sno,ques,a,b,correct) values(2,'Do you eat junk food more than twice a week?','Yes','No','No')")
cur.execute("insert into question(sno,ques,a,b,correct) values(3,'Do you take regular check up of your body?','Yes','No','Yes')")
cur.execute("insert into question(sno,ques,a,b,correct) values(4,'Are you overweighted as compared to your age people?','Yes','No','No')")
cur.execute("insert into question(sno,ques,a,b,correct) values(5,'Do you start heavy breathing after running a short while?','Yes','No','No')")
cur.execute("insert into question(sno,ques,a,b,correct) values(6,'Do you skip meals?','Yes','No','No')")
cur.execute("insert into question(sno,ques,a,b,correct) values(7,'Are you obese?','Yes','No','No')")
cur.execute("insert into question(sno,ques,a,b,correct) values(8,'Do you consult a doctor after every 3 months for body checkup?','Yes','No','Yes')")
cur.execute("insert into question(sno,ques,a,b,correct) values(9,'Are you diabetic?','Yes','No','No')")
cur.execute("insert into question(sno,ques,a,b,correct) values(10,'Are you a patient of severe headache?','Yes','No','No')")
cur.execute("select * from question")
print cur.fetchall()
con.commit()





