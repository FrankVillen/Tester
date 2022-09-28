################################
#         INTRODUCTION         #
################################

# pip install pyzbar
# pip install opencv-contrib-python-headless

import os
import os.path
import cv2 as cv
import numpy as np
import pyzbar.pyzbar as pyzbar

#############################
#         VARIABLES         #
#############################

# Calcula el numero de imagenes listas para ser registradas
# Arreglar comentario de arriba
directory = 'C:/Users/Fran/Documents/Accuro/PyCharm/Codigos de Barras/'


############################
#         FUNCTION         #
############################

# Funcion principal
# Lectura de los codigos de barra


def tifrbar(imagentif, guardadotxt):
    print(pyzbar.decode(cv.imread(imagentif)))
    try:

        # Carga de imagen
        tifimg = cv.imread(imagentif)
        # Carga de codigos de barras de la imagen en lista
        lstbc = pyzbar.decode(tifimg)
        # Recorre objetos encontrados
        fptxt = open(guardadotxt, 'a')
        i = 1
        for bc in lstbc:
            print(i)
            i = i + 1
            print(bc)
            npoint = bc.polygon
            print(npoint)
            # Busqueda de un area rectangular
            if len(npoint) > 4:
                hull = cv.convexHull(np.array([point for point in npoint], dtype=np.float32))
                hull = list(map(tuple, np.squeeze(hull)))
                print(hull)
            else:
                hull = npoint
            n = len(hull)
            if n > 0:
                # Codigo valido
                slinea = "%s|%s\n" % (bc.data, bc.type)

                # Carga y lectura del TxT donde quedan recogidos los codigos de barras
                file_open = open(directory + "Foto.txt", 'r')
                lectura = file_open.read()

                if slinea not in lectura:
                    fptxt.write(slinea)
                    print("Ha quedado registrado el cogido: " + slinea)
                else:
                    # El codigo ya ha sido insertado previamente
                    print("Ya se ha registrado previamente el codigo: " + slinea)
        fptxt.close()
        return True
    except:
        # Si hay algun error...
        print("ERROR de lectura")
    return False


###########################
#         PROGRAM         #
###########################

if __name__ == '__main__':
    photos = os.listdir(directory + "Prueba/")
    for item in photos:
        print(item)
        # Llamada a la funcion principal, dando la imagenen y el txt
        spathfile = (directory + "Prueba/" + item)
        spathtxt = (directory + "Foto.txt")
        tifrbar(spathfile, spathtxt)
