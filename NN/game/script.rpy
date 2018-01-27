# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

#Entrevistador cuando todavia no se presento
define e = Character("Entrevistador", color="#c8ffc8")

#Preguntar el nombre del personaje o decidir uno si lo deja en blanco
define c = Character("PP", color="#c8c8ff")

#Nombre entrevistador una vez que se presenta
define a = Character("Andres", color="#c8ffc8")


# El juego comienza aquí.

label start:
    # El prologo es una pantalla negra con monologo del PP

    call prologo

    # Muestra una imagen de fondo inicial

    #scene bg_one

    # Muestra la imagen de fondo a usar en el juego

    scene bg room
    
    # Llama a la intro del juego
    call intro

    # Llama a la primer pregunta
    call pregunta1

    # Llama a la segunda pregunta
    call pregunta2

    # Llama a la tercer pregunta

    call pregunta3
    # Evaluacion de las respuestas

    if (practico == True and complejo == True):

        $repuesta1 = "un equipo veterano en la pcia de Santa Cruz"

    if (practico = False and $complejo = True):

        $repuesta1 = "un equipo nuevo en la ciudad de Bs As"

    if $practico = True and $complejo = False:

        $repuesta1 = "un equipo pequeño en la ciudad de Mendoza"

    # Finaliza el juego:

    call resultados

    return
