#coiding:utf-8

"""

creation de tuple vide : ()
creation d'un tuple a un element : (1,)
creation d'un tuple a plusieurs element: (1,n)
creation d'un tuple a un element : 1,
creation d'un tuple a plusieurs element: 1,n



importance des tuples : -affectation multiple
                        - retour multiple 
"""

def increment_player_position(posX,posY):
    posX += 1
    posY += 1
    return (posX,posY)


coordX = 0
coorY = 0
print("X:{} et Y:{}".format(coordX,coorY))

(coordX,coorY) = increment_player_position(coordX,coorY)
print("X:{} et Y:{}".format(coordX,coorY))
