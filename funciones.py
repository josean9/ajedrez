from datos import *
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
                mover_pieza(fila_antes, columna_antes, fila_despues, columna_despues)
                return "Ha movido la pieza de la fila {}, columna {} a la fila {}, columna {}".format(fila_antes, columna_antes, fila_despues, columna_despues)
        elif respuesta == "no":
            print("No se ha movido ninguna pieza, partida finalizada")
            break
        else:
            print("Ingrese una respuesta valida")
            continue
def imprimir_tablero():
    print("""1. Tablero sin jugar
             2. Tablero 2""")
    tablero_seleccionado = input("Ingrese el tablero que desea imprimir: ")
    try:
        tablero_seleccionado = int(tablero_seleccionado)
    except:
        print("Ingrese un numero valido")
    else:
        if tablero_seleccionado == 1:
            print(tablero_sin_jugar)
            tablero_seleccionado = tablero_sin_jugar
        elif tablero_seleccionado == 2:
            print(tablero2)
            tablero_seleccionado = tablero2
        else:
            print("Ingrese un numero valido")
def accionmenu():
    while True:
        print("1. Imprimir tablero")
        print("2. Mover pieza")
        print("3. Salir")
        opcion = input("Ingrese una opcion: ")
        try:
            opcion = int(opcion)
        except:
            print("Ingrese un numero valido")
        else:
            if opcion == 1:
                imprimir_tablero()
            elif opcion == 2:
                movimiento()
            elif opcion == 3:
                print("Gracias por jugar")
                break
            else:
                print("Ingrese una opcion valida")
def mover_pieza(f1, c1, f2, c2):
    if tablero_sin_jugar[f1][c1] in negras:
        print("Movera una pieza negra")
        tablero_sin_jugar[f2-1][c2-1] = tablero_sin_jugar[f1-1][c1-1]
        tablero_sin_jugar[f1-1][c1-1] = " "
    elif tablero_sin_jugar[f1][c1] in blancas:
        print("Movera una pieza blanca")
        tablero_sin_jugar[f2-1][c2-1] = tablero_sin_jugar[f1-1][c1-1]
        tablero_sin_jugar[f1-1][c1-1] = " "
    else:
        print("No hay pieza en esa posicion")
    return tablero_sin_jugar

