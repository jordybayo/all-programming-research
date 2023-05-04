from ftplib import FTP

ftp = FTP('Nomdomaine.com')
ftp.login(user='NomUtilisateur', passwd='motDepass')
ftp.cwd('/DomainSpecif-ou-chemin/')

def EnvoiPourRecup():
    nomFichier = 'NOm.txt'
    fichierLocal = open(fichierLocal, 'wb')
    ftp.retrbinary('RETR ' + nomFichier, fichierLocal.write, 1024)
    ftp.quit()
    fichierLocal.close()

def stockFichier():
    nomFichier = 'NOm.txt'
    ftp.storbinary('STOR ' + nomFichier, open(filename, 'rb'))
    ftp.quit()