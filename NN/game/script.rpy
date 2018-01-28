# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

#Entrevistador cuando todavia no se presento
define e = Character("Entrevistador", color="#c8ffc8")

#Nombre entrevistador una vez que se presenta
define a = Character("Andrea", color="#c8ffc8")

#Fondo Negro
image black = "#000"
# El juego comienza aquí.

#show cancherito

label start:
    # El prologo es una pantalla negra con monologo del PP
    play music "sounds/bg_sound.mp3"
    call prologo
    
    
    # Llama a la intro del juego
    call intro

    show epregunta

    # Llama a la primer pregunta
    call pregunta1

    # Llama a la segunda pregunta
    call pregunta2

    # Llama a la tercer pregunta
    call pregunta3

    # Evaluacion de las respuestas

    # Respuesta 1
    if (social == True and complejo == True):

        $respuesta1 = "un equipo veterano en la India "

    if (social == False and complejo == True):

        $respuesta1 = "un equipo nuevo en la ciudad de Bs As"

    if (social == True and complejo == False):

        $respuesta1 = "un equipo pequeño en la Patagonia."

    #Respuesta 2
    #Opcion Roja
    if (horasextras == False and variosturnos == False):

        $respuesta2 = "con un sueldo mínimo, sin horas extras ni trabajos adicionales"

    #Opcion Naranja
    if (horasextras == False and variosturnos == True):

        $respuesta2 = "con un horario reducido, con opción a horas extras"

    #Opcion Verde
    if (horasextras == True and variosturnos == True):

        $respuesta2 = "con un horario completo, con la opción a realizar horas extras"
    # Finaliza el juego:

    #Respuesta 3
    #Opcion Roja
    if (complejo == True and practico == True):


        $respuesta3 = "Supervisor de un area de mantenimiento a usuarios finales."


    #Opcion Naranja
    if (compleja == False and practico == True):


        $respuesta3 = "Supervisor de un grupo especializado en microinformatica."


    #Opcion Verde
    if (compleja == True and practico == False):


        $respuesta3 = "Supervisor de un grupo grande de marketing."


    # Finaliza el juego:
    call resultados


    return
