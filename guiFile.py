""" This file has all of the code for running the gui
    and responding to user input
"""
import time
import tkinter
from tkinter import *
import globVar
from tkinter import ttk
from tkinter import font
import dbStuff
import device

def main_gui():
    # function to use one scroller bar for all tabs
    def yview(self, *args):
        self.blackTab.yview(*args)
        self.whiteTab.yview(*args)
        self.greyTab.yview(*args)

    #function for when "move to blacklist" button is pressed
    def move_to_blacklist():
        #get selection
        index = greyTab.curselection()[0]
        selection=greyTab.get(index)

        #remove from grey tab, add to black tab
        greyTab.delete(index)
        blackTab.insert(tkinter.END, selection)

        #remove from grey data table, add to black data table
        device_info = selection.split(" ",1)
        obj = device.Device(device_info[0],device_info[1])
        dbStuff.remove_from_table(2,obj)
        dbStuff.add_to_table(0,obj)

    #function for when "move to allowed list" button is pressed
    def move_to_approved():
        #get selection
        index = greyTab.curselection()[0]
        selection=greyTab.get(index)

        #remove from grey tab, add to black tab
        greyTab.delete(index)
        whiteTab.insert(tkinter.END, selection)
        # 4. remove from current sql table
        # 5. add to approved sql table

        #remove from grey data table, add to allowed data table
        device_info = selection.split(" ",1)
        obj = device.Device(device_info[0],device_info[1])
        dbStuff.remove_from_table(2,obj)
        dbStuff.add_to_table(1,obj)

    #make main window
    gui = tkinter.Tk()
    gui.title("MFA for Wi-Fi Connection")
    gui.geometry("400x250")

    #make frames for tabs and buttons
    tabFrame = ttk.Frame(gui,width=400)
    buttonFrame = ttk.Frame(gui,width=200)
    n = ttk.Notebook(tabFrame,width=400)

    #add addresses/names from grey list into grey tab list
    textFont = font.Font(size=10)
    greyTab = Listbox(tabFrame,font=textFont)
    greyTab.pack()
    for d in globVar.greyList:
        str = d.macAddress + " " + d.name
        greyTab.insert(END,str)

    blackTab = Listbox(tabFrame,font=textFont)
    blackTab.pack()
    for d in globVar.blackList:
        str = d.macAddress + " " + d.name
        blackTab.insert(END,str)

    whiteTab = Listbox(tabFrame,font=textFont)
    whiteTab.pack()
    for d in globVar.allowedList:
        str = d.macAddress + " " + d.name
        whiteTab.insert(END,str)

    #make scrollbar
    scroller = Scrollbar(tabFrame,command=yview)
    scroller.pack(side=RIGHT,fill=Y)
    greyTab.config(yscrollcommand=scroller.set)
    blackTab.config(yscrollcommand=scroller.set)
    whiteTab.config(yscrollcommand=scroller.set)

    #add tabs to notebook
    n.add(greyTab,text='Grey List')
    n.add(blackTab,text='Black List')
    n.add(whiteTab,text='Approved List')

    #create buttons to move to approved list / black list
    greyToWhite = Button(buttonFrame,text="Move to approved list",width=16,command=move_to_approved)
    greyToWhite.pack(anchor='ne')

    greyToBlack = Button(buttonFrame,text="Move to black list",width=16,command=move_to_blacklist)
    greyToBlack.pack(anchor="ne")

    #final packing
    n.pack(expand=1, fill='both',anchor='nw')
    tabFrame.pack(side=TOP)
    buttonFrame.pack(side=BOTTOM)

    gui.mainloop()
