
# application libraries
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import *

# library to display interactive maps on Tkinter
import tkintermapview

# calling the name matching tool
import Name_Matching as NM

def main(screen):
    def NMF():
        NM.main(screen)
    def regional_analysis():
                frame=Frame(screen,width=775,height=500,bg='#101517')
                frame.place(x=150,y=0)  
                screen.geometry('925x500+300+200')
                screen.configure(bg='#101517')
                screen.title('Regional Analysis Page')
                heading= Label(frame,text='Regional Analysis',fg='#57a1f8',bg='#101517',font=('Microsoft YaHei UI Light',23,'bold'))
                # heading.place(x=45,y=0)
                heading.place(relx=0.5,rely=0.2,anchor='center')

                def on_enter(e):
                    user.delete(0,'end')

                def on_leave(e):
                    name=user.get()
                    if name=='':
                        user.insert(0,'First Name*')

                # input and line are always 5 in the x different, line lower, and 27 in the y line greater, 70 y each sec
                user=Entry(frame,width=25,fg='#57a1f8',border=0,bg='#101517',font=('Microsoft YaHei UI Light',11))
                user.place(x=240,y=160)
                user.insert(0,'First Name*')
                # fname = user.get()
                user.bind('<FocusIn>', on_enter)
                user.bind('<FocusOut>', on_leave)
                # print("user is: ",user.get())
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
                # lname = user2.get()
                user2.bind('<FocusIn>', on_enter2)
                user2.bind('<FocusOut>', on_leave2)
                Frame(frame,width=295,height=2,bg='#4f94d4').place(x=235,y=257)

                # def on_enter3(e):
                #     user3.delete(0,'end')

                # def on_leave3(e):
                #     name=user3.get()
                #     if name=='':
                #         user3.insert(0,'Country*')

                # user3=Entry(frame,width=25,fg='#57a1f8',border=0,bg='#101517',font=('Microsoft YaHei UI Light',11))
                # user3.place(x=240,y=300)
                # user3.insert(0,'Country*')
                # country = user3.get()
                # print('country is:', country)
                # user3.bind('<FocusIn>', on_enter3)
                # user3.bind('<FocusOut>', on_leave3)
                countries = ['Select the Country','Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia',
                    'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
                    'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil',
                    'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada',
                    'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica',
                    'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
                    'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini',
                    'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece',
                    'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland',
                    'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Italy', 'Jamaica', 'Japan', 'Jordan',
                    'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kosovo', 'Kuwait', 'Kyrgyzstan',
                    'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg',
                    'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania',
                    'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique',
                    'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
                    'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea',
                    'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda',
                    'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino',
                    'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore',
                    'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka',
                    ' Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand',
                    'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine',
                    'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City',
                    'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
                ]
                # clicked = StringVar(frame)
                # clicked.set('Select Country')
                style = ttk.Style()
                style.configure("Custom.TMenubutton", foreground='#57a1f8', background='#101517', width=32, height=8, relief=tk.FLAT,font=('Microsoft YaHei UI Light',11))
                clicked = tk.StringVar(frame)

                drop = ttk.OptionMenu(frame, clicked, *countries, style="Custom.TMenubutton")
                drop.pack()
                drop.place(x=235,y=300)
                menu = drop["menu"]
                menu.configure(foreground='#57a1f8', background='#101517')
                Frame(frame,width=295,height=2,bg='#4f94d4').place(x=235,y=327)
                def rslt_RA():
                    fname = user.get()
                    # print("fname is: ",fname)
                    lname = user2.get()
                    # print("lname is: ",lname)
                    country = clicked.get()
                    # print("country is: ",country)
                    frame=Frame(screen,width=775,height=550,bg='#101517')
                    frame.place(x=150,y=0)  
                    screen.geometry('925x500+300+200')
                    screen.configure(bg='#101517')
                    screen.title('Regional Analysis Results')
                    # heading= Label(frame,text='Regional Analysis Results',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',10,'bold'))
                    # heading.place(x=230,y=0)
                    my_label = LabelFrame(frame,width=775,height=550)
                    my_label.place(relx=0.5,rely=0.4,anchor='center')
                    # my_label.pack(pady=20)

                    map_widget = tkintermapview.TkinterMapView(my_label, width=600, height=350, corner_radius=1)
                    name = country
                    # Set Address
                    map_widget.set_address(country,marker=True).set_text(fname+" "+lname)


                    # Set A Zoom Level
                    map_widget.set_zoom(0)
                    Button(frame,width=15,pady=7,text='Back',bg='#57a1f8',fg='#101517',border=0,command=regional_analysis).place(x=328,y=420)

                    map_widget.pack()


                    screen.mainloop()

                    



                Button(frame,width=15,pady=7,text='Analyze',bg='#57a1f8',fg='#101517',border=0,command=rslt_RA).place(x=420,y=350)

                Button(frame,width=15,pady=7,text='Back',bg='#57a1f8',fg='#101517',border=0,command=NMF).place(x=235,y=350)
    regional_analysis()