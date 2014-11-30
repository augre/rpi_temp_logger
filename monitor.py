#!/usr/bin/env python
import sqlite3

import os
import time
import glob
import serial

# global variables
tempDb='/var/www/templog.db'
humDb='/var/www/humlog.db'
ser = serial.Serial('/dev/ttyACM0', 115200)

def log_data(temp, dbase):

    conn=sqlite3.connect(dbase)
    curs=conn.cursor()

    curs.execute("INSERT INTO temps values(datetime('now', 'localtime'), (?))", (temp,))

    # commit the changes
    conn.commit()

    conn.close()
	
def log_data_h(temp, dbase):

    conn=sqlite3.connect(dbase)
    curs=conn.cursor()

    curs.execute("INSERT INTO hums values(datetime('now', 'localtime'), (?))", (hum,))

    # commit the changes
    conn.commit()

    conn.close()
	

def display_data(dbase):

    conn=sqlite3.connect(dbase)
    curs=conn.cursor()

    for row in curs.execute("SELECT * FROM temps"):
        print str(row[0])+"	"+str(row[1])

    conn.close()


if __name__=="__main__":
    
	i=0
	#throw away 8 lines
	while i<8:
		ser.readline()
		i=i+1
	line=ser.readline()
	#print line
	data=line.split(";")
	#print data
	temp=((data[0].split(":"))[1])
	hum=((data[1].split(":"))[1])
	print temp
	print hum 
	log_data(temp, tempDb)
	log_data_h(hum, humDb)
	display_data(tempDb)
	display_data(humDb)
	

