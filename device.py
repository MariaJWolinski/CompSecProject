""" This file defines the class Device, which
    is basically the type of anything that
    attempts to connect to our network
"""

class Device:
    def __init__(self, macAddress, name):
        self.macAddress = macAddress
        self.name = name

    def __str__(self):
        return "<%s, %s>" % (self.macAddress, self.name) # Make it not print weird

    def __repr__(self):
        return "<%s, %s>" % (self.macAddress, self.name) # Also the printing thing
