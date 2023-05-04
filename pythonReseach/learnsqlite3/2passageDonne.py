import sqlite3


conn = sqlite3.connect('tutoriel.db')
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS employees(
            nom TEXT,
            prenom TEXT,
            salaire INTEGER
        )""")
    conn.commit()

def data_entry():
    nom = 'nhesiterPasSurtout'
    prenom = 'devousAbonner'
    salaire = 4500
    # requette = "INSERT INTO employees VALUES('{}', '{}', {})".format(nom, prenom, salaire)
    #   print(requette)
    c.execute("INSERT INTO employees VALUES(?, ?, ?)",(nom, prenom, salaire))
    conn.commit()

#create_table()
data_entry()