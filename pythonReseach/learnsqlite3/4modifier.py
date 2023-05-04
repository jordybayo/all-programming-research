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

def retrieve():
    requette = "SELECT * FROM employees WHERE salaire={}".format(4500)
    print(requette)
    a = c.execute(requette).fetchall()
    print(a[1][2])
    
def update(NomEmp, PrenomEmploye, salaire):
    with conn:
        c.execute("""UPDATE employees SET salaire = :salaire WHERE nom = :nom AND prenom = :prenom""",{'nom':NomEmp, 'prenom':PrenomEmploye, 'salaire':salaire})
    
    
#create_table()
#data_entry()
#retrieve()
#update('tech', 'code', 7500)