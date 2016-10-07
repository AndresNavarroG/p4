import numpy

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
