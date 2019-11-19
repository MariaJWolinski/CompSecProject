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

    # Deauthentication variables
    global conf_iface
    conf_iface = "Realtek PCIe GBE Family Controller"  # This is what it needs to be for Will
    # conf_iface = "en0" # Maria is still figuring out what she needs...
    global router_bssid
    router_bssid = "00:C0:CA:90:99:FE" # This is what it needs to be for Will
    # router_bssid = "94:6a:77:90:9f:12" # This is what it needs to be for Maria

