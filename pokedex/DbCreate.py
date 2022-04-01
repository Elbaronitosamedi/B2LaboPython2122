import sqlite3

conn = sqlite3.connect('pokedex.db')
cursor = conn.cursor()

req = """CREATE TABLE pokedex(
          id INTEGER NOT NULL PRIMARY KEY,
          user_id INTEGER NOT NULL,
          poke_id INTEGER NOT NULL
          );"""
        
req1 = """CREATE TABLE pokemon(
        id INTEGER NOT NULL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        ptype VARCHAR(255) NOT NULL,
        img VARCHAR(255) NOT NULL
          );"""
    
req2 = """CREATE TABLE users(
                id INTEGER NOT NULL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
         );"""



cursor.execute(req)
conn.commit()
cursor.execute(req1)
conn.commit()
cursor.execute(req2)
conn.commit()
conn.close
