import numpy
import random 
#ocupar posicion
def escoger_movimiento( amenazas ):
    movimiento_x=""
    movimiento_y=""
    amenazas,cuadrantes=amenazas.strip().split(":")
    amenazas=amenazas.strip().split("-")
    cuadrantes=cuadrantes.strip().split("-")
    cuadrante_seguro=0
    n_de_naves=1000
    for cuadrante in cuadrantes:
        if int(cuadrante) < n_de_naves:
            cuadrante_seguro=cuadrante.index(cuadrante)
            n_de_naves=int(cuadrante)
    suma_vertical=int(cuadrantes[0])+int(cuadrantes[2])
    suma_horizontal=int(cuadrantes[1])+int(cuadrantes[3])

    g1=amenazas.count("1")
    g2=amenazas.count("2")
    g3=amenazas.count("3")
    if g1 <= g2 and g1 <=g3:
        if g2 <= g1 and g2 <=g3:
            eleccion = random.randint(2,3)
        if g3 <= g1 and g3 <=g2:
            eleccion = 1
    elif g2 <= g1 and g2 <=g3:
        eleccion = random.randint(2,3)
    elif g3 <= g1 and g3 <=g2:
        eleccion = 1
    elif g1==g2 and g2==g3 and g3==0:
        eleccion = random.randint(0,1)
        if eleccion==0:
            eleccion=random.randint(-3,-1)
        if eleccion==1:
            eleccion=random.randint(1,3)
    BANDERA=True
    while BANDERA:
        if suma_vertical < suma_horizontal:
            if cuadrante_seguro==0:
                movimiento_x='0'
                movimiento_y=str(eleccion)
            if cuadrante_seguro==2:
                movimiento_x='0'
                movimiento_y=str(-eleccion)
        if suma_vertical > suma_horizontal:
            if cuadrante_seguro==1:
                movimiento_x=str(-eleccion)
                movimiento_y='0'
            if cuadrante_seguro==3:
                movimiento_x=str(eleccion)
                movimiento_y="0"
        BANDERA=False

    #ir renovando posicion
    print  movimiento_x + "," + movimiento_y
    return movimiento_x + "," + movimiento_y

def escoger_disparo( amenazas ):
    print "comenzando disparo"
    disparo_x=""
    disparo_y=""
    amenazas,cuadrantes=amenazas.strip().split(":")
    amenazas=amenazas.strip().split("-")
    cuadrantes=cuadrantes.strip().split("-")
    cuadrante_peligroso=0
    n_de_naves=0
    for cuadrante in cuadrantes:        
        if int(cuadrante) > n_de_naves:
            cuadrante_peligroso=cuadrantes.index(cuadrante)
            n_de_naves=int(cuadrante)
    
    g1=amenazas.count("1")
    g2=amenazas.count("2")
    g3=amenazas.count("3")
    print "amenazas"
    if g1 >= g2 and g1 >=g3:
        eleccion = random.randint(4,5)
    if g2 >= g1 and g2 >=g3:
        eleccion = random.randint(2,3)
    if g3 >= g1 and g3 >=g2:
        eleccion = 1
    if g1==g2 and g2==g3 and g3==0:
        eleccion = random.randint(0,1)
        if eleccion==0:
            eleccion=random.randint(-5,-1)
        if eleccion==1:
            eleccion=random.randint(1,5)
    if cuadrante_peligroso==0:
        disparo_x="0"
        disparo_y=str(eleccion)
    if cuadrante_peligroso==1:
        disparo_x=str(-eleccion)
        disparo_y="0"
    if cuadrante_peligroso==2:
        disparo_x="0"
        disparo_y=str(-eleccion)
    if cuadrante_peligroso==3:
        disparo_x=str(eleccion)
        disparo_y="0"
    print  disparo_x + "," + disparo_y
    return disparo_x + "," + disparo_y
