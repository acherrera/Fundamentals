"""
Purpose: Learning SQLite
Created by: Anthony Herrera
Notes: Following Sentdex tutorials

Why SQLite? Do not have to load the entire file and easier to create and work
with. I.E. Fewer setup steps
Database just has a bunch of tables. - Easy. Can use a database viewer to view
the data in the database.
"""

import sqlite3


# Basic setup. Seen eveywhere. Will create database if it does not existselfself
# Cursor is object that will have all the action done to it.
conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

# Need to create a table in the database.
# stuffToPlot - name of table. unix, datestamp, keyword, value are table heading
# REAL TEXT are data types for the columns
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT,'
    'keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(14512343245234, '2016-01-01', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()


create_table()
data_entry()

# Use SQLite Browser to view data with GUI
