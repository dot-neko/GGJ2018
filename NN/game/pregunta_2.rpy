label pregunta2:

    menu:
        "¿Que disponibilidad horaria tienes?"
        #Opcion Verde
        "Necesito este laburo":
            $horasextras = True
            $variosturnos = True
            c "Estoy disponible para trabajar en los horarios que dispongan, en el tiempo que necesiten."
            show enormal
            show csonrisa
            a "Mira que para trabajar mucho tiempo tienes que saber manejar el estrés."
            show ejodida
            a "Pero me imagino que no estas tomando esta decisión a la ligera, así que continuemos."
            
        #Opcion Naranja
        "A ver si puedo conseguir algo...":
            $variosturnos = True
            $horasextras = False
            c "Sinceramente, creo que puedo rendir mejor por la mañana. Puedo adaptarme al horario que dispongan, de todas formas."
            show enormal
            show csonrisa
            a "Puede que no se encuentren todas las opciones disponibles. Igual lo vamos a tener en cuenta, no se preocupe."


        #Opcion Roja
        "Tengo hambre, pero no me voy a vender tan fácil":
            $horasextras = False
            $variosturnos = False
            $cabreo =+ 1
            c "Creo que en la entrevista anterior había quedado claro mi preferencia. Sólo trabajo por la mañana"
            show ejodida
            show csonrisa
            a "Cierto, quiza se nos escapó dentro de los datos del perfil."
            a "Lo vamos a tener en cuenta, no se preocupe."
            show etevasaenterar
            
            show epregunta


    return