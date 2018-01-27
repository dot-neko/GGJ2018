label pregunta3:

    menu:
        "¿Qué puedes hacer por la compania que nadie mas pueda?"
        #Opcion Verde
        "Soy una persona muy dedicada, le daría prioridad a mi trabajo":
            $scompleja = True
            $ssocial = False
            a "Claro, a veces se puede ir avanzando "
            

        #Opcion Naranja
        "Soy una persona trabajadora y social, puedo crear un buen ambiente mientras trabajo.":
            $ssocial = True
            $scompleja = False 
            
        #Opcion Roja
        "Soy el mejor en mi campo y todos saben eso.":
            $scompleja = True
            $ssocial = True

    return