# application libraries
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import *

# libraries that are used to make the tool work
from googlesearch import search
import newspaper
from newspaper import ArticleException
from requests.exceptions import HTTPError

# Model's pipeline
import Name_Matching as NM



def main(screen):
    def NMF(): # To call the Name Matching tool
        NM.main(screen)
    def adverse_media(): 
                frame=Frame(screen,width=775,height=500,bg='#101517')
                frame.place(x=150,y=0)  
                screen.geometry('925x500+300+200')
                screen.configure(bg='#101517')
                screen.title('Adverse Media Page')
                heading= Label(frame,text='Adverse Media',fg='#57a1f8',bg='#101517',font=('Microsoft YaHei UI Light',23,'bold'))
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

                first = user.get()
                last = user2.get()
                middle = user3.get()

                # create results page and display the them
                def rslt_AM():
                    frame=Frame(screen,width=775,height=500,bg='#101517')#bg='#101517')
                    frame.place(x=150,y=0)  
                    screen.geometry('925x500+300+200')
                    screen.configure(bg='#101517')
                    screen.title('Adverse Media Results')
                    heading= Label(frame,text='Adverse Media Results',fg='#57a1f8',bg='#101517',font=('Times New Roman',15,'bold'))
                    heading.place(relx=0.5,rely=0.1,anchor='center')


                    def get_top_3_google_searches(query):
                        try:
                            search_results = search(query, num_results=3, lang="en")
                            return list(search_results)
                        except HTTPError as e:
                            if "429" in str(e):
                                return "No results. Too Many Requests error occurred."
                            else:
                                raise 

                    # Ask the user for a query
                    # user_query = user.get()+' '+user2.get()
                    first = user.get()
                    last = user2.get()
                    middle = user3.get()
                    if middle == '' or middle == 'Middle Name': 
                        fullname = first+' '+last
                    else:
                        fullname = first+' '+middle+' '+last

                    # Get the top 3 Google search results
                    top_3_results = get_top_3_google_searches(fullname)

                    # Print the results
                    lst = []
                    print("Top 3 Google search results for '{}':".format(fullname))
                    tlt = Label(frame,text = "Top 3 Google search results for '{}':".format(fullname),fg='#57a1f8',bg='#101517',font=('times new roman',13,'bold'))
                    tlt.place(relx=0.5,rely=0.2,anchor='center')
                    for index, result in enumerate(top_3_results, start=1):
                        if index <4:
                            lst.append("{}. {}".format(index, result))
                    title = tk.Label(frame,text = "\n".join(lst),fg='#57a1f8',bg='#101517',font=('times new roman',10,'bold'))
                    title.place(relx=0.5,rely=0.3,anchor='center')
                    # title.pack()
                    

                    def summarize_website(url):
                        # Initialize a newspaper Article object with the provided URL
                        article = newspaper.Article(url)

                        # Download and parse the article content
                        try:
                            article.download()
                            article.parse()



                            # Perform natural language processing to generate a summary
                            article.nlp()
                        
                            # Return the summary
                            return article.summary
                        except ArticleException as e:
                            if "No connection adapters" in str(e):
                                return 0
                            else:
                                raise

                    lst2 = []
                    for i in range(3):
                        summary = summarize_website(top_3_results[i])
                        if summary == '' or summary == 0:
                            warn = tk.Label(frame, text = "No summary was able to be provided",fg='#57a1f8',bg='#101517',font=('Times new roman',13,'bold')).place(relx=0.5,rely=0.5,anchor='center')
                            # warn.place(relx=0.3,rely=0.5)
                        else:
                            lst2.append(summary)

                    result = tk.Label(frame,text = "\n".join(lst2),fg='#57a1f8',bg='#101517',font=('Times new roman',13,'bold')).place(relx=0.5,rely=0.5,anchor='center')
                    # result.pack()
                            # result.place(relx=0.3,rely=0.5)
                        

                    Button(frame,width=15,pady=7,text='Back',bg='#57a1f8',fg='#101517',border=0,command=adverse_media).place(relx=0.5,rely=0.85,anchor='center')# Go back to Adverse media page



                Button(frame,width=15,pady=7,text='Start',bg='#57a1f8',fg='#101517',border=0,command=rslt_AM).place(x=420,y=350)# go to results page

                Button(frame,width=15,pady=7,text='Back',bg='#57a1f8',fg='#101517',border=0,command=NMF).place(x=235,y=350)# go back to name matching tool
    adverse_media()