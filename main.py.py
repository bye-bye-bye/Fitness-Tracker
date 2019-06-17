from Tkinter import *
import sqlite3
from tkMessageBox import *
from random import *
conn = sqlite3.connect('quiz.db')
cur = conn.cursor()
cur.execute("create table if not exists man(name varchar(10),username varchar(20),password varchar(20))")
root=Tk()
root.title("Student Details")
root.resizable(0,0)
root.configure(bg='magenta')
Label(root,text="Name: Manika Sharma",font="Times 20 bold",bg='powderblue',fg='brown').grid(row=2,column=0,sticky=N,ipadx=50,ipady=10)
Label(root,text="Enroll. no.: 171B062",font="Times 20 bold",bg='powderblue',fg='brown').grid(row=4,column=0,sticky=N,ipadx=50,ipady=10)
Label(root,text="Batch : B2 (BX)",font="Times 20 bold",bg='powderblue',fg='brown').grid(row=6,column=0,sticky=N,ipadx=50,ipady=10)
Label(root,text="Email ID : shivi007800@gmail.com",font="Times 20 bold",bg='powderblue',fg='brown').grid(row=8,column=0,sticky=N,ipadx=50,ipady=10)
lb=Label(root,text="Project: Fitness Tracker",font="Times 20 bold",bg='powderblue',fg='brown')
lb.grid(row=10,column=0,sticky=N,ipadx=50,ipady=10)


global un, pas, dis  # declaring username and password variable as global
a = [0] * 51 #declaring a list of size 51 will all 0's
global score
score=0
global x  #generating random number
global c
v2=IntVar()
c=0 #counter variable to display in
#A persons score is initially zero

def func():
    root.destroy()
    logi()

def finish():
    global score
    global c
    global fin
    dis.destroy()
    fin=Toplevel()
    fin.title('FINAL SCORE')
    fin.resizable(0,0)
    fin.configure(bg='red')
    Label(fin,text='Quiz finished because you sumbitted all questions or pressed FINISH',font='Times 16 bold',relief='ridge',bg='blue',fg='white').grid(row=0,column=0)
    Label(fin,text='You attemped '+str(c)+' Questions',font='times 16 italic',relief='raised',bg='lightblue',fg='black',bd=5).grid(row=1,column=0,columnspan=16)
    Label(fin,text='Your Score = '+str(score),font='times 16 italic underline',relief='raised',bg='lightblue',fg='black',bd=5).grid(row=2,column=0,columnspan=16)
    Button(fin,text='CHECK FITNESS',font='bold',bg='yellow',bd=5,activeforeground='white',activebackground='black', command=lambda:final()).grid(row=4,column=0)
    
def final():
    global f
    fin.destroy()
    f=Toplevel()
    f.configure(bg='black')
    Label(f,text='If you scored more than 7 then your health is good',font='times 16 bold',bg='cyan',fg='black').pack()
    Label(f,text='and you are keeping a good track of your fitness',font='times 16 bold',bg='cyan',fg='black').pack()
    Label(f,text='and keep this thing going but if your score is',font='times 16 bold',bg='cyan',fg='black').pack()
    Label(f,text='less than 7 its high time for you to start',font='times 16 bold',bg='cyan',fg='black').pack()
    Label(f,text='thinking about your health',font='times 16 bold',bg='cyan',fg='black').pack()
    Label(f,text='HEALTH TIPS',font='arial 17 bold underline',bg='white',fg='black').pack()
    Label(f,text='SELECT GENDER',font='arial 17 italic underline',bg='black',fg='white').pack()
    Button(f,text='Female',font='bold',bg='black',fg='white',bd=5,command=lambda:female()).pack()
    Button(f,text='Male',font='bold',bg='black',fg='white',bd=5,command=lambda:male()).pack()

def female():
    f.destroy()
    fe=Toplevel()
    fe.title('FEMALE')
    fe.configure(bg='turquoise')
    Label(fe,text='1. DRINK AS 8 GLASSES OF WATER DAILY',font='times 12 bold').pack()
    Label(fe,text='2. MEDITATE DAILY',font='times 12 bold').pack()
    Label(fe,text='3. AVOID EATING OILY AND JUNK FOOD DAILY',font='times 12 bold').pack()
    Label(fe,text='4. MAKE SURE YOUR FOOD IS RICH IN IRON AND CALCIUM',font='times 12 bold').pack()
    Label(fe,text='5. BRISK WALK DAILY FOR 15 MINS ATLEAST',font='times 12 bold').pack()
    

def male():
    f.destroy()
    ma=Toplevel()
    ma.title('MALE')
    ma.configure(bg='turquoise')
    Label(ma,text='1.MEDITATE DAILY',font='times 12 bold').pack()
    Label(ma,text='2.DONT TAKE MUCH STRESS',font='times 12 bold').pack()
    Label(ma,text='3.GO FOR CHECKUPS REGULARLY',font='times 12 bold').pack()
    Label(ma,text='4.AVOID OILY AND JUNK FOOD',font='times 12 bold').pack()
    Label(ma,text='5.INCLUDE CARBOHYDRATES ,IRON AND CALCIUM IN YOUR FOOD',font='times 12 bold').pack()

def disques():
    #login.destroy()
    global x, dis,timeLabel,flag
    v2=IntVar()
    dis = Toplevel()
    dis.title("QUESTIONS")
    dis.geometry('+0+300')
    dis.resizable(0, 0)
    dis.configure(background='#00ccff')
    cur.execute('SELECT ques FROM question WHERE sno==(?)', (x,))
    question = str(cur.fetchone()[0])
    Label(dis, text=question, font='times 20 bold', relief='ridge',bg='#66ff33').grid(row=0, columnspan=6)
    cur.execute('SELECT a FROM question WHERE sno==(?)', (x,))
    opa = str(cur.fetchone()[0])
    r1 = Radiobutton(dis, text=opa, variable=v2, value=1,bg='#00ccff')
    r1.grid(row=1, column=0,sticky=W)
    cur.execute('SELECT b FROM question WHERE sno==(?)', (x,))
    opb = str(cur.fetchone()[0])
    r2 = Radiobutton(dis, text=opb, variable=v2, value=2,bg='#00ccff')
    r2.grid(row=2, column=0,sticky=W)
    cur.execute('SELECT correct FROM question WHERE sno==(?)', (x,))
    ans = str(cur.fetchone()[0])
    b1 = Button(dis, text='Sumbit',bg='powder blue',bd=5,activeforeground='blue',activebackground='red', command=lambda: dandq(ans,v2.get()))
    #b1 = Button(dis, text='Sumbit',bg='powder blue',bd=5,activeforeground='blue',activebackground='red', command=abc)
    b1.grid(row=5, column=1)
    exi = Button(dis, text='FINISH',bg='powder blue',bd=5,activeforeground='blue',activebackground='red', command=lambda: finish())
    exi.grid(row=5, column=5)
    dis.mainloop()


def dandq(ans,opt):
    global score
    global v2
    tt={1:'Yes',2:'No'}
    #print 'answer retrieved from db',ans,opt
    if tt[opt] == ans:     #if answer matches from database increase score
        score = score + 1
        #showinfo('Information','HEALTHY +1')
    elif v2.get()!=ans:     #if answer doesn't match then show error
        #showerror('Error','UNHEALTHY ANSWER')
        score=score+0

    dis.destroy()
    ques()

def ques():
    global x
    global c
    global user
    global sc
    #login.destroy()
    if c<10: #counter variable to check if not more than 10 ques are displayed
        x = randint(1, 10)    #calling random function to genrate a random number
        if a[x] == 0:   #a list for checking if the question has been displayed before or not
            a[x] = 1
            c = c + 1
            disques()
        else:   #if displayed then again calling this function
            ques()
    else:
        finish()


def insertdata():
    global nun, npas, nam, signup
    cur.execute("INSERT INTO man (name,username,password)  VALUES (?,?,?)", (nam.get(), nun.get(), npas.get(),))
    conn.commit()
    signup.destroy()
    



def enter():
    global un, pas, login
    
    cur.execute('select username from man where username=? AND  password=?', (un.get(), pas.get()))
    data = cur.fetchall()
    
    if not data:  # condition to check if data is found in database and if not found displaying correct error and also asking user for new input
        pas.delete(0, END)
        un.delete(0, END)
        un.focus_set()
        showerror('Error', 'Data Not Found,If New User Please Signup')
    else:  # if found then proceeding to quiz
        showinfo('Hello','WELCOME TO THE FITNESS QUIZ')
        ques()
        login.destroy()
    


def newuser():
    global nun, npas, nam, signup
    signup = Tk()
    signup.title('NEW USER')
    signup.resizable(0,0)
    Label(signup, text='Enter the details', font='times 30 bold').grid(row=0, columnspan=5)
    Label(signup, text='Name').grid(row=1, column=0)
    nam = Entry(signup, width=25,bd=5)
    nam.grid(row=1, column=2)
    Label(signup, text='Username').grid(row=2, column=0)
    nun = Entry(signup, width=25,bd=5)  # username input
    nun.grid(row=2, column=2)
    Label(signup, text='Password').grid(row=3, column=0)
    npas = Entry(signup, width=25, show='*',bd=5)  # password input
    npas.grid(row=3, column=2)
    s = Button(signup, text='Submit', bg='cyan',bd=5,command=lambda: insertdata())
    s.grid(row=4,column=2)


def logi():
    global un, pas, login
    login = Tk()
    login.title('Quiz Portal')
    login.resizable(0,0)
    login.geometry("600x500")
    login.configure(bg='orchid')
    Label(login, text='FITNESS ASSESSMENT', font='times 40 bold',bg='blue',bd=5).place(x=0,y=0)
    Label(login, text='Username',font='times 15 bold',bg='blue').place(x=150,y=200,width=100)
    un = Entry(login, width=25,font='times 10 bold',bd=5)  # username input
    un.place(x=260,y=200,height=25)
    Label(login, text='Password',font='times 15 bold',bg='blue').place(x=150,y=275,width=100)
    pas = Entry(login, width=25,show='*',bd=5)  # password input
    pas.place(x=260,y=275,height=25)
    b1 = Button(login, text='Login',bg='#6699ff',bd=5,activeforeground='blue',activebackground='black', command=enter)
    b1.place(x=200,y=320)
    b2 = Button(login, text='New User',bg='#6699ff',bd=5,activeforeground='blue',activebackground='black', command=newuser)
    b2.place(x=300,y=320)
#logi()
lb.after(4000,func)
root.mainloop()
