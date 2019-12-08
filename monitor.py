""" This file has all of the code for monitoring the
    devices on the network and adding new ones to
    the greyList
"""
import subprocess
import globVar
import device
import dbStuff


def monitor_devices():
    print("do the monitor thing!")

    # Get list of devices
    result = subprocess.check_output(["arp-scan", "-l"]).decode('utf-8')

    # Parse list so it's in the form we want
    result = result.partition(")\n")[2]
    result = result.partition("\n\n")[0]

    machines = result.split("\n")
    for machine in machines:
        sections = machine.split("\t")
        mac = sections[1]
        name = sections[2]

        if already_in_lists(mac) == 0: # If it's not in the lists already, add to grey list
            d = device.Device(mac, name)
            globVar.greyListMutex.acquire()
            try:
                globVar.greyList.append(d)
            finally:
                globVar.greyListMutex.release()

            # Also add it to the database
            globVar.dbMutex.acquire()
            try:
                dbStuff.add_to_table(2, d)
            finally:
                globVar.dbMutex.release()
                
            # TODO send message to GUI to prompt user acceptance/denial
                     
    # end of while loop


def already_in_lists(mac):
    for device in globVar.blackList:
        if device.macAddress == mac:
            return 1
    for device in globVar.allowedList:
        if device.macAddress == mac:
            return 1
    for device in globVar.greyList:
        if device.macAddress == mac:
            return 1
    return 0
