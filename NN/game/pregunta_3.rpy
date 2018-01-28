label pregunta3:

    menu:
        a "¿Qué puedes hacer por la compania que nadie mas pueda?"
        #Opcion Verde
        "♩TRABAJO MUY DURO, COMO UN ESCLAVO♪":
            $scompleja = True
            $ssocial = False
            c "Creo que el equipo toma forma sólo cuando hay una gran tarea por delante."
            #Cara sarcástica flash
            #Cara normal
            a "Cierto, a veces se puede ir avanzando sólo con un objetivo claro."

        #Opcion Naranja
        "Me interesa trabajar y tener buena onda con el equipo ◕ ◡ ◕ ":
            $scompleja = False
            $ssocial = True 
            #Cara sorpresa
            c "Me interesa que el equipo funcione, con lo que el aspecto humano no puede faltar ante una gran tarea."
            
        #Opcion Roja
        "Deal with it":
            $scompleja = True
            $ssocial = True
            #Cara sorpresa flash
            #Cara cabreada
            c "Creo en mis habilidades y que puedo llevar adelante cualquier proyecto, sin importar las cualidades del equipo".


    return