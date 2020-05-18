from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'

#player = input("Elige! Piedra, Papel o Tijeras: ")
player=''
player = player.lower()
#print(player)
ai = randint(1,3)

if ai == 1:
    ai = 'Piedra'

elif ai == 2:
    ai = 'Papel'

else:
    ai = 'Tijeras'

winner = ''

#print('La IA ha elegido: ' + ai)

def quienGana(player, ai):
    
    if player == 'piedra' and ai == 'Piedra':
        winner = 'Empate!'
    

    elif player == 'piedra' and ai == 'Papel':
        winner = 'Perdiste!'
    
    elif player == 'piedra' and ai == 'Tijeras':
        winner = 'Ganaste!'
    
    elif player == 'papel' and ai == 'Piedra':
        winner = 'Ganaste!'
    

    elif player == 'papel' and ai == 'Papel':
        winner = 'Empate!'
    
    elif player == 'papel' and ai == 'Tijeras':
        winner = 'Perdiste!'
    
    elif player == 'tijeras' and ai == 'Piedra':
        winner = 'Perdiste!'
    

    elif player == 'tijeras' and ai == 'Papel':
        winner = 'Ganaste!'
    
    elif player == 'tijeras' and ai == 'Tijeras':
        winner = 'Empate!'

    return winner

# Entry Point
def Game():
    # 
    #

    #
    #
    
    winner = quienGana (player, ai)

    print(winner)


#Game()


