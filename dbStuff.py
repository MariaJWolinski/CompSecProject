""" This file is going to be used to define all of the methods that
    involve calls to the SQLite database, so that within our code we
    can just use a simple method call to change our lists
"""
import globVar
import device
import sqlite3


""" This method gets called once, when the application is starting.
    It reads the information from the database into our global lists.
"""
def populate_lists():
    conn = sqlite3.connect('compSec_db.sqlite')
    cur = conn.cursor()
    
    #Uncomment the next two lines if you wish to reset your database.
    # cur.execute('DROP TABLE greyList')
    # conn.commit()

    # Create the tables if they don't exist
    cur.execute('CREATE TABLE IF NOT EXISTS blackList(macAddress VARCHAR, name VARCHAR)')
    conn.commit()
    cur.execute('CREATE TABLE IF NOT EXISTS allowedList(macAddress VARCHAR, name VARCHAR)')
    conn.commit()
    cur.execute('CREATE TABLE IF NOT EXISTS greyList(macAddress VARCHAR, name VARCHAR)')
    conn.commit()

    # Populate blackList
    cur.execute('SELECT * FROM blackList')
    data = cur.fetchall()
    for datum in data:
        macAddress = datum[0]
        name = datum[1]
        d = device.Device(macAddress, name)
        globVar.blackList.append(d)

    # Populate allowedList
    cur.execute('SELECT * FROM allowedList')
    data = cur.fetchall()
    for datum in data:
        macAddress = datum[0]
        name = datum[1]
        d = device.Device(macAddress, name)
        globVar.allowedList.append(d)

    # Populate greyList
    cur.execute('SELECT * FROM greyList')
    data = cur.fetchall()
    for datum in data:
        macAddress = datum[0]
        name = datum[1]
        d = device.Device(macAddress, name)
        globVar.greyList.append(d)

    conn.close()


""" Add a device to a table in the database.
    Only call this method if you have the dbMutex,
    bc I don't remember how atomic sql things are.
    For tableNum, 0 = blackList, 1 = allowedList,
    and 2 = greyList.
    d is the device you're adding to the table.
"""
def add_to_table(tableNum, d):
    conn = sqlite3.connect('compSec_db.sqlite')
    cur = conn.cursor()

    # black list
    if tableNum == 0:
        cur.execute('INSERT INTO blackList (macAddress, name) VALUES (?, ?)',
                    (d.macAddress, d.name))

    # allowed List
    if tableNum == 1:
        cur.execute('INSERT INTO allowedList (macAddress, name) VALUES (?, ?)',
                    (d.macAddress, d.name))

    # grey List
    if tableNum == 2:
        cur.execute('INSERT INTO greyList (macAddress, name) VALUES (?, ?)',
                    (d.macAddress, d.name))

    conn.commit()
    conn.close()


""" Remove a device from a table in the database.
    Only call this method if you have the dbMutex,
    bc I don't remember how atomic sql things are.
    For tableNum, 0 = blackList, 1 = allowedList,
    and 2 = greyList.
    d is the device you're removing from the table.
"""
def remove_from_table(tableNum, d):
    conn = sqlite3.connect('compSec_db.sqlite')
    cur = conn.cursor()

    # black list
    if tableNum == 0:
        cur.execute('DELETE FROM blackList WHERE macAddress = ?',
                    (d.macAddress, ))

    # allowed List
    if tableNum == 1:
        cur.execute('DELETE FROM allowedList WHERE macAddress = ?',
                    (d.macAddress, ))

    # grey List
    if tableNum == 2:
        cur.execute('DELETE FROM greyList WHERE macAddress = ?',
                    (d.macAddress, ))

    conn.commit()
    conn.close()

