label pregunta1:
    
    menu:
            scene fondoe
        "Si pudieras elegir el trabajo de supervisor ideal para ti, ¿cual seria?"
        #Opcion Verde
        "No me la juego: Equipo chico":
            $practico = True
            $complejo = False
            c "Sinceramente, me parece apropiado comenzar con un equipo pequeño."
            c "Mis habilidades son limitadas y no tengo mucha experiencia en el rubro, por lo que veo bien manejar un grupo chico de personas para poder dedicarles mi mayor atención."
            a "Me parece bien que reconozcas tus capacidades. Eso es algo que no veo todos los dias."
            show esonrisa
            a "De acuerdo, podemos ir trabajando sobre esto."

        #Opcion Naranja

        "Me gustaría formar un equipo de millenials que me cuestionen todo":
            $practico = False
            $complejo = True
            c "Me gustaría formar un equipo con personas de mente abierta que me cuestione"
            show ejodida
            a "Bien, bien. Veo que reconoces los desafios."
            show enormal
            a "De acuerdo, podemos ir trabajando sobre esto."

        #Opcion Roja
        "◔_◔ Esta es fácil":
            $practico = True
            $complejo = True
            $cabreo =+ 1
            c "Creo que me encuentro en condiciones para liderar cualquier equipo"
            show ejodida
            a "Aja, me imaginaba que tus capacidades eran superiores. Esta en su evaluación de perfil."
            a "De acuerdo, vamos a ver como podemos avanzar sobre esto."
            show enormal


    return