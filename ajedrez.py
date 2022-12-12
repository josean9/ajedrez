from datos import *
from funciones import *
f = open(partida-ajedrez.txt, 'w')
for i in tablero:
    f.write('\t'.join(i) + '\n')
f.close()