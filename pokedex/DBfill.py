import sqlite3

conn = sqlite3.connect('pokedex.db')
cursor = conn.cursor()


conn.execute("""insert into pokemon(name, ptype, img) values (?, ?, ?) """,
             ("Florizarre","Plante/Poison", "https://projectpokemon.org/images/normal-sprite/venusaur.gif"))
conn.commit()
conn.close()

