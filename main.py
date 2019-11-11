import globVar
import dbStuff
import threading
import monitor
import deauthenticate
import guiFile


# Initiate the global variables
globVar.init()

# Populate the lists of devices from the database
dbStuff.populate_lists()

"""
There are 3 main tasks that our program needs to be doing:
    1. Monitoring the network for any new devices that get added,
        and adding them to the greyList
    2. Continually sending deauthentication messages to devices
        on the blackList or greyList
    3. Displaying the gui and responding to any user input.  This
        could mean moving devices from the greyList to the allowed
        list, or moving stuff around in some other way
Because it's desirable to have all of this stuff happening at the
same time, I think that it makes sense to multi-thread our code, using
3 separate threads.  That means we'll have to use mutexes anytime we 
write to the device lists.
"""

# Create a string for each task
monitor = threading.Thread(target=monitor.monitor_devices, args=())
deauth = threading.Thread(target=deauthenticate.deauthenticate_devices(), args=())
guiThread = threading.Thread(target=guiFile.main_gui(), args=())

# Start the threads
monitor.start()
deauth.start()
guiThread.start()

# Join the threads
guiThread.join()

# Tell the other threads to stop when the gui returns
globVar.continueProcessing = 0

monitor.join()
deauth.join()


print("Done!")

