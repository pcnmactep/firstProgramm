#—оздать запись —трана следующей структуры: Ќазвание, столица, количество населени€. Ќаписать программу, реализующую следующее меню: 
#Х	добавить элемент в файл
#Х	удалить элемент из файла
#Х	принадлежность элемента файлу
#Х	вывод всех записей на экран



from ast import Str
from calendar import c
from msilib import Table
from msilib.schema import File
from re import L
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
        #fn = filedialog.SaveAs(root, filetypes = [('*.txt files', '.txt')]).show()
        #if fn == '':
        # return  
        #if not fn.endswith(".txt"):
        #    fn+=".txt"
        #open(fn, 'wt').write()

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

    resultLabel=Entry(searchPanel,background=color(175f, 186.0, 73.0))   
    resultLabel.grid(row=5,column=1)
    

    def search(event):
        fn=open("bd.txt","r")
        while(True):
            a=fn.readline()
            sr=a.split(";")
            if(sr[0]==searchEnter.get()):
                resultLabel.delete(0,END)
                resultLabel.insert(0,a)

            if(a==-1 or a==''):break


    

    Label(searchPanel,text="enter name").grid(row=1,column=1)

    searchEnter=Entry(searchPanel)
    searchEnter.grid(row=2,column=1)

    searchButton=Button(searchPanel,text="search")
    searchButton.grid(row=2,column=2)
    searchButton.bind("<Button-1>", search)

    searchPanel.mainloop()



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

Button(root, text = "See all").grid(row=1,column = 4)



#Button(root,text = "name").grid (row=2,column=1)
#Button(root,text = "country").grid (row=2,column=2)
#Button(root,text = "people").grid (row=2,column=3)

root.mainloop()