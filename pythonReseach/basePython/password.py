from getpass import getpass
import hashlib


default_password = b"mot de passe"
default_encrypt_password = hashlib.sha1(default_password).hexdigest()

verouiller  = True
while (verouiller):
    user_password = getpass("Mot de passe: ")
    user_password = user_password.encode()
    user_password_encrypt = hashlib.sha1(user_password).hexdigest()
    
    if user_password_encrypt == default_encrypt_password :
        verouiller = False
    else:
        verouiller = True
        print("mo de passe incorect !")

print("mot de passe accepté")
