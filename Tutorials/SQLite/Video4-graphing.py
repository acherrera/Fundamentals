"""
Purpose: Learning SQLite
Created by: Anthony Herrera
Notes: Following Sentdex tutorials
This file contains the most recent work on the tutorial. Each file is a
little different.

Tutorial 4 - getting and graphing data
"""

import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

# from tutorial 1
conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

# from tutorial 1
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp\
     TEXT,'
    'keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(14512343245234, '2016-01-01',\
    'Python', 5)")
    conn.commit()
    c.close()
    conn.close()

# From tutorial 2
def dynamic_data_entry():
    """
    Showing how to add data without having to hard code it. Note that SQLite
    uses '?' whereas mySQL will use '%s' when adding data
    """
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y,-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value)\
     VALUES (?, ?, ?, ?)", (unix, date, keyword, value))
    conn.commit()


def read_from_db():
    """
    Moving data into the program
    This selects with cursor, but need to copy to memory
    Using '*' will select all but you can be more specific
    WHERE unix > AND unix <
    WHERE value=3
    """
    c.execute("SELECT keyword, unix FROM stuffToPlot")
    # Get all the data
    # data = c.fetchall()
    for row in c.fetchall():
        print(row)


def graph_data():
    """
    Want to graph the values in data
    """
    c.execute('SELECT unix, value FROM stuffToPlot')
    dates = []
    values = []
    # Get the data out of the cursor
    for row in c.fetchall():
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()


# create_table()
# data_entry()
# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1)
# read_from_db()

graph_data()

# Only need to close this at the very end
c.close()
conn.close()
