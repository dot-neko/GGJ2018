label pregunta1:

    menu:
        "Si pudieras elegir el trabajo de supervisor ideal para ti, ¿cual seria?"
        #Opcion Verde
        "Para empezar estaria bien un equipo pequeño":
            $practico = True
            $complejo = False
            c "Sinceramente, me parece apropiado comenzar con un equipo pequeño."
            c "Mis habilidades son limitadas y no tengo mucha experiencia en el rubro, por lo que veo bien manejar un grupo chico de personas para poder dedicarles mi mayor atención."
            #Cara agradable
            a "Me parece bien que reconozcas tus capacidades. Eso es algo que no veo todos los dias."
            #cara pensando
            a "De acuerdo, podemos ir trabajando sobre esto."

        #Opcion Naranja

        "Me gustaría formar un equipo con mente abierta que me cuestione":
            $practico = False
            $complejo = True
            #cara sarcastica
            a "Bien, bien. Veo que reconoces los desafios."
            #cara pensando
            a "De acuerdo, podemos ir trabajando sobre esto."

        #Opcion Roja
        "Creo que me encuentro en condiciones para liderar cualquier equipo":
            $practico = True
            $complejo = True
            #cara sarcastica
            a "Aja, me imaginaba que tus capacidades eran superiores"
            #cara pensando
            a "De acuerdo, vamos a ver como podemos avanzar sobre esto."


    return