# python3
# import module
import sqlite3

# Connect database
conn = sqlite3.connect('markov.db')
c = conn.cursor()

# Create database table
c.execute("create table stocks(word1, word2)")

conn.close()