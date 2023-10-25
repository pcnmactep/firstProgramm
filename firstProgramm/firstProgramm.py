from ast import Str
from calendar import c
from msilib import Table
from msilib.schema import File
from re import L
from sre_parse import State
from tkinter import *
from tkinter import filedialog
from tokenize import String
import os
from datetime import datetime
from turtle import color





def AddField(event):
    def Final(event):
        name=nameEntry.get()
        country = countryEntry.get()
        people = peopleEntry.get()
        fn = open("bd.txt", 'a')
        fn.write(name+";"+country+";"+people+";"+'\n')
        fn.close()
        addPanel.destroy()


    #print "Adding proccess"
    addPanel = Tk()
    addPanel.title("add in file")

    nameLabel = Label(addPanel, text="Enter name your city")
    nameLabel.grid(row=1,column=1)
    nameLabel.place()
    nameEntry = Entry(addPanel)
    nameEntry.grid(row=1,column=2)
    nameEntry.place()

    countryLabel = Label(addPanel, text="Enter country")
    countryLabel.grid(row=2,column=1)
    countryLabel.place()
    countryEntry = Entry(addPanel)
    countryEntry.grid(row=2,column=2)
    countryEntry.place()

    peopleLabel=Label(addPanel, text="How much people in your city")
    peopleLabel.grid(row=3,column=1)
    peopleLabel.place()
    peopleEntry = Entry(addPanel)
    peopleEntry.grid(row=3,column=2)
    peopleEntry.place()

    addButtonFinal = Button(addPanel,text="Final")
    addButtonFinal.grid(row=4,column = 1)
    addButtonFinal.bind("<Button-1>", Final)
    addButtonFinal.place()

    addPanel.mainloop()


def delField(event):
    def msg(event):
        msgPanel = Tk()
        msgPanel.title("succesful")
        Label(msgPanel,text="Successful deliteng").grid(row=1,column=1)

    def DeleteField(event):
        name=nameEntry.get()

        fn=open("bd.txt","r")
        en=open("temp.txt","w")
        chck=False

        while(True) :
           
           a=fn.readline()
           sr=a.split(";")

           if(sr[0]!=name): en.write(a)
           else: chck=True

           if(a==-1 or a==''):break
        
        fn.close()
        en.close()
        os.remove("oldBD.txt")
        os.rename("bd.txt","oldBD.txt")
        os.rename("temp.txt","bd.txt")
        if(chck):msg("lmao")

        delPanel.destroy()

    #print "Adding proccess"
    delPanel = Tk()
    delPanel.title("delete in file")

    nameLabel = Label(delPanel, text = "name")
    nameLabel.grid(column=1,row=1)
    nameLabel.place()

    nameEntry = Entry(delPanel)
    nameEntry.grid(row=2,column=1)
    nameEntry.place()
    
    addButtonDelete = Button(delPanel,text="Delete")
    addButtonDelete.grid(row=2,column = 2)
    addButtonDelete.bind("<Button-1>", DeleteField)
    addButtonDelete.place()

    #addPanel.mainloop()

def searchField(event):

    searchPanel=Tk()
    searchPanel.title("search Panel")

    
    def clearTable():
        j=0
        joject=searchPanel.winfo_children()
        for i in joject:
            if(j>3):i.destroy()
            else:j+=1

    def search(event):
        clearTable()
        fn=open("bd.txt","r")
        i=4
        while(True):
            a=fn.readline()
            sr=a.split(";")
            if(sr[0].lower()==searchEnter.get().lower()):
                Label(searchPanel,text="country name").grid(row=3,column=1)
                Label(searchPanel,text="central city").grid(row=3,column=2)
                Label(searchPanel,text="population").grid(row=3,column=3)
                j=0
                
                for info in sr:
                    j+=1
                    Label(searchPanel,text=info).grid(row=i,column=j)
                i+=1
                
                

            if(a==-1 or a==''):break

    
    Label(searchPanel,text="enter name").grid(row=1,column=1)

    searchEnter=Entry(searchPanel)
    searchEnter.grid(row=2,column=1)

    searchButton=Button(searchPanel,text="search")
    searchButton.grid(row=2,column=2)
    searchButton.bind("<Button-1>", search)

    searchPanel.mainloop()




def seeAll(event):

    seePanel=Tk()
    seePanel.title("table with all Data")
    refreshButton=Button(seePanel,text="refresh")
    
    

    def default():
        fn=open("bd.txt","r")
        Label(seePanel,text="Name Country").grid(row=1,column=1)
        Label(seePanel,text="Central city").grid(row=1,column=2)
        Label(seePanel,text="Population").grid(row=1,column=3)
        j=1
        while(True):
            j+=1;
            a=fn.readline()

            if(a==-1 or a==''):break

            sr=a.split(";")     
            i=0
            for info in sr:
                i+=1
                Label(seePanel,text=info).grid (row=j,column=i )

    def clearTable(event):
        j=0
        joject=seePanel.winfo_children()
        for i in joject:
            if(j>0):i.destroy()
            else:j+=1
        default()
        
    default()

    refreshButton.grid()
    refreshButton.bind("<Button-1>",clearTable)

root = Tk("nice soft from russia")
root.title("im work but im tired")

addBut=Button(root, text = "add")
addBut.bind("<Button-1>", AddField)
addBut.grid(row=1,column = 1)
addBut.place();

delButton=Button(root, text = "Delete")
delButton.grid(row=1,column = 2)
delButton.bind("<Button-1>",delField)
delButton.place()
searchButton=Button(root, text = "Check in file")
searchButton.grid(row=1,column = 3)
searchButton.bind("<Button-1>",searchField)
searchButton.place()

seaAll=Button(root, text = "See all")
seaAll.grid(row=1,column = 4)
seaAll.bind("<Button-1>",seeAll)
seaAll.place()


#2.	Создать стек целых чисел на основе статического массива. Реализовать методы : Добавить элемент, удалить элемент, вершина стека.
def questionTwo(event):
    q2 = Tk()
    q2.title("woaw i think its label not reading somebody")

    try:import stepBrotherImSTACK as stackModule
    except:q2.destroy()

    stack = stackModule.stack()

    enter = Entry(q2)
    enter.grid(row=1,column=1)
    enter.place()

    def addInStack(event):
        stack.push(int(enter.get()))
        pass

    def delInStack(event):
        stack.pop()
        pass

    def seeInStack(event):
        enter.__setitem__(str,stack.get())
        pass

    addButton  = Button (q2, text="adding")
    addButton.grid(row=1,column=2)
    addButton.bind("<Button-1>", addInStack)
    addButton.place()

    delButton  = Button (q2, text="delete")
    delButton.grid(row=1,column=3)
    delButton.bind("<Button-1>", delInStack)
    delButton.place()

    seeButton  = Button (q2, text="see")
    seeButton.grid(row=1,column=4)
    seeButton.bind("<Button-1>", seeInStack)
    seeButton.place()


    


    pass

questionTwoButton=Button(root, text="example 2")
questionTwoButton.grid(row=2,column=1)
questionTwoButton.bind("<Button-1>",questionTwo)
questionTwoButton.place()

root.mainloop()