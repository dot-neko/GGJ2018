label pregunta1:

    menu:
        "¿Qué puedes hacer por la compañía que nadie mas pueda?"
        #Opcion Verde
        "Soy una persona muy dedicada, le daría prioridad a mi trabajo":
            $trabajo = True
            

        #Opcion Naranja
        "Soy una persona trabajadora y social, puedo crear un buen ambiente mientras trabajo.":
            $social = true


        #Opcion Roja
        "Soy el mejor en mi campo y todos saben eso.":
            $trabajo = False
            $social = False

    return