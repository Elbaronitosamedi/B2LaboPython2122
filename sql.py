from faker import Faker 
import sqlite3 

fake = Faker('fr_FR')
conn = sqlite3.connect('python.db')
cursor = conn.cursor()


def fill(limit) : 

    for i in range(limit) :
            prenom = fake.first_name()
            nom = fake.last_name()
            dateN = fake.date_of_birth()
            dateR = fake.date_this_year()
            tel = fake.phone_number()
            mail = fake.safe_email()
            job = fake.job() 
            conn.execute("""insert into Employé(
            nom, prénom, date, recrutement, tel, Email, job)
            values (?, ?, ?, ?, ?, ?,?)""",(nom, prenom, dateN, dateR, tel, mail, job))
            conn.commit()
    conn.close()

fill(10000)