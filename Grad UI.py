
# Application Libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfile 
import tkinter as tk
import time

# for DB connection
import ast
import sqlite3
import sys
import subprocess

# Application tools pipeline
import Name_Matching as NM
import Regional_Analysis as RA
import Name_Generator as NG
import Adverse_Media as AM

# blue color -> #4f94d4
# gray color for backgrounds -> #101517


root=Tk()
root.title('Sign in')
root.geometry('925x500+300+200')
root.configure(bg='#101517')
root.resizable(False, False)

frame=Frame(root,width=925,height=500,bg='#101517')
frame.place(x=0,y=0)

heading = Label(frame,text='Sign in',fg='#4f94d4',bg='#101517',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(relx=0.5,rely=0.2,anchor='center')

#DB connection
conn = sqlite3.connect('mydatabase.db', timeout=1)
cursor = conn.cursor()
def restart():
        root.destroy()
        python = sys.executable
        cmd = [python] + sys.argv
        subprocess.call(cmd)
def admins():
    #DB connection
    cursor.execute("CREATE TABLE IF NOT EXISTS CREDENTIALS(username varchar(200) NOT NULL, password NOT NULL);") #here put the credentials u want from every user

    cursor.execute("""
    INSERT OR REPLACE INTO CREDENTIALS( username, password)
    VALUES (?,?)
    """, ( str(user.get()), str(user2.get()))) #here enter the names of the variables that contain these credentials
    cursor.execute('''SELECT * from CREDENTIALS''')
    result = cursor.fetchall()
    print(result)
    conn.commit ()

    # login using admin account
    username=user.get()
    password=user2.get()
    if username=='admin' and password=='123456':
        screen=root
        screen.title("app")
        screen.geometry('925x500+300+200')
        screen.configure(bg='#101517')


        frame=Frame(screen,width=925,height=500, bg='#101517')
        frame.place(x=0,y=0)
        heading= Label(frame,text='Welcome back, Admin',fg='#57a1f8',bg='#101517',font=('Microsoft YaHei UI Light',30,'bold'))
        heading.place(relx=0.5,rely=0.5)

        label=Label(frame,text='you can input a .csv file containing different names to be matched and scored',fg='#57a1f8',bg='#101517',font=('Microsoft YaHei UI Light',9))
        label.place(x=345,y=200)

        label2=Label(frame,text='or you can choose to enter a single name to get matched:',fg='#57a1f8',bg='#101517',font=('Microsoft YaHei UI Light',9))
        label2.place(x=400,y=235)
            
        def settingpg(): #settings page
            frame=Frame(screen,width=775,height=500,bg='#101517')
            frame.place(x=150,y=0) 
            screen.geometry('925x500+300+200')
            screen.configure(bg='#101517')
            screen.title('Setting Page')
            heading= Label(frame,text='Setting',fg='#57a1f8',bg='#101517',font=('Microsoft YaHei UI Light',23,'bold'))
            heading.place(relx=0.5,rely=0.2,anchor='center')

            def on_enter(e):
                user.delete(0,'end')

            def on_leave(e):
                name=user.get()
                if name=='':
                    user.insert(0,'Email')

            user=Entry(frame,width=25,fg='#57a1f8',border=0,bg='#101517',font=('Microsoft YaHei UI Light',11))
            user.place(x=240,y=160)
            user.insert(0,'Email')
            user.bind('<FocusIn>', on_enter)
            user.bind('<FocusOut>', on_leave)
            Frame(frame,width=295,height=2,bg='#4f94d4').place(x=235,y=187)

            def on_enter2(e):
                user2.delete(0,'end')

            def on_leave2(e):
                name=user2.get()
                if name=='':
                    user2.insert(0,'Username')

            user2=Entry(frame,width=25,fg='#57a1f8',border=0,bg='#101517',font=('Microsoft YaHei UI Light',11))
            user2.place(x=240,y=230)
            user2.insert(0,'Username')
            user2.bind('<FocusIn>', on_enter2)
            user2.bind('<FocusOut>', on_leave2)
            Frame(frame,width=295,height=2,bg='#4f94d4').place(x=235,y=257)



            Button(frame,width=15,pady=7,text='Logout',bg='#57a1f8',fg='#101517',border=0,command=restart).place(x=420,y=350)

            Button(frame,width=15,pady=7,text='Reset Password',bg='#57a1f8',fg='#101517',border=0,command=NMF).place(x=235,y=350)

        def homepg():
            frame=Frame(screen,width=775,height=500,bg='#101517')
            frame.place(x=150,y=0)  
            heading= Label(frame,text='Welcome back, Admin',fg='#57a1f8',bg='#101517',font=('Microsoft YaHei UI Light',30,'bold'))
            heading.place(relx=0.5,rely=0.3,anchor='center')
            
            s = ttk.Style()
            s.theme_use('clam')
            s.configure("#4f94d4.Horizontal.TProgressbar", fg='#4f94d4', bg='#4f94d4')
            
            def open_file():
                file_path = askopenfile(mode='r', filetypes=[('CSV Files', '*csv')])
                if file_path is None:
                    # Label(frame, text='No File Uploaded', fg='white',bg='#101517').place(relx=0.5,y=240,anchor='center')
                    pass
                else:
                    uploadFiles()
            def uploadFiles():

                bar = ttk.Progressbar(
                    frame, 
                    style="#4f94d4.Horizontal.TProgressbar",
                    orient=HORIZONTAL, 
                    length=300, 
                    mode='determinate',
                    )
                bar.place(relx=0.5,y=200,anchor='center')
                for i in range(5):
                    frame.update_idletasks()
                    bar['value'] += 30
                    time.sleep(1)
                bar.destroy()
                Label(frame, text='File Uploaded!', fg='white',bg='#101517').place(relx=0.5,y=240,anchor='center')

            tk.Button(frame, text='enter a list', width=20, height=5, bg='#4f94d4',command=open_file).place(x=450,y=270)

            tk.Button(frame, text='enter a name', width=20, height=5, bg='#4f94d4',command=NMF).place(x=180,y=270)

        def NMF():
            NM.main(screen)

        
        def RAF():
            RA.main(screen)

      
        def NGF():
            NG.main(screen)

        def AMF():
            AM.main(screen)
 
        homepg()

        menu_frame = tk.Frame(frame, width=200, bg="#57a1f8")
        menu_frame.pack(side="left", fill="y")

        menu_options = ["Home", "Name Matching", "Regional Analysis", "Name Generator", "Adverse Media",'Settings']

        for option in menu_options:
            if option == 'Home':
                tk.Button(menu_frame, text=option, width=20, height=5, bg='#4f94d4',command=homepg).pack()
            elif option == 'Name Matching':
                tk.Button(menu_frame, text=option, width=20, height=5, bg='#4f94d4',command=NMF).pack()
            elif option == 'Regional Analysis':
                tk.Button(menu_frame, text=option, width=20, height=5, bg='#4f94d4',command=RAF).pack()
            elif option == 'Name Generator':
                tk.Button(menu_frame, text=option, width=20, height=5, bg='#4f94d4',command=NGF).pack()
            elif option == 'Adverse Media':
                tk.Button(menu_frame, text=option, width=20, height=5, bg='#4f94d4',command=AMF).pack()
            elif option == 'Settings':
                tk.Button(menu_frame, text=option, width=20, height=5, bg='#4f94d4',command=settingpg).pack()
        
        screen.mainloop()
    elif username!='admin' or password!='123456':
        messagebox.showerror('Error','Invalid Username or Password')

def signuppg():
    pg = Tk()
    pg.title('Sign up')
    pg.geometry('925x500+300+200')
    pg.configure(bg='#101517')
    pg.resizable(False,False)

    frame= Frame(pg,width=925,height=500,bg='#101517')
    frame.place(x=0,y=0)


    heading = Label(frame,text='Sign up',fg='#4f94d4',bg='#101517',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(relx=0.5,rely=0.1,anchor='center')
    
    # Email
    def E_enter(e):
        userE.delete(0,'end')

    def E_leave(e):
        name=userE.get()
        if name=='':
            userE.insert(0,'Email')

    userE=Entry(frame,width=30,fg='#57a1f8',border=0,bg='#101517',font=('Microsoft YaHei UI Light',11))
    userE.place(relx=0.48,rely=0.27,anchor='center')
    userE.insert(0,'Email')
    userE.bind('<FocusIn>', E_enter)
    userE.bind('<FocusOut>', E_leave)
    Frame(frame,width=290,height=2,bg='#4f94d4').place(relx=0.34,rely=0.3)

    # username
    def on_enter(e):
        user.delete(0,'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')

    user=Entry(frame,width=25,fg='#57a1f8',border=0,bg='#101517',font=('Microsoft YaHei UI Light',11))
    user.place(relx=0.458,rely=0.4,anchor='center')
    user.insert(0,'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)
    Frame(frame,width=290,height=2,bg='#4f94d4').place(relx=0.34,rely=0.43)

    # Password
    def on_enter2(e):
        user2.delete(0,'end')

    def on_leave2(e):
        name=user2.get()
        if name=='':
            user2.insert(0,'Password')

    user2=Entry(frame,width=25,fg='#57a1f8',border=0,bg='#101517',font=('Microsoft YaHei UI Light',11))
    user2.place(relx=0.458,rely=0.53,anchor='center')
    user2.insert(0,'Password')
    user2.bind('<FocusIn>', on_enter2)
    user2.bind('<FocusOut>', on_leave2)
    Frame(frame,width=290,height=2,bg='#4f94d4').place(relx=0.34,rely=0.56)
    
    # confirm password
    def on_enter3(e):
        user3.delete(0,'end')

    def on_leave3(e):
        name=user3.get()
        if name=='':
            user3.insert(0,'Confirm Password')

    user3=Entry(frame,width=25,fg='#57a1f8',border=0,bg='#101517',font=('Microsoft YaHei UI Light',11))
    user3.place(relx=0.458,rely=0.66,anchor='center')
    user3.insert(0,'Confirm Password')
    user3.bind('<FocusIn>', on_enter3)
    user3.bind('<FocusOut>', on_leave3)
    Frame(frame,width=290,height=2,bg='#4f94d4').place(relx=0.34,rely=0.69)

    def cred():
        email=userE.get()
        username=user.get()
        password=user2.get()
        confirm=user3.get()

        if password==confirm:
            try:
                file=open('datasheet.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={email:[username,password]}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open('datasheet.txt','w')
                w=file.write(str(r))
                messagebox.showinfo('Sign', 'Successfully Signed up!')
            except:
                file=open('datasheet.txt','w')
                pp=str({'Email':['Username','password']})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('Invalid','Passwords dont match!')

    #DB connection
    conn = sqlite3.connect('mydatabase.db', timeout=1)
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS CREDENTIALS(email TEXT PRIMARY KEY, username TEXT NOT NULL, password NOT NULL);") #here put the credentials u want from every user

    cursor.execute("""
        INSERT OR REPLACE INTO CREDENTIALS(email, username, password)
        VALUES (?,?,?)
        """, (str(userE.get()), str(user.get), str(user2.get()))) #here enter the names of the variables that contain these credentials
    cursor.execute('''SELECT * from CREDENTIALS''')
    result = cursor.fetchall()
    print(result)
    conn.commit ()
    Button(frame,width=45,pady=7,text='Sign up',bg='#57a1f8',fg='#101517',border=0,command=cred).place(relx=0.5,rely=0.8,anchor='center')
    

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

# this is the user variable for the login page
user=Entry(frame,width=25,fg='#57a1f8',border=0,bg='#101517',font=('Microsoft YaHei UI Light',11))
user.place(relx=0.458,rely=0.4,anchor='center')
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame,width=290,height=2,bg='#4f94d4').place(relx=0.34,rely=0.43)

def on_enter2(e):
    user2.delete(0,'end')

def on_leave2(e):

    name=user2.get()
    if name=='':
        user2.insert(0,'Password')

user2=Entry(frame,width=25,fg='#57a1f8',border=0,bg='#101517',font=('Microsoft YaHei UI Light',11))
user2.pack(fill='x',expand=True)
user2.place(relx=0.458,rely=0.53,anchor='center')
user2.insert(0,'Password')
user2.bind('<FocusIn>', on_enter2)
user2.bind('<FocusOut>', on_leave2)

def toggle_password_visibility():
    global show_password
    show_password = not show_password
    if show_password:
        user2.config(show="")
        eye_button.itemconfig(pupil, fill="gray")
    else:
        user2.config(show="*")
        eye_button.itemconfig(pupil, fill="black")

eye_button = Canvas(root, width=30, height=20,bg='#101517',highlightthickness=0)
eye_button.pack()
eye_button.place(relx=0.66,rely=0.53,anchor='w')
# Draw the white background of the eye
eye_button.create_oval(3, 3, 27, 13, fill="black", outline="#4f94d4", width=2)
# Draw the black pupil of the eye
pupil = eye_button.create_oval(9, 4.5, 21, 12, fill="#4f94d4", outline="#4f94d4", width=2)
# Bind the eye button to toggle the password visibility
eye_button.bind("<Button-1>", lambda event: toggle_password_visibility())
show_password = False

Frame(frame,width=290,height=2,bg='#4f94d4').place(relx=0.34,rely=0.56)

Button(frame,width=45,pady=7,text='Sign in',bg='#57a1f8',fg='#101517',border=0,command=admins).place(relx=0.5,rely=0.7,anchor='center')
label= Label(frame,text="Don't have an account?",fg='#57a1f8',bg='#101517',font=('Microsoft YaHei UI Light',9))
label.place(relx=0.465,rely=0.8,anchor='center')

signup =Button(frame, width=6, text='Sign up',border=0,fg='#4f94d4',bg='#101517',cursor='hand2',command=signuppg)
signup.place(relx=0.58,rely=0.8,anchor='center')


root.mainloop()
conn.close()