from datos import *
from funciones import *
nombre_fichero = input('Introduce el nombre del fichero: ')
fichero = open(nombre_fichero, 'w')
for i in tablero_sin_jugar:
    fichero.write('\t'.join(i) + '\n')
fichero.close()
for i in tablero_sin_jugar.split('\n'):
    tablero_final.append(i.split('\t'))