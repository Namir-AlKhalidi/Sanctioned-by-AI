# libraries for the application page
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import *
import random

# for generating name variants depending on how the name is sounded
from phonetics import dmetaphone

# Model's pipeline
import Name_Matching as NM


def main(screen):
    # this is a function that is used to call Name Matching tool
    def NMF():
        NM.main(screen)
    # Name Generator tool
    def name_generator():
                frame=Frame(screen,width=775,height=500,bg='#101517')
                frame.place(x=150,y=0)  
                screen.geometry('925x500+300+200')
                screen.configure(bg='#101517')
                screen.title('Name Generator Page')
                heading= Label(frame,text='Name Generator',fg='#57a1f8',bg='#101517',font=('Microsoft YaHei UI Light',23,'bold'))
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

                # this function is used to capitalize the first letter of each name 
                def capitalize_name(name): 
                    name_parts = name.split()
                    capitalized_parts = [part.capitalize() for part in name_parts]
                    capitalized_name = ' '.join(capitalized_parts)

                    return capitalized_name

                # results page for the Name Generator tool
                def rslt_NG():
                    frame=Frame(screen,width=775,height=500,bg='#101517')
                    frame.place(x=150,y=0)
                    screen.geometry('925x500+300+200')
                    screen.configure(bg='#101517')
                    screen.title('Name Generator Results')
                    heading= Label(frame,text='Name Generator Results',fg='#57a1f8',bg='#101517',font=('Microsoft YaHei UI Light',10,'bold'))
                    heading.place(relx=0.4,rely=0)
                    # heading.place(relx=0.4,rely=0)

                    #function that creates variant names with similar phonetic
                    def generate_name_variants(name): 
                        variants = []
                        suffixes = ["son", "ston", "sen", "syn", "san", "zad", "fah", "al", "el", "bin"]

                        for i in range(len(name)):
                            for j in range(i + 1, len(name)):
                                for k in range(len(name)):
                                    if k != i and k != j:
                                        letters = list(name)
                                        letters[i], letters[k] = letters[k], letters[i]
                                        letters[j], letters[k] = letters[k], letters[j]
                                        name_variation = "".join(letters)
                                        if dmetaphone(name_variation)[0] == dmetaphone(name)[0] and name_variation not in variants:
                                            variants.append(name_variation)

                        for suffix in suffixes:
                            variant = name + suffix
                            if dmetaphone(variant)[0] == dmetaphone(name)[0] and variant not in variants:
                                variants.append(variant)

                        random.shuffle(variants)

                        return variants
                    
                    title1= Label(frame,text='Original Name',fg='#4f94d4',bg='#101517',font=('times new roman',15,'bold'))
                    title1.place(x=150,y=100)
                    title2= Label(frame,text='Generated Names',fg='#4f94d4',bg='#101517',font=('times new roman',15,'bold'))
                    title2.place(x=425,y=100)
                    fullname1 = user.get()+' '+user2.get()
                    fullname = capitalize_name(fullname1)
                    GN = generate_name_variants(fullname)
                    generated_names = tk.Label(frame, text="\n".join(GN[:10]),fg='#4f94d4',bg='#101517',font=('Times new roman',15))
                    generated_names.place(x=430,y=150)
                    org_name = tk.Label(frame, text=fullname,fg='#4f94d4',bg='#101517',font=('Times new roman',15))
                    org_name.place(x=150,y=150)


                    Button(frame,width=15,pady=7,text='Back',bg='#57a1f8',fg='#101517',border=0,command=name_generator).place(x=328,y=420)

                Button(frame,width=15,pady=7,text='Generate',bg='#57a1f8',fg='#101517',border=0,command=rslt_NG).place(x=415,y=280)

                Button(frame,width=15,pady=7,text='Back',bg='#57a1f8',fg='#101517',border=0,command=NMF).place(x=230,y=280)
    name_generator()
