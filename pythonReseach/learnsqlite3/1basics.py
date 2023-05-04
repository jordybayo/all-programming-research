import sqlite3


conn = sqlite3.connect('tutoriel.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix Real, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(124548787864, '2019-21-05', 'python', 8)")

#create_table()
data_entry()