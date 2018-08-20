"""
Purpose: Learning SQLite
Created by: Anthony Herrera
Notes: Following Sentdex tutorials - video 2


"""

import sqlite3
import time
import datetime
import random


# from previous
conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

# from previous
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT,'
    'keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(14512343245234, '2016-01-01', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()

# New Stuff!
def dynamic_data_entry():
    """
    Showing how to add data without having to hard code it. Note that SQLite uses '?' whereas mySQL will use '%s' when adding data
    """
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y,-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
             (unix, date, keyword, value))
    conn.commit()


# from previous
# create_table()
# data_entry()


create_table()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1)


# Only need to close this at the very end
c.close()
conn.close()
