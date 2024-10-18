def ingresar_puntuacion_y_comentario():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()

        if point.isdecimal():
            point = int(point)

            if point <= 0 or point > 5:  # Expresión condicional que verifica si es menor que 0 o mayor que 5
                print('Indíquelo en una escala de 1 a 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                file_pc = open("data.txt", 'a')
                file_pc.write(f'{ post } \n')
                file_pc.close()
                break
        else:
            print('Por favor, introduzca la puntuación en números')

def comprobar_resultados_obtenidos():
    print('Resultados hasta la fecha.')
    read_file = open("data.txt", "r")
    print(read_file.read())
    read_file.close()

while True:
    print('Seleccione el proceso que desea aplicar')
    print('1: Ingresar puntuación y comentario')
    print('2: Comprueba los resultados obtenidos hasta ahora.')
    print('3: Finalizar')
    num = input()

    if num.isdecimal():
        num = int(num)
        if num == 1:
            ingresar_puntuacion_y_comentario()  # Llamada al método
        elif num == 2:
            comprobar_resultados_obtenidos()  # Llamada al método
        elif num == 3:
            print('Finalizando')
            break  # Sentencia para finalizar el procesamiento
        else:
            print('Introduzca un número del 1 al 3')
    else:
        print('Introduzca un número del 1 al 3')
