#!/usr/bin/env python
import sqlite3

import os
import time
import glob

# global variables
speriod=(15*60)-1
dbname='/var/www/templog.db'
def display_data():

    conn=sqlite3.connect(dbname)
    curs=conn.cursor()

    for row in curs.execute("SELECT * FROM temps"):
        print str(row[0])+"	"+str(row[1])

    conn.close()

if __name__=="__main__":
	display_data()
