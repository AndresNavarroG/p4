#Modulos
import numpy
import random 
#Funciones
def n_de_jugadores(cuadrantes):
	tam=0
	n_naves=cuadrantes.values()
	n_naves=n_naves.sum()
	if n_naves<5:
		tam=10
	elif n_naves<10:
		tam=15
	else:
		tam=20
	return n_naves,tam
def procesar(amenazas):
	amenazas=amenazas.split(":")
	cuadrantes=dict()
	grados=dict()
	for g in amenazas[0]:
		if grados.has_key(g)==False:
			if g=="a":
				#hacer nada
			else:
				grados[int(g)]=0
		grados[g]+=1
	for cuadrante in amenazas[1]:
		cuadrantes[amenazas[1].index(cuadrante)+1]=int(cuadrante)

	#grados 1;3,3;2 hay 3 amenazas de grado 1
	#cuadrantes 1;4,2;4 hay cuatro navez en el cuadrante 1
	return grados,cuadrantes			



def escoger_movimiento(grados,cuadrantes):
	cuadranteS=0
	minnaves=1000
	cantidad_de_los_grados=grados.values()
	cantidad_de_los_grados.sort()
	grado_-_predominante=0
    for cuadrante in cuadrantes:
		if cuadrantes[cuadrante]<minnaves:
        	cuadranteS=cuadrante
			minnaves=cuadrantes[cuadrante]
	for grado in grados:
		if grados[grado]==cantidad_de_los_grados[0]:
			grado_-_predominante=grado
    suma_vertical=int(cuadrantes[1])+int(cuadrantes[3])
    suma_horizontal=int(cuadrantes[2])+int(cuadrantes[4])
	if grado_-_predominante==1:
		eleccion=random.randint(4,5)
	elif grado_-_predominante==2:
		eleccion=random.randint(2,3)
	else: #==3  
		eleccion=1
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

def coords_disp(cuadranteP,eleccion):
	if cuadranteP==1:
		x=0
		y=eleccion
	if cuadranteP==2:
		x=-eleccion
		y=0
	if cuadranteP==3:
		x=0
		y=-eleccion
	if cuadranteP==4:
		x=eleccion
		y=0
	return str(x)+","str(y)

def escoger_disparo( grados,cuadrantes):
    print "comenzando disparo"
	cuadranteP=0
	maxnaves=0
	cantidad_de_los_grados=grados.values()
	cantidad_de_los_grados.sort()
	cantidad_de_los_grados.reverse()
	grado_predominante=0
	for cuadrante in cuadrantes:
		if cuadrantes[cuadrante]>maxnaves:
			cuadranteP=cuadrante
			maxnaves=cuadrantes[cuadrante]
	for grado in grados:
		if grados[grado]==cantidad_de_los_grados[0]:
			grado_predomintante=grado
	if grado_predominante==1:
		eleccion=random.randint(4,5)
	elif grado_predominante==2:
		eleccion=random.randint(2,3)
	else: #==3  
		eleccion=1
	return coords_disp(cuadranteP,eleccion)
