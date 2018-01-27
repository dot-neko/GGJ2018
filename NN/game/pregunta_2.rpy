label pregunta2:

    menu:
        "¿Que disponibilidad horaria tienes?"
        #Opcion Verde
        "Tengo disponibilidad horaria y puedo trabajar horas extras.":
            $horasextras = True
            c "Estoy disponible para trabajar en los horarios que dispongan, en el tiempo que necesiten."
            #Cara pensando
            a "Mira que para trabajar mucho tiempo tienes que saber manejar el estrés."
            #cara pensando
            a "Pero me imagino que no estas tomando esta decisión a la ligera, así que continuemos."
            

        #Opcion Naranja
        "Si es posible, preferiría trabajar de mañana, pero me adapto.":
            $variosturnos = True
            c "Sinceramente, creo que puedo rendir mejor por la mañana. Puedo adaptarme al horario que dispongan, de todas formas."


        #Opcion Roja
        "Solo estoy dispuesto a trabajar de mañana, las tardes y noches son para mi.":
            $horasextras = False
            $variosturnos = False

    return