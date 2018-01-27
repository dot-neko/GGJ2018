label pregunta1:

    menu:
        "Si pudieras elegir el trabajo de supervisor ideal para ti, ¿cual seria?"
        #Opcion Verde
        "Para empezar estaria bien un equipo pequeño":
            $equipo_pequeno = True
            c "Sinceramente, me parece apropiado comenzar con un equipo pequeño."
            c "Mis habilidades son limitadas y no tengo mucha experiencia en el rubro, por lo que veo bien manejar un grupo chico de personas para poder dedicarles mi mayor atención."
            #Cara agradable
            a "Me parece bien que reconozcas tus capacidades. Eso es algo que no veo todos los dias."
            #cara pensando
            a "De acuerdo, podemos ir trabajando sobre esto."

        #Opcion Naranja
        "Me gustaria formar un equipo con mente abierta que me cuestione":
            $equipo_pequeno = False
            #cara sarcastica
            a "Bien, bien. Veo que reconoces los desafios."
            #cara pensando
            a "De acuerdo, podemos ir trabajando sobre esto."

        #Opcion Roja
        "Creo que me encuentro en condiciones para liderar cualquier equipo":
            $equipo_pequeno = False
            $equipo_dificil = True
            #cara sarcastica
            a "Aja, me imaginaba que tus capacidades eran superiores"
            #cara pensando
            a "De acuerdo, podemos ir trabajando sobre esto."


    return