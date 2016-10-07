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
			grados[g]=0
		grados[g]+=1
	for cuadrante in amenazas[1]:
		cuadrantes[amenazas[1].index(cuadrante)+1]=int(cuadrante)

	#grados 1;3,3;2 hay 3 amenazas de grado 1
	#cuadrantes 1;4,2;4 hay cuatro navez en el cuadrante 1
	return grados,cuadrantes			


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
	return str(x)+","+str(y)

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
		if grados[grado]==cantidad_de_los_grados[0] and grado!="a":
			grado_predomintante=grado
	if grado_predominante==1:
		eleccion=random.randint(4,5)
	elif grado_predominante==2:
		eleccion=random.randint(2,3)
	else: #==3  
		eleccion=1
	return coords_disp(cuadranteP,eleccion)
def disparo():
    pass

def movimiento():
    pass
