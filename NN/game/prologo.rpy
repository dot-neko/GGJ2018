label prologo:
    #Mostrar fondo dormitorio del entrevistado
    #Eleccion de nombre

    # The phrase in the brackets is the text that the game will display to prompt 
	# the player to enter the name they've chosen.

    $ player_name = renpy.input("¿Querés elegir tu nombre?")

    $ player_name = player_name.strip()

    if player_name == "":
    	"No importa. Recordaste de repente que tu nombre era Pepito."
        $ player_name="Pepito"

  #Preguntar el nombre del personaje o decidir uno si lo deja en blanco
	define c = Character("[player_name]", color="#c8c8ff")

    scene black

    c "Ayer fui selecionado para trabajar en la empresa R.E.O. SA como supervisor de un área de IT"
    c "Aun queda pendiente de negociar el tema del horario, sueldo y la sucursal en la que voy a trabajar."
    c "Todo esto se va a decidir en la entrevista de esta tarde que se va a hacer con una entrevista online"
    c "Por desgracia no es el mejor dia para mi conexión, bueno, de alguna manera se arreglará."

    return