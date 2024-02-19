'''
    ___________ Implementar el juego de Piedra Papel Tijeras ___________
'''

import random as ran

''' ## Definiendo las opciones del juego ##
    PIEDRA = 0
    PAPEL = 1
    TIJERAS = 2
'''

win_messages = [
    "¡Ganaste!",
	"¡Bien hecho!",
	"¡Sigue así!",
	"¡Eres el mejor!",
]

lose_messages = [
    "¡Perdiste!",
	"¡Lo siento!",
	"¡Sigue intentando!",
	"¡No te rindas!",
]

draw_messages = [
	"¡Empate!",
	"¡Vaya Empate!",
	"¡Vamos de nuevo!",
	"¡Suerte para la próxima!",
]

# Variable para almacenar el resultado de cada ronda
computer_score, player_score = 0, 0

# Función para jugar una ronda
def playRound(player_value):
    # Generar numero aleatorio para la opción de la computadora
    computer_value = ran.randint(0, 2)

    # Determinar el mensaje dependiendo del resultado
    match computer_value:
        case 0:
            computer_choice_str = "La computadora eligió Piedra"
        case 1:
            computer_choice_str = "La computadora eligió Papel"
        case 2:
            computer_choice_str = "La computadora eligió Tijeras"
    
    # Generar un numero aleatorio de 0 a 3 para el mensaje de resultado
    message_int = ran.randint(0, 3)

    if player_value == computer_value:
        ronda = draw_messages[message_int]
    elif player_value == (computer_value + 1) % 3:
        ronda = win_messages[message_int]
    else:
        ronda = lose_messages[message_int]
    
    return f'{computer_choice_str} \n {ronda} \n'

# Función para jugar el juego
print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")

while True:
    print("Selecciona una opción: \n 0 - Piedra \n 1 - Papel \n 2 - Tijeras \n 3 - Salir")
    player_value = int(input())

    if player_value == 3:
        break
    elif player_value < 0 or player_value > 2:
        print("Opción inválida")
    else:
        print(playRound(player_value))
