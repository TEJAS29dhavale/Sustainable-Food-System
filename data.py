from tkinter import *
from tkinter import PhotoImage
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from tkinter import ttk
import mysql.connector
import math
import pandas as pd
import csv


class home:
    F1='false'
    F2='false'
    F3='false'

    def showgraph(self):
                if self.F1 =='true':
                    self.Frame1.destroy()
                    self.F1='false'
                elif self.F2 == 'true':
                    self.Frame2.destroy()
                    self.F2='false'
                elif self.F3 == 'true':
                    self.Frame3.destroy()
                    self.F3='false'
                self.Frame1 = Frame(self.root)
                self.Frame1.place(x=90, y=130)
                self.Frame1.configure(relief=GROOVE)
                self.Frame1.configure(borderwidth="2")
                self.Frame1.configure(relief=GROOVE)
                self.Frame1.configure(background="#9dcdf8",bd=0)
                self.Frame1.configure(highlightcolor="#af2222")
                self.Frame1.configure(width=1400, height=650)
                
                self.histo ='false'
                self.pie='false'
                self.sca='false'
                
                
                vegetables=[]
                fruits =[]
                grains = []
                with open('.vscode/Project/Sheet1.csv', ) as csvfile:
                    reader = csv.DictReader(csvfile)
                    
                    for row in reader:
                        vegetables.append(int(row['Vegitables']))  #assuming the first
                        fruits.append(int(row['Fruits']))
                        grains.append(int(row['Grains']))
                    print(vegetables)
                    print(grains)
                    print(fruits)
                def getvalues(vegetables,fruits,grains):
                    if self.histo =='true' or self.pie=='true' or self.sca=='true':
                        for widget in self.Frame1.winfo_children():
                            widget.destroy()
                           #clearing the frame before plotting new graph
                    kg=[]
                    for i in range(4):
                        kg.append(vegetables[i]+fruits[i]+grains[i]/3) 
                    v1 =vegetables[0]+vegetables[1]+vegetables[2]+vegetables[3]
                    v=v1/4
                    f1 =fruits[0]+fruits[1]+fruits[2]+fruits[3]
                    f=f1/4
                    g1 =grains[0]+grains[1]+grains[2]+grains[3]
                    g=g1/4
                    sqr1=v**2
                    sqr11=vegetables[0]**2+vegetables[1]**2+vegetables[2]**2+vegetables[3]**2
                    sqr111=sqr11/4-sqr1
                    sqr2=f**2
                    sqr22=fruits[0]**2+fruits[1]**2+fruits[2]**2+fruits[3]**2
                    sqr222=sqr22/4-sqr2
                    
                    s1q=g**2
                    s2q=grains[0]**2+grains[1]**2+grains[2]**2+grains[3]**2
                    s3q=s2q/4-s1q
                    sd=math.sqrt(sqr111)
                    sd2=math.sqrt(sqr222)
                    s3d=math.sqrt(s3q)
                    valu=v1*20+f1*40+g1*14
                    self.lab13 = tk.Label(self.Frame1,text="Total Population :"+str('1000'),font=16,bg="#31014f",fg="#ffffff")
                    self.lab14 = tk.Label(self.Frame1,text="Target Food Production :"+str('10000'),font=16,bg="#31014f",fg="#ffffff")
                    self.lab15 = tk.Label(self.Frame1,text="Total Value production :"+str(valu)+'rs',font=16,bg="#31014f",fg="#ffffff")
                    self.lab1 = tk.Label(self.Frame1,text="Yearly Mean of Vegetables :"+str(v),font=16,bg="#31014f",fg="#ffffff")
                    self.lab2 = tk.Label(self.Frame1,text="Yearly Mean of Fruits :"+str(f),font=16,bg="#31014f",fg="#ffffff")
                    self.lab3 = tk.Label(self.Frame1,text="Yearly Mean of Grains :"+str(g),font=16,bg="#31014f",fg="#ffffff")
                    self.lab4 = tk.Label(self.Frame1,text="Standard Deviation Veg:"+str(sd),font=16,bg="#31014f",fg="#ffffff")
                    self.lab5 = tk.Label(self.Frame1,text="Standard Deviation Fru:"+str(sd2),font=16,bg="#31014f",fg="#ffffff")
                    self.lab6 = tk.Label(self.Frame1,text="Standard Deviation Gra:"+str(s3d),font=16,bg="#31014f",fg="#ffffff")
                    
                    self.lab1.place(x=930,y=260)
                    self.lab2.place(x=930,y=300)
                    self.lab3.place(x=930,y=340)
                    self.lab4.place(x=930,y=380)
                    self.lab5.place(x=930,y=420)
                    self.lab6.place(x=930,y=460)
                    self.lab13.place(x=930,y=40)
                    self.lab14.place(x=930,y=80)
                    self.lab15.place(x=930,y=120)
                    
                   
                    
                    
                    def autolabel(reactangle_group):
                        for rect in reactangle_group:
                            height = rect.get_height()
                            ax.annotate(str(height),xy = (rect.get_x() + rect.get_width()/2,height),
                            ha = 'center',
                            xytext=(0,3),textcoords='offset points',
                            color = 'grey') 
    
                    months = ['Jan-Mar','Apr-Jun','Jul-Sep','Oct-Dec']
                  
    
                    fig,ax = plt.subplots(figsize=(9,5))
                    canvas = (FigureCanvasTkAgg(fig, master = self.Frame1))
                    canvas.get_tk_widget().place(x=20, y=20)
    
                    width = 0.2
                    x_veg = [x - width for x in range(len(vegetables))]
                    x_fru = [x for x in range(len(fruits))]
                    x_gra = [x + width for x in range(len(grains))]
    
                    rect1 = ax.bar(x_veg, vegetables, width, label='Vegetables', color = '#7bf95f')
                    rect2 = ax.bar(x_fru, fruits, width, label='Fruits', color = '#f6ae65')
                    rect3 = ax.bar(x_gra, grains, width, label='Grains', color = '#af816d')
                    ax.plot(months,kg, label='Stat', color = '#420054', marker = 'o')
                    
    
                    ax.set_title("Production analysis")
                    ax.set_ylabel("Total Kilograms")
                    ax.set_xlabel("Total Duration")
                    ax.legend(loc=(1.0,0.9))
                    plt.tight_layout()
    
                    autolabel(rect1)
                    autolabel(rect2)
                    autolabel(rect3)
                    
                    plt.plot(months,kg)
                    plt.show()
                    
                    self.histo='true'
                    return sd,sd2,s3d
                  
                def getpie(vegetables,fruits,grains):
                    if self.histo =='true' or self.pie=='true' or self.sca=='true':
                        for widget in self.Frame1.winfo_children():
                            widget.destroy()
                          #clearing the frame before plotting new graph
                    k= ['Vegetables', 'Grains', 'Fruits']
                    t=[]  
                    v1 =vegetables[0]+vegetables[1]+vegetables[2]+vegetables[3]
                    v=v1/4
                    t.append(v1)
                
                    f1 =fruits[0]+fruits[1]+fruits[2]+fruits[3]
                    f=f1/4
                    t.append(f1)
                    
                    g1=grains[0]+grains[1]+grains[2]+grains[3]
                    g=g1/4
                    t.append(g1)
                    sqr1=v**2
                    sqr11=vegetables[0]**2+vegetables[1]**2+vegetables[2]**2+vegetables[3]**2
                    sqr111=sqr11/4-sqr1
                    sqr2=f**2
                    sqr22=fruits[0]**2+fruits[1]**2+fruits[2]**2+fruits[3]**2
                    sqr222=sqr22/4-sqr2
                    
                    s1q=g**2
                    s2q=grains[0]**2+grains[1]**2+grains[2]**2+grains[3]**2
                    s3q=s2q/4-s1q
                    sd=math.sqrt(sqr111)
                    sd2=math.sqrt(sqr222)
                    s3d=math.sqrt(s3q)
                  
                    v=v1/10000*100
                    f=f1/10000*100
                    g=g1/10000*100
                    valu=v1*20+f1*40+g1*14
                    fig,ax = plt.subplots(figsize=(9,6))
                    canvas = (FigureCanvasTkAgg(fig, master = self.Frame1))
                    canvas.get_tk_widget().place(x=20, y=20)
                    
                    
    
                    ax.set_title("Production analysis")
                    
                    ax.set_xlabel("Total Percentages")
                    ax.legend(title='Items', loc=(1.0,0.9))
                    plt.tight_layout()
                    ax.pie(t,labels=k,autopct="%2.1f%%")
                    
                    
                    self.lab13 = tk.Label(self.Frame1,text="Total Population :"+str('1000'),font=16,bg="#31014f",fg="#ffffff")
                    self.lab14 = tk.Label(self.Frame1,text="Target Food Production :"+str('10000'),font=16,bg="#31014f",fg="#ffffff")
                    self.lab15 = tk.Label(self.Frame1,text="Total Value production :"+str(valu)+'rs',font=16,bg="#31014f",fg="#ffffff")
                    self.lab7 = tk.Label(self.Frame1,text="Yearly Percentage of Vegetables :"+str(v),font=16,bg="#31014f",fg="#ffffff")
                    self.lab8 = tk.Label(self.Frame1,text="Yearly Percentage of Fruits :"+str(f),font=16,bg="#31014f",fg="#ffffff")
                    self.lab9 = tk.Label(self.Frame1,text="Yearly Percentage of Grains :"+str(g),font=16,bg="#31014f",fg="#ffffff")
                    self.lab4 = tk.Label(self.Frame1,text="Standard Deviation Veg:"+str(sd),font=16,bg="#31014f",fg="#ffffff")
                    self.lab5 = tk.Label(self.Frame1,text="Standard Deviation Fru:"+str(sd2),font=16,bg="#31014f",fg="#ffffff")
                    self.lab6 = tk.Label(self.Frame1,text="Standard Deviation Gra:"+str(s3d),font=16,bg="#31014f",fg="#ffffff")
                    self.lab7.place(x=930,y=260)
                    self.lab8.place(x=930,y=300)
                    self.lab9.place(x=930,y=340)
                    self.lab4.place(x=930,y=380)
                    self.lab5.place(x=930,y=420)
                    self.lab6.place(x=930,y=460)
                    self.lab13.place(x=930,y=40)
                    self.lab14.place(x=930,y=80)
                    self.lab15.place(x=930,y=120)
                    
                    plt.pie(t,labels=k,autopct="%2.1f%%")
                    
                    plt.legend(title='Items', loc=(1.0,0.9))
                    plt.show()
                    self.pie='true'
                def getsca(vegetables,fruits,grains):
                    if self.histo =='true' or self.pie=='true' or self.sca=='true':
                        for widget in self.Frame1.winfo_children():
                            widget.destroy()
                          #clearing the frame before plotting new graph
                    t=[]  
                    v1 =vegetables[0]+vegetables[1]+vegetables[2]+vegetables[3]
                    t.append(v1)
                
                    f1 =fruits[0]+fruits[1]+fruits[2]+fruits[3]
                    t.append(f1)
                    
                    g1=grains[0]+grains[1]+grains[2]+grains[3]
                    t.append(g1)
                    
                    v=v1/4
                    f=f1/4
                    g=g1/4
                    valu=v1*20+f1*40+g1*14
                    months = ['Jan-Mar','Apr-Jun','Jul-Sep','Oct-Dec']
                    
                    fig,ax = plt.subplots(figsize=(9,6))
                    canvas = (FigureCanvasTkAgg(fig, master = self.Frame1))
                    canvas.get_tk_widget().place(x=20, y=20)
                    
                    
                
                    ax.set_title("Production analysis")
                    ax.set_ylabel("Total Kilograms")
                    ax.set_xlabel("Total Duration")
                    ax.legend(["Vegetables","Fruits","Grains"],title='Items' ,loc=(1.0,0.9))
                    
                    ax.scatter(months,vegetables)  
                    ax.scatter(months,fruits)
                    ax.scatter(months,grains)
                    
                    
                   
                    self.lab13 = tk.Label(self.Frame1,text="Total Population :"+str('1000'),font=16,bg="#31014f",fg="#ffffff")
                    self.lab14 = tk.Label(self.Frame1,text="Target Food Production :"+str('10000'),font=16,bg="#31014f",fg="#ffffff")
                    self.lab15 = tk.Label(self.Frame1,text="Total Value production :"+str(valu)+'rs',font=16,bg="#31014f",fg="#ffffff")
                    self.lab10 = tk.Label(self.Frame1,text="Mean Data Points of Vegetables :"+str(v),font=16,bg="#31014f",fg="#ffffff")
                    self.lab11= tk.Label(self.Frame1,text="Mean Data Points of Fruits :"+str(f),font=16,bg="#31014f",fg="#ffffff")
                    self.lab12= tk.Label(self.Frame1,text="mean Data Points of Grains :"+str(g),font=16,bg="#31014f",fg="#ffffff")
                    self.lab10.place(x=930,y=260)
                    self.lab11.place(x=930,y=300)
                    self.lab12.place(x=930,y=340)
                    self.lab13.place(x=930,y=40)
                    self.lab14.place(x=930,y=80)
                    self.lab15.place(x=930,y=120)
                    
                    plt.scatter(months,fruits,color='orange')
                    plt.scatter(months,vegetables,color='green')
                    plt.scatter(months,grains, color="blue") 
                    plt.title("Scatterplot")
                    plt.xlabel("Months")
                    plt.ylabel("Kilograms")
                    plt.legend(["Vegetables","Fruits","Grains"],title='Items', loc=(1.0,0.9))
                    plt.show()
                    
                    self.sca='true'
                
                self.button = tk.Button(self.root, text="Show HistoGraph",font=40, bg="#c534ed", fg="white", bd=0, activebackground="#1D1042", activeforeground="#1D1042",command=lambda:getvalues(vegetables,fruits,grains))
                self.button.place_configure(x=600, y=100, height=40, width=200)
                self.button1 = tk.Button(self.root, text="Show Pie Graph",font=40, bg="#c534ed", fg="white", bd=0, activebackground="#1D1042", activeforeground="#1D1042",command=lambda:getpie(vegetables,fruits,grains))
                self.button1.place_configure(x=830, y=100, height=40, width=200)
                self.button2 = tk.Button(self.root, text="Show Scatter Graph",font=40, bg="#c534ed", fg="white", bd=0, activebackground="#1D1042", activeforeground="#1D1042",command=lambda:getsca(vegetables,fruits,grains))
                self.button2.place_configure(x=1060, y=100, height=40, width=200)
                
                self.F1='true'

    def showtree(self):
                if self.F1 =='true':
                    self.Frame1.destroy()
                    self.button.destroy()
                    self.button1.destroy()
                    self.button2.destroy()
                    self.F1='false'
                elif self.F2 == 'true':
                    self.Frame2.destroy()
                    self.F2='false'
                elif self.F3 == 'true':
                    self.Frame3.destroy()
                    self.F3='false'
                self.Frame2 = Frame(self.root)
                self.Frame2.place(x=130, y=160)
                self.Frame2.configure(relief=GROOVE)
                self.Frame2.configure(borderwidth="2")
                self.Frame2.configure(relief=GROOVE)
                self.Frame2.configure(background="#e0ffde",bd=0, )
                self.Frame2.configure(highlightcolor="#af2222")
                self.Frame2.configure(width=1300, height=600)
                
                connection = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="hv")
                
                if connection.is_connected():
                    self.la4 = tk.Label(self.Frame2,text="The connection has established to hv database",font=20,bg="#e0ffde",fg="#31014f")
                    self.la4.place(x=200,y=20)
                    print("The connection has established to hv database")
                else:
                    self.la4 = tk.Label(self.Frame2,text='Database Not Connected',font=25,bg="#e0ffde", fg="#af2222")
                    self.la4.place(x=200,y=20)
                
                    
                self.la3 = tk.Label(self.Frame2,text='Food Data',font=25,bg="#e0ffde", fg="#1c8b16")
                self.la3.place(x=50,y=20)
                e2 = tk.Entry(self.Frame2,width=20,justify=CENTER,font=('Arial',15))
                e2.place_configure(x=1000,y=100)
                e3 = tk.Entry(self.Frame2,width=20,justify=CENTER,font=('Arial',15))
                e3.place_configure(x=1000,y=150)
                e4 = tk.Entry(self.Frame2,width=20,justify=CENTER,font=('Arial',15))
                e4.place_configure(x=1000,y=300)
               
                self.la1 = tk.Label(self.Frame2,text='Food Type',font=20,bg="#e0ffde",fg="#31014f")
                self.la1.place(x=880,y=100)
                self.la2 = tk.Label(self.Frame2,text='Name',font=20,bg="#e0ffde",fg="#31014f")
                self.la2.place(x=880,y=150)
                self.la5 = tk.Label(self.Frame2,text='Id No',font=25,bg="#e0ffde", fg="#31014f")
                self.la5.place(x=880,y=300)
                
                def insert(e2,e3):
                        
                        type =e2.get()
                        name = e3.get()
                        connection = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="hv")
                        mycursor = connection.cursor()
                        mycursor.execute("INSERT INTO hvdata (FName,Type) VALUES(%s,%s)",(type,name))
                        connection.commit()
                        
                        
                def delete(e4):
                        id=int(e4.get())
                        connection = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="hv")
                        mycursor = connection.cursor()
                        mycursor.execute("DELETE FROM hvdata WHERE id='%d'"%(id))
                        connection.commit()
                        
                
                 
                
                Frame1dis = Frame(self.Frame2)
                Frame1dis.place(x=20, y=70)
                Frame1dis.configure(relief=GROOVE)
                Frame1dis.configure(borderwidth="2")
                Frame1dis.configure(relief=GROOVE)
                Frame1dis.configure(background="#9dcdf8",bd=0)
                Frame1dis.configure(highlightcolor="#af2222")
                Frame1dis.configure(width=700, height=550)

                def display():
                    connection = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="hv")
                    mycursor = connection.cursor()
                    mycursor.execute("SELECT * FROM hvdata")
                    resu = mycursor.fetchall()
                    listbox = tk.Listbox(Frame1dis)
                    listbox.pack()
                    for data in resu:
                        print(data)
                        listbox.insert(tk.END, data)
                   
                           

                self.button = tk.Button(self.Frame2, text="Insert product",font=40, bg="#c534ed", fg="white", bd=0, activebackground="#1D1042", activeforeground="#1D1042",command=lambda:insert(e2,e3))
                self.button.place_configure(x=1000, y=220, height=40, width=215)
                
                self.button = tk.Button(self.Frame2, text="Delete product",font=40, bg="#c534ed", fg="white", bd=0, activebackground="#1D1042", activeforeground="#1D1042",command=lambda:delete(e4))
                self.button.place_configure(x=1000, y=350, height=40, width=215)
                
                self.buttond = tk.Button(self.Frame2, text="Display Data",font=40, bg="#c534ed", fg="white", bd=0, activebackground="#1D1042", activeforeground="#1D1042",command=lambda:display())
                self.buttond.place_configure(x=1000, y=450, height=40, width=215)
                
               


                
                self.F2='true'
                connection.close()
                return self.F2
                
               
                

    def showgreeh(self):
                if self.F1 =='true':
                    print("frame1 destroyed")
                    self.Frame1.destroy()
                    self.button.destroy()
                    self.button1.destroy()
                    self.button2.destroy()
                    self.F1='false'
                elif self.F2 == 'true':
                    self.Frame2.destroy()
                    print("frame2 destroyed")
                    self.F2='false'
                elif self.F3 == 'true':
                    self.Frame3.destroy()
                    print("frame3 destroyed")
                    self.F3='false'
                self.Frame3 = Frame(self.root)
                self.Frame3.place(x=130, y=160)
                self.Frame3.configure(relief=GROOVE)
                self.Frame3.configure(borderwidth="2")
                self.Frame3.configure(relief=GROOVE)
                self.Frame3.configure(background="#fff0dc",bd=0, )
                self.Frame3.configure(highlightcolor="#af2222")
                self.Frame3.configure(width=1300, height=600)
                
                connection = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="hv")
                
                if connection.is_connected():
                    self.label4 = tk.Label(self.Frame3,text="The connection has established to hv database",font=20,bg="#e0ffde",fg="#31014f")
                    self.label4.place(x=200,y=20)
                    print("The connection has established to hv database")
                else:
                    self.label4 = tk.Label(self.Frame3,text='Database Not Connected',font=25,bg="#e0ffde", fg="#af2222")
                    self.label4.place(x=200,y=20)
                
                    
                self.label3 = tk.Label(self.Frame3,text='Food Data',font=25,bg="#e0ffde", fg="#1c8b16")
                self.label3.place(x=50,y=20)
                     



                self.label5 = tk.Label(self.Frame3,text='Envoirnment',font=25,bg="#fff0dc", fg="#1c8b16")
                self.label5.place(x=800,y=100)
                
                self.label6 = tk.Label(self.Frame3,text=' GreneHouse Id',font=25,bg="#fff0dc", fg="#1c8b16")
                self.label6.place(x=800,y=250)

                en = tk.Entry(self.Frame3,width=20,justify=CENTER,font=('Arial',15))
                en.place_configure(x=950,y=100)

                de = tk.Entry(self.Frame3,width=20,justify=CENTER,font=('Arial',15))
                de.place_configure(x=950,y=250)
                
                
                
                def sertg(en):
                        grt= en.get()
                        cap=100
                        connection = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="hv")
                        mycursor = connection.cursor()
                        mycursor.execute("INSERT INTO gr (green, capacity) VALUES(%s,%s)",(grt,cap))
                        connection.commit()
                        connection.close()
                        
                def eteg(de):
                        Id=int(de.get())
                        connection = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="hv")
                        mycursor = connection.cursor()
                        mycursor.execute("DELETE FROM gr WHERE id='%d'"%(Id))
                        connection.commit()
                        connection.close()
                
                
                button = tk.Button(self.Frame3, text="Add Green House",font=20, bg="#c534ed", fg="white", bd=0, activebackground="#1D1042", activeforeground="#1D1042",command=lambda:sertg(en))
                button.place_configure(x=950, y=150, height=40, width=240)

                button1 = tk.Button(self.Frame3, text="Delete Green House",font=20, bg="#c534ed", fg="white", bd=0, activebackground="#1D1042", activeforeground="#1D1042",command=lambda:eteg(de))
                button1.place_configure(x=950, y=300, height=40, width=240)

               

                self.F3 = 'true'
                return self.F3
                


    
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1000x600")
        self.root.wm_title("HEALTH VERSE")
        self.root.configure(background="#f9e9ff")
        #self.mainubar = tk.Menu(self.root)
        #self.stat = tk.Menu(self.mainubar,tearoff=0)
        #self.treef = tk.Menu(self.mainubar,tearoff=0)
        #self.greenh = tk.Menu(self.mainubar,tearoff=0)

        #self.mainubar.add_cascade(menu=self.stat,label="Stat",)
        #self.mainubar.add_cascade(menu=self.treef,label="Tree",)
        #self.mainubar.add_cascade(menu=self.greenh,label="Greh",)
        #self.root.config(menu=self.mainubar)

        #self.stat.add_command(command=self.showgraph)

        self.topFrame = tk.Frame( bg="#1D1042")
        self.topFrame.place_configure(height=800, width=80)

        self.label = tk.Label(text="Sustainable Food System", font="Bahnschrift 25", bg="#f9e9ff", fg="#1D1042")
        self.label.place_configure(x=100, y=10)

        self.Logo = PhotoImage(file=".vscode/Project/LOGO.png",)
        self.logo = self.Logo.subsample(1, 1)
        self.homeLabel = tk.Label( image=self.logo, bg="#f9e9ff")
        self.homeLabel.place(x=1360, y=10, height=90, width=90, )

        self.stat = PhotoImage(file=".vscode/Project/gaugeperfor.png")
        self.sta = self.stat.subsample(2, 2)
        self.tree = PhotoImage(file=".vscode/Project/hierarchy-structuretree.png")
        self.tre = self.tree.subsample(2, 2)
        self.gree = PhotoImage(file=".vscode/Project/spider-diagramhome.png")
        self.gre = self.gree.subsample(2, 2)
        self.log = PhotoImage(file=".vscode/Project/Iconlogin.png")
        self.lo = self.log.subsample(2, 2)  

        self.button = tk.Button(self.root, text="Stat", image =self.sta, bg="#1D1042", fg="white", bd=0, activebackground="#1D1042", activeforeground="#1D1042",command=self.showgraph)
        self.button.place_configure(x=10, y=100, height=60, width=60)

        self.button = tk.Button(self.root, text="Stat", image =self.tre, bg="#1D1042", fg="white", bd=0, activebackground="#1D1042", activeforeground="#1D1042",command=self.showtree)
        self.button.place_configure(x=10, y=170, height=60, width=60)

        self.button = tk.Button(self.root, text="Stat", image =self.gre, bg="#1D1042", fg="white", bd=0, activebackground="#1D1042", activeforeground="#1D1042",command=self.showgreeh)
        self.button.place_configure(x=10, y=240, height=60, width=60)

        self.button = tk.Button(self.root, text="Stat", image =self.lo, bg="#1D1042", fg="white", bd=0, activebackground="#1D1042", activeforeground="#1D1042")
        self.button.place_configure(x=10, y=310, height=60, width=60)
        self.root.mainloop()      
        
home()