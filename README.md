# CompSecProject

This code is simply executed by running 'main.py' with python3

It is inteneded to gather a database filled with devices on our currently connected network via ARP scans. Then it sends deAuth packets to devices we do not permit to connect to our access point.


Since our code doesn't work all together cohesively, There are two added files that show how our code works individually.

Running 'deAuth.py' with python 3 is how we create and send deauthentication packets.

Running 'main_onlyGui.py' with python demonstrates how our gui works without being bogged down by ARP requests and Deauth packets.
