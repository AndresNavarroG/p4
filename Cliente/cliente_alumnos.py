import socket
from botplayer import *

def spawn(cliente):
    mensaje = cliente.recv(1024)
    posicion = mensaje.split(",")
    return int(posicion[0]), int(posicion[1])

#LOGIN
cliente = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
IP = raw_input("ingrese la ip ")
PORT = input("ingrese el puerto ")
cliente.connect( (IP ,PORT ) )
usuario = raw_input( "Ingrese nombre de usuario:" )
cliente.send( usuario )

#SPAWN INICIAL
posicion = spawn(cliente) 

juego = 1
try:
    while (juego):

        #Recibir mensaje del servidor
        mensaje = cliente.recv(1024)

        # mensaje, es el string de amenazas, en base a aquel mensaje, tomar una decision
        
        """
        escoger_disparo( mensaje ) se encuentra en botdummy, es tarea de ustedes completar esta funcion.

        escoger_movimieto( mensaje ) se encuentra en botdummy, es tarea de ustedes completar esta funcion.

        """
        posicion=list(posicion) #se transforma la tupla a una lista para poder modificarla
        #disparo = escoger_disparo( mensaje )        
        #movimiento = escoger_movimiento( mensaje )
        #mensaje =  disparo+"/"+movimiento
        mensaje=procesar(mensaje,posicion)
        mov=mensaje.split("/")[1]
        sumar_pos=mov.split(",")
        posicion[0]+=int(sumar_pos[0])
        posicion[1]+=int(sumar_pos[1])
        posicion[0]=posicion[0]%11
        posicion[1]=posicion[1]%11
        
        
        cliente.send(mensaje )
except socket.error:
    cliente.close()
    print "GAME OVER"
