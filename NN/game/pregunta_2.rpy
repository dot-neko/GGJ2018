label pregunta1:

    menu:
        "¿Qué disponibilidad horaria tienes?"
        #Opcion Verde
        "Tengo disponibilidad horaria y puedo trabajar horas extras.":
            $horasextras = True
            

        #Opcion Naranja
        "Si es posible, preferiría trabajar de mañana, pero me adapto.":
            $variosturnos = True


        #Opcion Roja
        "Sólo estoy dispuesto a trabajar de mañana, las tardes y noches son para mi.":
            $horasextras = False
            $variosturnos = False

    return