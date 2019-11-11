""" This file defines the global variables, so they
    can be accessible to any file
"""
from threading import Lock


def init(): # This gets called first thing in the main file
    global blackList
    blackList = []
    global blackListMutex
    blackListMutex = Lock()

    global allowedList
    allowedList = []
    global allowedListMutex
    allowedListMutex = Lock()

    global greyList
    greyList = []
    global greyListMutex
    greyListMutex = Lock()

    global continueProcessing
    continueProcessing = 1

    global dbMutex
    dbMutex = Lock()
