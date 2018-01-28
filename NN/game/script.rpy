# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

#Entrevistador cuando todavia no se presento
define e = Character("Entrevistador", color="#c8ffc8")

#Nombre entrevistador una vez que se presenta
define a = Character("Chica", color="#c8ffc8")

#Fondo Negro
image black = "#000"

#Fondo Blanco
image white = "#fff"
# El juego comienza aquí.

#show cancherito
scene fondoe

label start:
    # El prologo es una pantalla negra con monologo del PP

    call prologo

    #scene bg_one
    
    
    # Llama a la intro del juego
    call intro


    # Muestra la imagen de fondo a usar en el juego
    scene bg room


    show epregunta

    # Llama a la primer pregunta
    call pregunta1

    # Llama a la segunda pregunta
    call pregunta2

    # Llama a la tercer pregunta
    call pregunta3

    # Evaluacion de las respuestas

    # Respuesta 1
    if (practico == True and complejo == True):

        $respuesta1 = "un equipo veterano en la pcia de Santa Cruz"

    if (practico == False and complejo == True):

        $respuesta1 = "un equipo nuevo en la ciudad de Bs As"

    if (practico == True and complejo == False):

        $respuesta1 = "un equipo pequeño en la ciudad de Mendoza"

    #Respuesta 2
    #Opcion Roja
    if (horasextras == False and variosturnos == False):

        $respuesta2 = "con un sueldo mínimo, sin horas extras ni trabajos adicionales"

    #Opcion Naranja
    if (horasextras == False and variosturnos == True):

        $respuesta2 = "con un horario reducido, con opción a horas extras"

    #Opcion Verde
    if (horasextras == True and variosturnos == False):

        $respuesta2 = "con un horario completo, con la opción a realizar horas extras"
    # Finaliza el juego:

    #Respuesta 3
    #Opcion Roja
    if (scompleja == True and ssocial == True):

        $respuesta3 = ""

    #Opcion Naranja
    if (scompleja == False and ssocial == True):

        $respuesta3 = ""

    #Opcion Verde
    if (scompleja == True and ssocial == False):

        $respuesta3 = ""
    # Finaliza el juego:
    call resultados


    return
