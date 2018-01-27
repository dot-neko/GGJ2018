# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

#Entrevistador cuando todavia no se presento
define e = Character("Entrevistador")

#Preguntar el nombre del personaje o decidir uno si lo deja en blanco
define c = Character("PP")

#Nombre entrevistador una vez que se presenta
define a = Character("Andres")


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

    "primer PREGUNTA"

    # Llama a la segunda pregunta

    e "Segunda pregunta"

    # Llama a la tercer pregunta

    e "Y por último: "

    # Evaluacion de las respuestas

    # Finaliza el juego:

    return
