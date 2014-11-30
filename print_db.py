#!/usr/bin/env python
import sqlite3

import os
import time
import glob

# global variables
dbname='/var/www/templog.db'
humDb='/var/www/humlog.db'
def display_data():

    conn=sqlite3.connect(dbname)
    curs=conn.cursor()

    for row in curs.execute("SELECT * FROM temps"):
        print str(row[0])+"	"+str(row[1])

    conn.close()

def display_data_h():

    conn=sqlite3.connect(humDb)
    curs=conn.cursor()

    for row in curs.execute("SELECT * FROM hums"):
        print str(row[0])+"     "+str(row[1])

    conn.close()


if __name__=="__main__":
	display_data()
	display_data_h()
