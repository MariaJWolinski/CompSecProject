""" This file has all of the code for running the gui
    and responding to user input
"""
import time
import Tkinter
from Tkinter import *
import globVar
import ttk


def main_gui():
    print("do the gui thing!")
    # time.sleep(10)

    gui = Tkinter.Tk()

    # widgets added here
    gui.title("Kick 'em off your Wifi")
    gui.geometry("600x600")

    n = ttk.Notebook(gui)
    greyTab = ttk.Frame(n)
    blackTab = ttk.Frame(n)
    allowedTab = ttk.Frame(n)

    n.add(greyTab, text='Grey List')
    n.add(blackTab, text='Black List')
    n.add(allowedTab, text='Allowed List')

    i = 0
    for d in globVar.greyList:
        l1 = Label(greyTab, text=d.macAddress, padx=5, pady=5)
        l1.grid(column=0, row=i)
        l2 = Label(greyTab, text=d.name, padx=5, pady=5)
        l2.grid(column=1, row=i)
        i += 1

    i = 0
    for d in globVar.blackList:
        l1 = Label(blackTab, text=d.macAddress, padx=5, pady=5)
        l1.grid(column=0, row=i)
        l2 = Label(blackTab, text=d.name, padx=5, pady=5)
        l2.grid(column=1, row=i)
        i += 1

    i = 0
    for d in globVar.allowedList:
        l1 = Label(allowedTab, text=d.macAddress, padx=5, pady=5)
        l1.grid(column=0, row=i)
        l2 = Label(allowedTab, text=d.name, padx=5, pady=5)
        l2.grid(column=1, row=i)
        i += 1



    n.pack(expand=1, fill='both')

    gui.mainloop()

