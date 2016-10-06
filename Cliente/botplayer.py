import numpy

def bot(amenaza):
    pass

def checkear_amenazas(amenazas):
    a, b = amenazas.strip().split(":")
    print a, b
    

def escoger_movimiento( amenazas ):
    checkear_amenazas(amenazas)
    movimiento_x = "2"
    movimiento_y = "0" 
    return movimiento_x + "," + movimiento_y

def escoger_disparo( amenazas ):
    disparo_x = "0"
    disparo_y = "1"
    return disparo_x + "," + disparo_y
