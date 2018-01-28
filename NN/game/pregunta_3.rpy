label pregunta3:

    menu:
        a "¿Qué puedes hacer por la compania que nadie mas pueda?"
        #Opcion Verde
        "♩TRABAJO MUY DURO, COMO UN ESCLAVO♪":
            $compleja = True
            $social = False
            c "Creo que el equipo toma forma sólo cuando hay una gran tarea por delante."
            show enormal
            a "Cierto, a veces se puede ir avanzando sólo con un objetivo claro."
            c "Si, es un poco lo que tengo en mente para este trabajo."

        #Opcion Naranja
        "Me interesa trabajar y tener buena onda con el equipo ◕ ◡ ◕ ":
            $compleja = False
            $social = True 
            show ejodida
            show enormal
            c "Me interesa que el equipo funcione, con lo que el aspecto humano no puede faltar ante una gran tarea."
            a "Ciertamente, al tener un grupo que se conozca entre sí, los trabajos tienen mejor calidad"
            
        #Opcion Roja
        "Deal with it":
            $compleja = True
            $social = True
            c "Creo en mis habilidades y que puedo llevar adelante cualquier proyecto, sin importar las cualidades del equipo"
            show ejodida
            show etevasaenterar
            a "Interesante. Creo que hay pocos perfiles adecuados como el suyo."
            a "Creo que existen varias oportunidades para que pueda desarrollar sus {b}habilidades únicas{/b}."
            show esonrisa

    return