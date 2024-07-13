def save():
    rate=0
    while rate < 1 or rate > 5:
        print("Por favor, introduzca un valor entre el 1 y 5")
        rate = int(input("Ingrese una puntuacion del 1 al 5"))
    comment = str(input("Ingrese un comentario si desea, en caso de no querer solo apriete enter en el espacio vacio"))
    if comment == "":
        comment = "Sin comentarios."
    file = open('data.txt', 'a')
    # El metodo open se usa para abrir un archivo externo
    # El primer parametro debe ser el nombre del archivo
    # El segundo parametro debe ser lo que se permita hacer con el archivo
    # 'r' es para solo leer el contenido del archivo
    # 'w' es para solo poder escribir en el contenido del archivo
    # 'a' es se permite hacer ambos
    register = f'Puntos: {rate} estrellas\\nComentarios: {comment}\\n'
    file.write(f'{register}\\n')
    # con el metodo write podemos agregarle texto al archivo
    file.close()
    # con el metodo close cerramos el archivo, hacer esto es obligatorio para
    # guardar los cambios.
    print("Su comentario se ha registrado exitosamente")

def show():
    print("Este es el registro de valoraciones hasta la fecha \\n")
    read_file = open('data.txt', 'r')
    # usamos el metodo read cada vez que precisemos leer el archivo
    print(read_file.read())
    read_file.close()

    