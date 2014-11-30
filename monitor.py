import sqlite3

import os
import time
import glob
import serial

# global variables
speriod=(15*60)-1
dbname='/var/www/templog.db'
ser = serial.Serial('/dev/ttyACM0', 115200)

def log_temperature(temp):

    conn=sqlite3.connect(dbname)
    curs=conn.cursor()

    curs.execute("INSERT INTO temps values(datetime('now', 'localtime'), (?))", (temp,))

    # commit the changes
    conn.commit()

    conn.close()

def display_data():

    conn=sqlite3.connect(dbname)
    curs=conn.cursor()

    for row in curs.execute("SELECT * FROM temps"):
        print str(row[0])+"	"+str(row[1])

    conn.close()

i=0

while i<8:
        ser.readline()
        i=i+1
line=ser.readline()
#print line
data=line.split(";")
#print data
temp=((data[0].split(":"))[1])
print temp
log_temperature(temp)
display_data()

