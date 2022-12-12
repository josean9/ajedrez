def movimiento():
    print("Desea mover una pieza? (si/no)")
    movimientos = 0
    respuesta = input()
    while True:
        if respuesta == "si":
            fila_antes = input("Ingrese la fila de la pieza que desea mover")
            columna_antes = input("Ingrese la columna de la pieza que desea mover")
            fila_despues = input("Ingrese la fila a la que desea mover la pieza")
            columna_despues = input("Ingrese la columna a la que desea mover la pieza")
            try:
                fila_antes = int(fila_antes)
                columna_antes = int(columna_antes)
                fila_despues = int(fila_despues)
                columna_despues = int(columna_despues)
            except:
                print("Ingrese un numero valido")
                continue
            else:
                movimientos += 1
                tablero_sin_jugar[fila_despues-1][columna_despues-1] = tablero_sin_jugar[fila_antes-1][columna_antes-1]
                return "Ha movido la pieza de la fila {}, columna {} a la fila {}, columna {}".format(fila_antes, columna_antes, fila_despues, columna_despues)
        elif respuesta == "no":
            print("No se ha movido ninguna pieza, partida finalizada")
            break
        else:
            print("Ingrese una respuesta valida")
            continue

print(movimiento())