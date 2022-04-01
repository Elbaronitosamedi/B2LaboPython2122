import sqlite3

conn = sqlite3.connect('scores.db')
cursor = conn.cursor()

req = "CREATE TABLE Scores (Score INTEGER NOT NULL PRIMARY KEY, Pseudo VARCHAR(15) NOT NULL)" 

cursor.execute(req)
conn.commit()