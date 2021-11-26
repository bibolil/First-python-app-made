
import csv
import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
import os
from tkinter import scrolledtext
import tkinter.ttk as ttk

schemeDark = {'main bg': '#2C2F33', 'bg': '#383c41', 'label fg': '#8e8a69', 'text fg': '#8b6379',
              'button fg': '#10141b', 'text fg selected': '#4b4f54'}
active_scheme = schemeDark




def configure_default_settings(widget, size):
    if isinstance(widget, tk.Label):
        widget.config(
            bg=active_scheme['main bg'],
            fg=active_scheme['label fg'],
            font='Arial ' + str(size),
        )
    elif isinstance(widget, tk.Entry) or isinstance(widget, tk.Text):
        widget.config(
            bg=active_scheme['bg'],
            fg=active_scheme['text fg'],
            selectbackground=active_scheme['text fg selected'],
            selectforeground=active_scheme['text fg'],
            font='Arial ' + str(size),
            border=0
        )
    elif isinstance(widget, tk.Button):
        widget.config(
            bg=active_scheme['bg'],
            fg=active_scheme['button fg'],
            activebackground=active_scheme['main bg'],
            activeforeground=active_scheme['bg'],
            font='Arial ' + str(size),
            border=0,
            relief=FLAT
        )
    elif isinstance(widget, tk.Frame):
        widget.config(
            bg=active_scheme['main bg']
        )
        for num in range(size):
            widget.grid_columnconfigure(num, weight=1)
    elif isinstance(widget, tk.Listbox):
        widget.config(
            bg=active_scheme['bg'],
            fg='black',
            highlightbackground='black',
            highlightcolor='black',
            selectbackground=active_scheme['text fg selected'],
            selectforeground=active_scheme['text fg'],
            border=0,
            width=30,
            height=size
        )
    elif isinstance(widget, tk.Checkbutton):
        widget.config(
            bg=active_scheme['main bg'],
            fg=active_scheme['label fg'],
            activebackground=active_scheme['main bg'],
            activeforeground=active_scheme['label fg'],
            font='Arial ' + str(size),
            selectcolor=active_scheme['bg']
        )

def existence(code,l):
      lst=[]
      x=0
      try:  
        with open("jobslist.csv",'r') as data:
            reader=csv.reader(data,delimiter=';')
            for line in reader:
                lst.append(line)
        for i in lst:
            if i[l]==code:
                x=1
        if x==0:
            return False
        else:
            return True
      except FileNotFoundError:
        showwarning('Error','No File yet!')   

          

        
#---------------------------------------------------------------------#ADMINSTRATOR CODE#---------------------------------------------------------------------#
def addnewjoboffer():

    window=tk.Toplevel()
    window.configure(bg=active_scheme['main bg'])

    #code input
    label_code=tk.Label(window,text='Enter a code for the new job:')
    code=StringVar()
    entry_code=tk.Entry(window,textvariable=code)

    label_companyinfo = tk.Label(window,text='Company informations:')

    #name input
    label_name = tk.Label(window,text='Name:')
    name=StringVar()
    entry_name=tk.Entry(window,textvariable=name)

    #phone number input
    label_phone = tk.Label(window,text='Phone Number:')
    phonenumber=StringVar()
    entry_phonenum=tk.Entry(window,textvariable=phonenumber)

    #address input
    label_address = tk.Label(window,text='Address:')
    address=StringVar()
    entry_address=tk.Entry(window,textvariable=address)


    label_profiledesc = tk.Label(window,text='Profile description:')

    #Degree input
    label_degree = tk.Label(window,text='Degree:')
    degree=StringVar()
    entry_degree=tk.Entry(window,textvariable=degree)

    #qualification input
    label_qual = tk.Label(window,text='Qualification:')
    qualification=StringVar()
    entry_qualification=tk.Entry(window,textvariable=qualification)

    #experience input
    label_exp = tk.Label(window,text='Experience:')
    experience=StringVar()
    entry_experience=tk.Entry(window,textvariable=experience)

    #mission description input
    label_missdesc = tk.Label(window,text='Mission description: ')
    
    mission=StringVar()
    entry_mission=tk.Entry(window,textvariable=mission)
    #domaine input
    label_domaine=tk.Label(window,text='Domaine: ')
    domaine=StringVar()
    entry_domaine=tk.Entry(window,textvariable=domaine)
    #register in file function
    def register():
        f=open("jobslist.csv","a")
        lst=[]
        x=1
        modification=0
        with open("jobslist.csv",'r') as data:
            reader=csv.reader(data,delimiter=';')
            for line in reader:
                lst.append(line)
        for i in lst:
            if i[0]==code.get():
                code.set('')
                x=0
                showwarning('Warning','The used code already exist!')
        if code.get()=='' or name.get()=='' or phonenumber.get()=='' or address.get()=='' or degree.get()=='' or qualification.get()=='' or experience.get()=='' or mission.get()=='' or domaine.get()=='':
            showwarning('Warning','There are missed informations')            

        elif x==1:        
            ligne=code.get()+";"+name.get()+";"+phonenumber.get()+";"+address.get()+";"+degree.get()+";"+qualification.get()+";"+experience.get()+";"+mission.get()+";"+domaine.get()
            f.write(ligne)
            f.write("\n")
            f.close()
            code.set("")
            name.set("")
            phonenumber.set("")
            address.set("")
            degree.set("")
            qualification.set("")
            experience.set("")
            mission.set("")
            domaine.set("")
        
    button=Button(window,text="Register",command=register) #tzyd fel fichiers
    button1=Button(window,text='Exit',command=window.destroy)

    # CONFIGURING
    configure_default_settings(label_code, 13)
    configure_default_settings(entry_code, 13)
    configure_default_settings(label_companyinfo, 10)
    configure_default_settings(label_name, 13)
    configure_default_settings(entry_name, 13)
    configure_default_settings(label_phone, 13)
    configure_default_settings(entry_phonenum, 13)
    configure_default_settings(label_address, 13)
    configure_default_settings(entry_address, 13)
    configure_default_settings(label_profiledesc, 10)
    configure_default_settings(label_degree, 13)
    configure_default_settings(entry_degree, 13)
    configure_default_settings(label_qual, 13)
    configure_default_settings(entry_qualification, 13)
    configure_default_settings(label_exp, 13)
    configure_default_settings(entry_experience, 13)
    configure_default_settings(label_missdesc, 13)
    configure_default_settings(entry_mission, 13)
    configure_default_settings(entry_domaine,13)
    configure_default_settings(label_domaine,13)
    configure_default_settings(button, 13)
    configure_default_settings(button1, 13)

    # GRIDING
    label_code.grid(row=1, column=0, padx=8)
    entry_code.grid(row=1,column=1,padx=5)
    label_companyinfo.grid(row=2,column=0,columnspan=2,padx=5,pady=(10, 0))
    label_name.grid(row=3,column=0,padx=5)
    entry_name.grid(row=3,column=1,padx=5)
    label_phone.grid(row=4,column=0,padx=5)
    entry_phonenum.grid(row=4,column=1,padx=5)
    label_address.grid(row=5,column=0,padx=5)
    entry_address.grid(row=5,column=1,padx=5)
    label_profiledesc.grid(row=6, column=0, columnspan=2, padx=5, pady=(10, 0))
    label_degree.grid(row=7,column=0,padx=5)
    entry_degree.grid(row=7,column=1,padx=5)
    label_qual.grid(row=8,column=0,padx=5)
    entry_qualification.grid(row=8,column=1,padx=5,pady=5)
    label_exp.grid(row=9,column=0,padx=5)
    entry_experience.grid(row=9,column=1,padx=5)
    label_missdesc.grid(row=10,column=0,padx=5)
    entry_mission.grid(row=10,column=1,padx=5)
    label_domaine.grid(row=11,column=0,padx=5)
    entry_domaine.grid(row=11,column=1,padx=5)
    button.grid(row=12,column=0,columnspan=2,padx=5,pady=(10, 0))
    button1.grid(row=13,column=0,columnspan=2,padx=5,pady=(10, 0))


def updateajoboffer():
 
    window=tk.Toplevel()
    window.configure(bg=active_scheme['main bg'])

    label=tk.Label(window,text='Enter a job code')
    cd=StringVar()
    entry_code=tk.Entry(window,textvariable=cd)

    def update():
        
        if existence(cd.get(),0)==False:
            showwarning("Error","Write an existin code !")
            
        else:
            lst=[]
            with open("jobslist.csv",'r') as data:
               reader=csv.reader(data,delimiter=';')
               for line in reader:
                  lst.append(line)
            for i in lst:
              if i[0]==cd.get():
                  
                  a="Name: "+i[1]
                  b="Phone number: "+i[2]
                  c="Address: "+i[3]
                  d="Degree: "+i[4]
                  e="Qualification: "+i[5]
                  f="Experience: "+i[6]
                  h="Mission description: "+i[7]
                  k="Domaine: "+i[8]
                  
            window1=tk.Toplevel()
            window1.configure(bg=active_scheme['main bg'])


            #labels
            label=tk.Label(window1,text=a)
            label1=tk.Label(window1,text=b)
            label2=tk.Label(window1,text=c)
            label3=tk.Label(window1,text=d)
            label4=tk.Label(window1,text=e)
            label5=tk.Label(window1,text=f)
            label6=tk.Label(window1,text=h)
            label8=tk.Label(window1,text=k)
            label7=tk.Label(window1,text="rewrite the job offer data with the desired modification")


            configure_default_settings(label,15)
            configure_default_settings(label1,15)
            configure_default_settings(label2,15)
            configure_default_settings(label3,15)
            configure_default_settings(label4,15)
            configure_default_settings(label5,15)
            configure_default_settings(label6,15)
            configure_default_settings(label7,15)
            configure_default_settings(label8,15)
            

            #Entries
            
            name=StringVar()
            entry_name=tk.Entry(window1,textvariable=name)

            phonenumber=StringVar()
            entry_phonenum=tk.Entry(window1,textvariable=phonenumber)

            address=StringVar()
            entry_address=tk.Entry(window1,textvariable=address)

            degree=StringVar()
            entry_degree=tk.Entry(window1,textvariable=degree)

            qualification=StringVar()
            entry_qualification=tk.Entry(window1,textvariable=qualification)

            experience=StringVar()
            entry_experience=tk.Entry(window1,textvariable=experience)

            mission=StringVar()
            entry_mission=tk.Entry(window1,textvariable=mission)

            domaine=StringVar()
            entry_domaine=tk.Entry(window1,textvariable=domaine)


            
            



            def loadnewmodification():
                lst=[]
                lst1=[]
                with open("jobslist.csv",'r') as data: 
                   reader=csv.reader(data,delimiter=';')
                   for line in reader:
                      lst.append(line)
                os.remove("jobslist.csv")    
                with open('jobslist.csv','a') as lecture:
                    for i in lst:
                         if i[0]==cd.get():
                              i[1]=name.get();
                              i[2]=phonenumber.get();
                              i[3]=address.get();
                              i[4]=degree.get();
                              i[5]=qualification.get();
                              i[6]=experience.get();
                              i[7]=mission.get();
                              i[8]=domaine.get();
                         line=""
                         line=i[0]
                         line=';'.join(i[0:])
                         line+='\n'
                         lst1.append(line)
                    lecture.writelines(lst1)
                window2=tk.Toplevel()
                window2.configure(bg=active_scheme['main bg'])
                label10=tk.Label(window2,text="database successfuly updated")
                button3=Button(window2,text="Return",command=window2.destroy)
                configure_default_settings(label10,15)
                configure_default_settings(button3,15)
                label10.grid(row=1,column=0)
                button3.grid(row=2,column=0,columnspan=2,padx=5,pady=(10, 0))
                
                
            button=Button(window1,text="Update",command=loadnewmodification)
            button1=Button(window1,text="Exit",command=window1.destroy)


            #CONFIGURATION

            
            configure_default_settings(entry_domaine,15)
            configure_default_settings(entry_name,15)
            configure_default_settings(entry_phonenum,15)
            configure_default_settings(entry_address,15)
            configure_default_settings(entry_degree,15)
            configure_default_settings(entry_qualification,15)
            configure_default_settings(entry_experience,15)
            configure_default_settings(entry_mission,15)
            configure_default_settings(button,15)
            configure_default_settings(button,15)
            configure_default_settings(button1,15)
            
            #GRIDING
            label7.grid(row=1,column=0)
            label.grid(row=2,column=0)
            label1.grid(row=3,column=0)
            label2.grid(row=4,column=0)
            label3.grid(row=5,column=0)
            label4.grid(row=6,column=0)
            label5.grid(row=7,column=0)
            label6.grid(row=8,column=0)
            label8.grid(row=9,column=0)
            entry_name.grid(row=2,column=1)
            entry_phonenum.grid(row=3,column=1)
            entry_address.grid(row=4,column=1)      
            entry_degree.grid(row=5,column=1)      
            entry_qualification.grid(row=6,column=1)       
            entry_experience.grid(row=7,column=1)
            entry_mission.grid(row=8,column=1)
            entry_domaine.grid(row=9,column=1)
            button.grid(row=10,column=0,columnspan=2,padx=5,pady=(10, 0))
            button1.grid(row=11,column=0,columnspan=2,padx=5,pady=(10, 0))
            


            
    button=Button(window,text='Browse',command=update)#taffichy  el fichier bsh tbadel feha
    button1=Button(window,text='Exit',command=window.destroy)

    configure_default_settings(label, 13)
    configure_default_settings(entry_code, 13)
    configure_default_settings(button, 13)
    configure_default_settings(button1, 13)

    label.grid(row=1,column=0,padx=5)
    entry_code.grid(row=1,column=1,padx=5)
    button.grid(row=2,column=0,columnspan=2,padx=5,pady=(10, 0))
    button1.grid(row=3,column=0,columnspan=2,padx=5,pady=(10, 0))


def deletejob():

    window=tk.Toplevel()
    window.configure(bg=active_scheme['main bg'])

    code=StringVar()

    label = tk.Label(window,text='Enter a job code')
    entry_code=tk.Entry(window,textvariable=code)

    configure_default_settings(label, 13)
    configure_default_settings(entry_code, 13)

    label.grid(row=1, column=0, padx=5)
    entry_code.grid(row=1,column=1,padx=5)
    
    
    def delete():
     if existence(code.get(),0)==True :

         lst=[]
         x=0
         modification=0
         with open("jobslist.csv",'r') as data:
             reader=csv.reader(data,delimiter=';')
             for line in reader:
                 lst.append(line)
         for i in lst:
             if i[0]==code.get():
                 lst.pop(x)
             x+=1
             cd=1
         lst1=[]
         if cd==1:
             os.remove('jobslist.csv')
             with open('jobslist.csv','a') as lecture:
                 for i in lst:
                     line=""
                     line=i[0]
                     line=';'.join(i[0:])
                     line+='\n'
                     lst1.append(line)
                 lecture.writelines(lst1)
         code.set('')
     else:
         showwarning('Error','Write an existing code!')
         code.set('')
         

        
        
    button=Button(window,text='delete',command=delete)
    button1=Button(window,text='Exit',command=window.destroy)

    configure_default_settings(button, 13)
    configure_default_settings(button1, 13)

    button.grid(row=2,column=0,columnspan=2,padx=5,pady=(10, 0))
    button1.grid(row=3,column=0,columnspan=2,padx=5,pady=(10, 0))


    
def brows():
    global txt2,option2
    window=tk.Toplevel()
    window.configure(bg=active_scheme['main bg'])
    LB1 = Label(window, text="Job offers :")
    LB1.pack()
    browse = Frame(window, borderwidth=60)
    browse.pack(fill=BOTH, expand=True)
    option2 = IntVar()
    MyColor='#2C2F33'
    s=ttk.Style()
    s.configure('Wild.TRadiobutton',background=MyColor,foreground='white')
    rad1 = ttk.Radiobutton(browse,text='Option 1 :List all job seekers that applied for job offers',style = 'Wild.TRadiobutton', value=0, variable=option2)
    rad2 = ttk.Radiobutton(browse,text='Option 2 :List the job seekers that applied for the same job',style = 'Wild.TRadiobutton', value=1, variable= option2)
    txt2 = scrolledtext.ScrolledText(browse, width=50,height=16)
    LB2=Label(window,text="NB :write a job code if you picked option 2")
    txt2.pack(side=LEFT)
    rad1.pack(side=TOP)
    rad2.pack(side=TOP)
    LB2.pack(side=TOP)
    search = StringVar()
    SearchBox = Entry(browse, textvariable=search)
    SearchBox.pack(side=TOP, pady=5)

    def listbrows():
        txt2.delete(1.0,END)
        if option2.get()==0:
            with open("appliedjobs.csv",'r') as data:
             reader=csv.reader(data,delimiter=';')
             for line in reader:
                 txt2.insert(INSERT,str(line)+'\n')
        elif option2.get()==1 and search.get()!='':
            with open("appliedjobs.csv",'r') as data:
             reader=csv.reader(data,delimiter=';')
             for line in reader:
                 if line[1]==search.get():
                     txt2.insert(INSERT,str(line)+'\n')
        elif option2.get()==1 and search.get()=='':
            showwarning("Error,write a job code for option 2")
            
            

            
    BB1 = Button(browse, text='List', fg='navy', command=listbrows)
    BB1.pack(side=TOP)
    
    BB6= Button(browse,text="Exit",command=window.destroy)
    BB6.pack()

    configure_default_settings(LB1,16)
    configure_default_settings(browse,10)
    
    configure_default_settings(LB2,10)
    window.mainloop()

    

def roles():
    window0.destroy()
    window1=tk.Toplevel()
    frame=tk.Frame(window1)
    window1.configure(bg=active_scheme['main bg'])
    button2=Button(frame,text="Add new job offer",command=addnewjoboffer)
    button3=Button(frame,text="Update a job offer",command=updateajoboffer)
    button1=Button(frame,text="Delete a job offer ",command=deletejob)
    button5=Button(frame,text="Exit",command=window1.destroy)
    button4=Button(frame,text="Brows the list of job ",command=brows)
    label=tk.Label(frame,text=" ")
    label1=tk.Label(frame,text=" ")
    label2=tk.Label(frame,text=" ")
    label3=tk.Label(frame,text=" ")
    frame.grid(padx=50,pady=50)


    #CONFIGURING
    configure_default_settings(button1, 13)
    configure_default_settings(button2, 13)
    configure_default_settings(button3, 13)
    configure_default_settings(button4, 13)
    configure_default_settings(button5, 13)
    configure_default_settings(label,10)
    configure_default_settings(label1,10)
    configure_default_settings(label2,10)
    configure_default_settings(label3,10)
    configure_default_settings(frame,1)

    #GRIDING
    button2.grid(row=1,column=0)
    label.grid(row=2,column=0)
    button3.grid(row=3,column=0)
    label1.grid(row=4,column=0)
    button1.grid(row=5,column=0)
    label2.grid(row=6,column=0)
    button4.grid(row=7,column=0)
    label3.grid(row=8,column=0)
    button5.grid(row=9,column=0)


#fonction ta3 login administrator
def login():
    global window0
    window0 = tk.Toplevel()
    window0.configure(bg=active_scheme['main bg'])

    def check_pass():
        if password.get() == 'root': 
            return roles()
        else:
            showwarning('Results','Password incorrect.\n Try again!')
            password.set('')
    password=StringVar()
    username=StringVar()

    label1 = tk.Label(window0, text='Username:')
    label2 = tk.Label(window0,text='Password:')
    entry_username=tk.Entry(window0,textvariable=username)
    entry_pass=tk.Entry(window0,textvariable=password,show='*')
    button1=Button(window0,text="QUIT",command=window0.destroy)
    button = Button(window0, text="LOG_IN", command=check_pass)
    #CONFIGURATION
    configure_default_settings(label1, 13)
    configure_default_settings(label2, 13)
    configure_default_settings(entry_username, 13)
    configure_default_settings(entry_pass, 13)
    configure_default_settings(button1, 13)
    configure_default_settings(button, 13)

    #GRIDING
    label1.grid(row=1,column=0,padx=5)
    label2.grid(row=2, column=0, padx=5)
    entry_pass.grid(row=2,column=1,padx=10)
    button.grid(column=0,columnspan=2,padx=5,pady=(10, 0))
    button1.grid(column=2)
    entry_username.grid(row=1,column=1,padx=10)


def retry(window):
    login()
    return window.destroy
#------------------------------------------------------------------------------------------------------------------------------------------------------#
def applyforajob():
    window=tk.Toplevel()
    window.configure(bg=active_scheme['main bg'])
    LB1 = Label(window, text="Available job offers :")
    LB1.pack()
    browse = Frame(window, borderwidth=60)
    browse.pack(fill=BOTH, expand=True)
    txt1 = scrolledtext.ScrolledText(browse, width=104,height=16)
    txt1.pack(side=LEFT)
    try:
        
        with open('jobslist.csv','r') as data:
            reader = csv.reader(data, delimiter=';')
            for line in reader:
                    txt1.insert(INSERT,str(line[:8])+'\n')
            data.close()
        
    except FileNotFoundError:
        showwarning('Error','No Job Offers yet!')
    BB1 = Button(browse, text='Apply for a job', fg='black', command=apply_for_a_job)
    BB1.pack(side=TOP)

    BB2= Button(browse,text="Exit",command=window.destroy)
    BB2.pack()
    
    configure_default_settings(LB1,18)
    configure_default_settings(BB1,16)
    configure_default_settings(BB2,16)
    configure_default_settings(browse,10)
    window.mainloop()


def apply_for_a_job():
    global window9
    window9=tk.Toplevel()
    window9.configure(bg=active_scheme['main bg'])
    label=tk.Label(window9,text="Chosen job code")
    jobcode=StringVar()
    entry_code=tk.Entry(window9,textvariable=jobcode)
    label1=tk.Label(window9,text="retype the ID and password for identity confirmation")
    label2=tk.Label(window9,text="ID")
    ab=StringVar()
    entry_ab=tk.Entry(window9,textvariable=ab)
    label3=tk.Label(window9,text="pw")
    bc=StringVar()
    entry_bc=tk.Entry(window9,textvariable=bc)
    
    def applying():
        lst=[]
        r=0
        with open("jobseekers.csv",'r') as data:
            reader=csv.reader(data,delimiter=';')
            for line in reader:
                lst.append(line)
        for i in lst:
            if i[0]==ab.get() and i[1]==bc.get():
                r=1
        

        if r==1:
            f=open("appliedjobs.csv","a")
            lst=[]
            w=0
            with open("appliedjobs.csv",'r') as data:
                reader=csv.reader(data,delimiter=';')
                for line in reader:
                    lst.append(line)
            for i in lst:
                if i[0]==ab.get() and i[1]==jobcode.get():
                      w=1  
            if w==1:
                showinfo("Notice","You already applied for this job")
            else:
                line=ab.get()+";"+jobcode.get()
                f.write(line)
                f.write("\n")
                f.close()
                showinfo("Notice","You applied for the job successfully")
                window9.destroy()
        else:
            showwarning("Error","Wrong username or password")
            window9.destroy()
            
        
    button=Button(window9,text="Apply",command=applying)
    button1=Button(window9,text="Exit",command=window9.destroy)

    configure_default_settings(label,13)
    configure_default_settings(entry_code,13)
    configure_default_settings(button,12)
    configure_default_settings(button1,12)
    configure_default_settings(label1,15)
    configure_default_settings(label2,13)
    configure_default_settings(label3,13)
    configure_default_settings(entry_ab,13)
    configure_default_settings(entry_bc,13)
    

    label.grid(row=1,column=0)
    entry_code.grid(row=1,column=1)
    label1.grid(row=2,column=0)
    label2.grid(row=3,column=0)
    entry_ab.grid(row=3,column=1)
    label3.grid(row=4,column=0)
    entry_bc.grid(row=4,column=1)
    
    button.grid(row=5,column=0,columnspan=2,padx=5,pady=(10,0))
    button1.grid(row=6,column=0,columnspan=2,padx=5,pady=(10,0))
    
    
    

def loginuser():
    global window10
    window10=tk.Toplevel()
    window10.configure(bg=active_scheme['main bg'])
    label1=tk.Label(window10,text="ID :")
    label2=tk.Label(window10,text="password: ")
    label3=tk.Label(window10,text="Not having an ID ? sign up:")
                   
    ID=StringVar()
    pw=StringVar()
    entry_id=tk.Entry(window10,textvariable=ID)
    entry_password=tk.Entry(window10,textvariable=pw,show='*')

    def idverif():
        lst=[]
        x=0
        with open("jobseekers.csv",'r') as data:
            reader=csv.reader(data,delimiter=';')
            for line in reader:
                lst.append(line)
        for i in lst:
            if i[0]==ID.get() and i[1]==pw.get():
                x=1
                
        if x==1:
            seeking()
        else:
            showwarning("Error",'Wrong username or password')
            ID.set('')
            pw.set('')
            
        
    
    button=Button(window10,text="Log in",command=idverif)
    button1=Button(window10,text="Sign up",command=register_)
    button2=Button(window10,text="Exit",command=window10.destroy)


    configure_default_settings(window10,1)
    configure_default_settings(label1,12)
    configure_default_settings(label2,12)
    configure_default_settings(label3,12)
    configure_default_settings(button,12)
    configure_default_settings(button1,12)
    configure_default_settings(button2,12)
    configure_default_settings(entry_id,12)
    configure_default_settings(entry_password,12)
    

    label1.grid(row=1,column=0)
    label2.grid(row=2,column=0)
    entry_id.grid(row=1,column=1)
    entry_password.grid(row=2,column=1)
    label3.grid(row=4,column=0)
    button.grid(row=3,column=0,columnspan=2,padx=5,pady=(10, 0))
    button1.grid(row=5,column=0,columnspan=2,padx=5,pady=(10, 0))
    button2.grid(row=6,column=0,columnspan=2,padx=5,pady=(10,0))
    
    

def register_():
    global window20
    window10.destroy()
    window20=tk.Toplevel()
    window20.configure(bg=active_scheme['main bg'])

    label0=tk.Label(window20,text="Personal informations :")
    configure_default_settings(label0,15)
    

    label=tk.Label(window20,text="ID :")
    ID=StringVar()
    entry_ID=tk.Entry(window20,textvariable=ID)
    configure_default_settings(label,12)
    configure_default_settings(entry_ID,12)

    label1=tk.Label(window20,text="Password :")
    pw=StringVar()
    entry_pw=tk.Entry(window20,textvariable=pw,show='*')
    configure_default_settings(label1,12)
    configure_default_settings(entry_pw,12)

    label2=tk.Label(window20,text="CIN :")
    cin=StringVar()
    entry_cin=tk.Entry(window20,textvariable=cin)
    configure_default_settings(label2,12)
    configure_default_settings(entry_cin,12)

    label3=tk.Label(window20,text="Name :")
    name=StringVar()
    entry_name=tk.Entry(window20,textvariable=name)
    configure_default_settings(label3,12)
    configure_default_settings(entry_name,12)

    label4=tk.Label(window20,text="Address :")
    address=StringVar()
    entry_address=tk.Entry(window20,textvariable=address)
    configure_default_settings(label4,12)
    configure_default_settings(entry_address,12)

    label5=tk.Label(window20,text="Phone Num :")
    phonenum=StringVar()
    entry_phonenum=tk.Entry(window20,textvariable=phonenum)
    configure_default_settings(label5,12)
    configure_default_settings(entry_phonenum,12)

    label6=tk.Label(window20,text="University degree :")
    unideg=StringVar()
    entry_unideg=tk.Entry(window20,textvariable=unideg)
    configure_default_settings(label6,12)
    configure_default_settings(entry_unideg,12)

    label7=tk.Label(window20,text="Professional informations :")
    configure_default_settings(label7,15)

    label8=tk.Label(window20,text="Experience :")
    experience=StringVar()
    entry_experience=tk.Entry(window20,textvariable=experience)
    configure_default_settings(label8,12)
    configure_default_settings(entry_experience,12)

    label9=tk.Label(window20,text="Skills :")
    skills=StringVar()
    entry_skills=tk.Entry(window20,textvariable=skills)
    configure_default_settings(label9,12)
    configure_default_settings(entry_skills,12)

    label0.grid(row=1,column=0,columnspan=2,padx=5,pady=(10, 0))
    
    label.grid(row=2,column=0)
    entry_ID.grid(row=2,column=1)

    label1.grid(row=3,column=0)
    entry_pw.grid(row=3,column=1)

    label2.grid(row=4,column=0)
    entry_cin.grid(row=4,column=1)

    label3.grid(row=5,column=0)
    entry_name.grid(row=5,column=1)

    label4.grid(row=6,column=0)
    entry_address.grid(row=6,column=1)

    label5.grid(row=7,column=0)
    entry_phonenum.grid(row=7,column=1)

    label6.grid(row=8,column=0)
    entry_unideg.grid(row=8,column=1)

    label7.grid(row=9,column=0,columnspan=2,padx=5,pady=(10, 0))

    label8.grid(row=10,column=0)
    entry_experience.grid(row=10,column=1)

    label9.grid(row=11,column=0)
    entry_skills.grid(row=11,column=1)

    def save():
        f=open("jobseekers.csv","a")
        lst=[]
        x=1
        
        with open("jobseekers.csv",'r') as data:
            reader=csv.reader(data,delimiter=';')
            for line in reader:
                lst.append(line)
        for i in lst:
            if i[0]==ID.get():
                ID.set('')
                x=0
                showwarning('Warning','The used ID already exist!')
        if x==1:
            ligne=ID.get()+';'+pw.get()+';'+cin.get()+';'+name.get()+';'+address.get()+';'+phonenum.get()+';'+unideg.get()+';'+experience.get()+';'+skills.get()
            f.write(ligne)
            f.write('\n')
            f.close
            ID.set('')
            name.set('')
            pw.set('')
            cin.set('')
            address.set('')
            phonenum.set('')
            unideg.set('')
            experience.set('')
            skills.set('')
            showinfo("Notification","Signed up successfully")
        window20.destroy()

    button2=Button(window20,text="Register",command=save)
    configure_default_settings(button2,12)

    button1=Button(window20,text="Exit",command=window20.destroy)
    configure_default_settings(button1,12)

    button2.grid(row=12,column=0,columnspan=2,padx=5,pady=(10,0))
    button1.grid(row=13,column=0,columnspan=2,padx=5,pady=(10,0))
                   
    
def updatejobseeker():
    global wind,ID_,password_
    lst=[]
    wind=tk.Toplevel()
    wind.configure(bg=active_scheme['main bg'])
    y=0
    label=tk.Label(wind,text="Re write ID and password to update")
    label1=tk.Label(wind,text="ID :")
    label2=tk.Label(wind,text="Password :")
    ID_=StringVar()
    entry_id=tk.Entry(wind,textvariable=ID_)
    password_=StringVar()
    entry_password=tk.Entry(wind,textvariable=password_,show='*')

    label.grid(row=1,column=0)
    label1.grid(row=2,column=0)
    label2.grid(row=3,column=0)
    entry_id.grid(row=2,column=1)
    entry_password.grid(row=3,column=1)
    button=Button(wind,text="validate",command=test)
    button.grid(row=4,column=0,columnspan=2,padx=5,pady=(10,0))
    
    
    configure_default_settings(label,14)
    configure_default_settings(label1,14)
    configure_default_settings(label2,14)
    configure_default_settings(entry_id,14)
    configure_default_settings(entry_password,14)
    configure_default_settings(button,14)
    

def test():
    global x
    lst=[]
    y=0
    with open("jobseekers.csv",'r') as data:
            reader=csv.reader(data,delimiter=';')
            for line in reader:
                lst.append(line)
    for i in lst:
            if i[0]==ID_.get() and i[1]==password_.get():
                x=i[0]
                y=1
                
    if y==1:
         displayupdate()   
        
    else:
        showwarning("Error","Wrong ID or password")
        
def displayupdate():
        lst=[]
        window=tk.Toplevel()
        window.configure(bg=active_scheme['main bg'])
        
        wind.destroy()
        with open("jobseekers.csv",'r') as data:
            reader=csv.reader(data,delimiter=';')
            for line in reader:
                lst.append(line)
        
        for i in lst:
            if x==i[0]:
                a="Id :"+i[0]
                b="Password :"+i[1]
                c="Cin :"+i[2]
                d="Name :"+i[3]
                e="Address :"+i[4]
                f="Phone num :"+i[5]
                j="university degree :"+i[6]
                h="Experience :"+i[7]
                k="Skills :"+i[8]
                
        label3=tk.Label(window,text=a)
        label4=tk.Label(window,text=b)
        label5=tk.Label(window,text=c)
        label6=tk.Label(window,text=d)
        label7=tk.Label(window,text=e)
        label8=tk.Label(window,text=f)
        label9=tk.Label(window,text=j)
        label10=tk.Label(window,text=h)
        label11=tk.Label(window,text=k)
        label12=tk.Label(window,text="Rewrite the informations with desired modifications")
        
        IDN=StringVar()
        entry3=tk.Entry(window,textvariable=IDN)
        pas=StringVar()
        entry4=tk.Entry(window,textvariable=pas)
        cin=StringVar()
        entry5=tk.Entry(window,textvariable=cin)
        name=StringVar()
        entry6=tk.Entry(window,textvariable=name)
        address=StringVar()
        entry7=tk.Entry(window,textvariable=address)
        phonenum=StringVar()
        entry8=tk.Entry(window,textvariable=phonenum)
        unideg=StringVar()
        entry9=tk.Entry(window,textvariable=unideg)
        experience=StringVar()
        entry10=tk.Entry(window,textvariable=experience)
        skills=StringVar()
        entry11=tk.Entry(window,textvariable=skills)

        configure_default_settings(label3,14)
        configure_default_settings(label4,14)
        configure_default_settings(label5,14)
        configure_default_settings(label6,14)
        configure_default_settings(label7,14)
        configure_default_settings(label8,14)
        configure_default_settings(label9,14)
        configure_default_settings(label10,14)
        configure_default_settings(label11,14)
        configure_default_settings(label12,16)

        configure_default_settings(entry3,14)
        configure_default_settings(entry4,14)
        configure_default_settings(entry5,14)
        configure_default_settings(entry6,14)
        configure_default_settings(entry7,14)
        configure_default_settings(entry8,14)
        configure_default_settings(entry9,14)
        configure_default_settings(entry10,14)
        configure_default_settings(entry11,14)
        
        label12.grid(row=1,column=0)
        label3.grid(row=2,column=0)
        label4.grid(row=3,column=0)
        label5.grid(row=4,column=0)
        label6.grid(row=5,column=0)
        label7.grid(row=6,column=0)
        label8.grid(row=7,column=0)
        label9.grid(row=8,column=0)
        label10.grid(row=9,column=0)
        label11.grid(row=10,column=0)

        
        entry4.grid(row=3,column=1)
        entry5.grid(row=4,column=1)
        entry6.grid(row=5,column=1)
        entry7.grid(row=6,column=1)
        entry8.grid(row=7,column=1)
        entry9.grid(row=8,column=1)
        entry10.grid(row=9,column=1)
        entry11.grid(row=10,column=1)

        def jobseekerup():
            lst=[]
            lst1=[]
            with open("jobseekers.csv",'r') as data: 
                   reader=csv.reader(data,delimiter=';')
                   for line in reader:
                      lst.append(line)
            os.remove("jobseekers.csv")    
            with open('jobseekers.csv','a') as lecture:
                    for i in lst:
                         if x==i[0]:
                              i[1]=pas.get()
                              i[2]=cin.get()
                              i[3]=name.get();
                              i[4]=address.get();
                              i[5]=phonenum.get();
                              i[6]=unideg.get();
                              i[7]=experience.get();
                              i[8]=skills.get();
                         line=""
                         line=i[0]
                         line=';'.join(i[0:])
                         line+='\n'
                         lst1.append(line)
                    lecture.writelines(lst1)
            showinfo("Update","Updated successfuly")
            window.destroy()

        buttonup=Button(window,text="Update",command=jobseekerup)
        buttonup.grid(row=11,column=0,columnspan=2,padx=5,pady=(10,0))
        configure_default_settings(buttonup,14)
        
    
def Search():
    try:
        txt.delete(1.0,END)
        cd =0
        with open('jobslist.csv','r') as data:
            reader = csv.reader(data, delimiter=';')
            X="[Name;PhoneNum;Address;Degree;Qualification;Experience;Mission;Domaine]"
            txt.insert(INSERT,X+'\n')
            for line in reader:
                if line[option.get()]==(search.get()):
                    cd=1
                    txt.insert(INSERT,str(line[:8])+'\n')
            data.close()
        if cd==0:
            showwarning('Error','No such offer exists!')
    except FileNotFoundError:
        showwarning('Error','No Job Offers yet!')   


def listing():
    try:
        txt.delete(1.0,END)
        
        with open('jobslist.csv','r') as data:
            reader = csv.reader(data, delimiter=';')
            for line in reader:
                    txt.insert(INSERT,str(line[:8])+'\n')
            data.close()
        
    except FileNotFoundError:
        showwarning('Error','No Job Offers yet!')


def jobseeking():
    global option, search,txt
    admin=tk.Toplevel()
    admin.configure(bg=active_scheme['main bg'])
    LB1 = Label(admin, text="Welcome,Choose search options:")
    LB1.pack()
    browse = Frame(admin, borderwidth=60)
    browse.pack(fill=BOTH, expand=True)
    option = IntVar()
    MyColor='#2C2F33'
    s=ttk.Style()
    s.configure('Wild.TRadiobutton',background=MyColor,foreground='white')
    rad1 = ttk.Radiobutton(browse,text='by JobID      ',style = 'Wild.TRadiobutton', value=0, variable=option)
    rad2 = ttk.Radiobutton(browse,text='by Domain  ',style = 'Wild.TRadiobutton', value=7, variable= option)
    rad3 = ttk.Radiobutton(browse,text='by Location',style = 'Wild.TRadiobutton', value=3, variable=option)
    txt = scrolledtext.ScrolledText(browse, width=104,height=16)
    txt.pack(side=LEFT)
    rad1.pack(side=TOP)
    rad2.pack(side=TOP)
    rad3.pack(side=TOP)
    search = StringVar()
    SearchBox = Entry(browse, textvariable=search)
    SearchBox.pack(side=TOP, pady=5)
    BB1 = Button(browse, text='Search', fg='navy', command=Search)
    BB1.pack(side=TOP)
    BB3 = Button(browse, text='List All', command=listing)
    BB3.pack()
    
    BB6= Button(browse,text="Exit",command=admin.destroy)
    BB6.pack()

    configure_default_settings(LB1,16)
    configure_default_settings(browse,10)
    configure_default_settings(SearchBox,10)
    admin.mainloop()



def seeking():
    window10.destroy()
    window=tk.Toplevel()
    window.configure(bg=active_scheme['main bg'])

    button=Button(window,text="Search job offer",command=jobseeking)
    button1=Button(window, text="Brows and apply for a job offer ", command=applyforajob)
    button2=Button(window,text="Update a job seeker information",command=updatejobseeker)
    button3=Button(window,text="Exit",command=window.destroy)

    label=Label(window,text=" ")
    label2=Label(window,text=" ")
    label3=Label(window,text=" ")
    label4=Label(window,text=" ")
    configure_default_settings(button, 12)
    configure_default_settings(button1, 12)
    configure_default_settings(button2,12)
    configure_default_settings(label, 12)
    configure_default_settings(label3, 12)
    configure_default_settings(label2, 12)
    configure_default_settings(label4, 12)
    configure_default_settings(button3,12)
    label.grid()
    button.grid()
    label2.grid()
    button1.grid()
    label3.grid()
    button2.grid()
    label4.grid()
    button3.grid()



root= Tk()

frame = tk.Frame(root)
root.title("ISI company recruitment")

root.configure(bg=active_scheme['main bg'])

button2=Button(frame,text="Administrator log in",command=login)
button3=Button(frame,text="job seeking",command=loginuser)
button1=Button(frame,text="Quit",command=root.destroy)

label=tk.Label(frame,text="")
label1=tk.Label(frame,text="")
frame.grid(padx=100,pady=100)


#CONFIGURING
configure_default_settings(button2, 15)
configure_default_settings(button3, 15)
configure_default_settings(button1, 15)
configure_default_settings(label,5)
configure_default_settings(label1,5)
configure_default_settings(frame,1)

#GRIDING
button2.grid(row=1,column=0,columnspan=2,padx=5,pady=(10, 0))
label.grid(row=2,column=0,columnspan=2,padx=5,pady=(10, 0))
button3.grid(row=1,column=10,columnspan=2,padx=5,pady=(10, 0))
label1.grid(row=3,column=0,columnspan=2,padx=5,pady=(10, 0))
button1.grid(row=4,column=2,columnspan=2,padx=5,pady=(10, 0))

root.mainloop()
