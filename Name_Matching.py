
# application libraries
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import *
import pandas as pd
import numpy as np

# Importing the models Pipelines
import LSTM_API as lstm

def RA_connect(name):

    def capitalize_name(name_cap):
        name_parts = name_cap.split()
        capitalized_parts = [part.capitalize() for part in name_parts]
        capitalized_name = ' '.join(capitalized_parts)


        return capitalized_name
    
    l = lstm.API_RNN()
    df = [name]
    rst1 = l.call(pd.DataFrame(np.array(df)))
    # rst = capitalize_name(rst1)
    return rst1[0]

def main(screen):
    
    def name_matching():
                frame=Frame(screen,width=775,height=500,bg='#101517')
                frame.place(x=150,y=0) 
                screen.geometry('925x500+300+200')
                screen.configure(bg='#101517')
                screen.title('Name Matching Page')
                heading= Label(frame,text='Name Matching',fg='#57a1f8',bg='#101517',font=('Microsoft YaHei UI Light',23,'bold'))
                heading.place(relx=0.5,rely=0.2,anchor='center')

                def on_enter(e):
                    user.delete(0,'end')

                def on_leave(e):
                    name=user.get()
                    if name=='':
                        user.insert(0,'First Name*')

                user=Entry(frame,width=25,fg='#57a1f8',border=0,bg='#101517',font=('Microsoft YaHei UI Light',11))
                user.place(x=240,y=160)
                user.insert(0,'First Name*')
                user.bind('<FocusIn>', on_enter)
                user.bind('<FocusOut>', on_leave)
                Frame(frame,width=295,height=2,bg='#4f94d4').place(x=235,y=187)

                def on_enter2(e):
                    user2.delete(0,'end')

                def on_leave2(e):
                    name=user2.get()
                    if name=='':
                        user2.insert(0,'Last Name*')

                user2=Entry(frame,width=25,fg='#57a1f8',border=0,bg='#101517',font=('Microsoft YaHei UI Light',11))
                user2.place(x=240,y=230)
                user2.insert(0,'Last Name*')
                user2.bind('<FocusIn>', on_enter2)
                user2.bind('<FocusOut>', on_leave2)
                Frame(frame,width=295,height=2,bg='#4f94d4').place(x=235,y=257)

                def on_enter3(e):
                    user3.delete(0,'end')

                def on_leave3(e):
                    name=user3.get()
                    if name=='':
                        user3.insert(0,'Middle Name')

                user3=Entry(frame,width=25,fg='#57a1f8',border=0,bg='#101517',font=('Microsoft YaHei UI Light',11))
                user3.place(x=240,y=300)
                user3.insert(0,'Middle Name')
                user3.bind('<FocusIn>', on_enter3)
                user3.bind('<FocusOut>', on_leave3)
                Frame(frame,width=295,height=2,bg='#4f94d4').place(x=235,y=327)
                
                # this is a function used to make sure that the first letter of each name is capitalize
                def capitalize_name(name):
                    name_parts = name.split()
                    capitalized_parts = [part.capitalize() for part in name_parts]
                    capitalized_name = ' '.join(capitalized_parts)

                    return capitalized_name
                
                # results page for the name matching tool
                def rslt_NM():
                    frame2=Frame(screen,width=775,height=500,bg='#101517')
                    frame2.place(x=150,y=0)  
                    screen.geometry('925x500+300+200')
                    screen.configure(bg='#101517')
                    screen.title('Name Matching Results')
                    heading= Label(frame2,text='Name Matching Results',fg='#57a1f8',bg='#101517',font=('Microsoft YaHei UI Light',10,'bold'))
                    heading.place(relx=0.4,rely=0)

                    # Connecting the Model API to the application
                    first = user.get()
                    last = user2.get()
                    middle = user3.get()

                    # initialize the model
                    name = lstm.API_RNN()

                    if middle == '' or middle == 'Middle Name': 
                        fullname1 = first+' '+last
                    else:
                        fullname1 = first+' '+middle+' '+last
                    fullname = capitalize_name(fullname1)
                    
                    # this part is for the transformer
                    # rst = name.decode(fullname)  
                    
                    # this part is for RNN
                    df = [fullname]
                    rst1 = name.call(pd.DataFrame(np.array(df)))
                    rst = []
                    for i in range(len(rst1)):
                        rst.append(capitalize_name(rst1[i]))
                    # rst = str(rst1)

                    # Results output page
                    title1 = Label(frame2,text='Original Name',fg='#57a1f8',bg='#101517',font=('times new roman',15,'bold'))

                    title1.place(x=100,y=100)
                    title2 = Label(frame2,text='Matched Name',fg='#57a1f8',bg='#101517',font=('times new roman',15,'bold'))
                    title2.place(x=400,y=100)
                    heading.place(relx=0.4,rely=0)

                    generated_names = tk.Label(frame2, text="\n".join(rst[:3]),bg='#101517',fg="#57a1f8",font=('Times new roman',15))
                    generated_names.place(x=400,y=150)
                    # generated_names.pack()
                    
                    org_name = tk.Label(frame2, text=fullname,bg='#101517',fg="#57a1f8",font=('Times new roman',15,'bold'))
                    # org_name.pack()
                    org_name.place(x=100,y=150)

                    

                    Button(frame2,width=15,pady=7,text='Back',bg='#57a1f8',fg='#101517',border=0,command=name_matching).place(x=328,y=420)


                Button(frame,width=15,pady=7,text='Match',bg='#57a1f8',fg='#101517',border=0,command=rslt_NM).place(x=420,y=350)

                Button(frame,width=15,pady=7,text='Back',bg='#57a1f8',fg='#101517',border=0,command=name_matching).place(x=235,y=350)
    name_matching()