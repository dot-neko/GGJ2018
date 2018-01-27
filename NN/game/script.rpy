# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")


# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo:

    scene bg room

    # Muestra un personaje:

    show eileen happy

    # Presenta las líneas del diálogo.

    "¡Hola, mundo!"

    call prologue

    e "Has creado un nuevo juego Ren'Py."

    show eileen sad

    e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

    # Finaliza el juego:

    return
