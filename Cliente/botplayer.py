#Modulos
import numpy
import random 
#Funciones

bandera_de_posicion=True
def procesar(amenazas,posicion):
        x=posicion[1]
        y=posicion[0]
        if len(amenazas)!=0: #Si hay otra nave
                amenazas=amenazas.split(":")
                amenazas[0]=amenazas[0].split("-") #lista de grados de amenazas
                amenazas[1]=amenazas[1].split("-") #lista de naves por cuadrante
                cuadrantes=dict()
                grados=dict()
                for g in amenazas[0]:
                        if grados.has_key(g)==False:
                                if g=="a": #si es una a, pasa
                                        pass
                                else: #se agrega la llave, es el grado de amenaza
                                        grados[int(g)]=0
                        if g!="a": #se le suma uno cada vez que esta aparezca
                                grados[int(g)]+=1
                c=1
                for cuadrante in amenazas[1]:
                        cuadrantes[c]=int(cuadrante) #la llave es el n del cuadrante y el valor es el numero de naves
                        c+=1
                disp=escoger_disparo(grados,cuadrantes,x,y)
                mov=escoger_movimiento(grados,cuadrantes)                
                #grados 1;3,3;2 hay 3 amenazas de grado 1
                #cuadrantes 1;4,2;4 hay cuatro navez en el cuadrante 1
                return disp+"/"+mov
        else: #si no hay otra nave , da lo mismo para que lado se mueva
                return "1,0/0,1"



def escoger_movimiento(grados,cuadrantes):
        cantidad_de_los_grados=grados.items()
        cantidad_de_los_grados.sort() # los ordena en orden de grados
        grado_menos_predominante=0
        naves=cuadrantes.values()
        n_naves=0
        for numero in naves:
                n_naves+=numero
        for grado in grados:
                if grados[grado]==cantidad_de_los_grados[0][1]: # si el valor del grado es igual al valor de cantidad de los grados es el menor
                        grado_menos_predominante=grado # se guarda como grado menor
        suma_vertical=int(cuadrantes[1])+int(cuadrantes[3]) #suma de las naves en cuadrantes verticales
        suma_horizontal=int(cuadrantes[2])+int(cuadrantes[4]) #suma de las naves en cuadrantes horizontales
        if grado_menos_predominante==1: #se ven los demas ya que no se puede mover tan lejos
                if grados.has_key(2) and grados.has_key(3):
                        if grados[2]<grados[3]: #si es menor el grado 2
                                eleccion=random.randint(2,3)
                        else: #si es menor el grado 1
                                eleccion=1
                else:
                        if grados.has_key(2): #menor es grado 2
                                eleccion=random.randint(2,3)
                        else: #menor es grado 1
                                eleccion=1
        elif grado_menos_predominante==2: 
                if n_naves==1: # si hay una sola nave,  mas seguro moverse 1 en vez de 2 o 3 en donde si puede haber nave
                        eleccion=1
                else:
                        eleccion=random.randint(2,3)
        elif grado_menos_predominante==3: #==3  
                if n_naves==1: # si hay una sola nave es mas seguro moverse 2 o 3 en vez de 1 solo
                        eleccion=random.randint(2,3)
                else:
                        eleccion=1
        else: #si no hay grados de amenaza
                eleccion=random.randint(1,3)
        return coords_mov(eleccion,cuadrantes,suma_vertical,suma_horizontal)
####
        
def coords_mov(eleccion,cuadrantes,s_ver,s_hor):
        if s_ver>1 and s_hor>1: #si hay mas de un bot funciona lo de abajo, de lo contrario no entra a ningun lado
                if s_ver<=s_hor and s_ver>0:
                        if cuadrantes[1]<cuadrantes[3] and cuadrantes[1]>0:
                                x=0
                                y=-eleccion
                        else:
                                x=0
                                y=eleccion
                if s_ver>=s_hor and s_hor>0:
                        if cuadrantes[2]<cuadrantes[4] and cuadrantes[2]>0:
                                y=0
                                x=-eleccion
                        else:
                                y=0
                                x=eleccion
        elif s_ver==0 and s_hor==0: #si no hay bot
                x=1
                y=0
        else: #si solo hay 1 bot
                if cuadrantes[1]==1: # si se quiere ir par arriba se le debe sumar a la x
                        print "arriba"
                        y=0
                        x=eleccion
                elif cuadrantes[3]==1: #para abajo restar a la x
                        print "abajo"
                        y=0
                        x=-eleccion
                elif cuadrantes[2]==1: #para la izquierda restar a la y
                        print "izq"
                        x=0
                        y=-eleccion
                else: #para la derecha sumar a la y
                        print "der"
                        x=0
                        y=eleccion
        return str(y)+","+str(x)
def coords_disp(cuadranteP,grado_predominante,x,y):
        if cuadranteP==1: #el de arriba
                if grado_predominante==1:
                        if y==5: #en este caso la unica opcion es que este en el 4, ya que si estuviese en el 5 estaria en el cuadrante 3
                                eleccion=4
                        else:
                                eleccion=random.randint(4,5)
                elif grado_predominante==2:
                        if y==3: #misma razon, si esta en y=3 y el grado predominante es 2, su unica opcion es disparar a la primera fila
                                eleccion=2
                        else:
                                eleccion=random.randint(2,3)
                elif grado_predominante==3: #==3  
                        eleccion=1
                else:
                        eleccion=1
                y=-eleccion
                x=0
        if cuadranteP==2: #izquierda
                if grado_predominante==1:
                        if x==5: #misma justificacion que arriba
                                eleccion=4
                        else:
                                eleccion=random.randint(4,5)
                elif grado_predominante==2:
                        if x==2: #misma justificacion que arriba
                                eleccion=2
                        else:
                                eleccion=random.randint(2,3)
                elif grado_predominante==3: #==3  
                        eleccion=1
                else:
                        eleccion=1
                x=-eleccion
                y=0
        if cuadranteP==3:
                if grado_predominante==1:
                        if y==6: #misma justificacion, solo que ocurre en el otro lado del tablero
                                eleccion=4
                        else:
                                eleccion=random.randint(4,5)
                elif grado_predominante==2:
                        if y==8: #misma justificacion
                                eleccion=2
                        else:
                                eleccion=random.randint(2,3)
                elif grado_predominante==3: #==3  
                        eleccion=1
                else:
                        eleccion=1
                x=0
                y=eleccion
        if cuadranteP==4:
                if grado_predominante==1:
                        if x==6: #misma justificacion
                                eleccion=4
                        else:
                                eleccion=random.randint(4,5)
                elif grado_predominante==2:
                        if x==8: #misma justificacion
                                eleccion=2
                        else:
                                eleccion=random.randint(2,3)
                elif grado_predominante==3: #==3  
                        eleccion=1
                else:
                        eleccion=2
                x=eleccion
                y=0
        if cuadranteP==0: # si no hay naves
                x=1
                y=0
        return str(y)+","+str(x)


def escoger_disparo(grados,cuadrantes,x,y):
        cuadranteP=0 #peligroso
        maxnaves=0
        cantidad_de_los_grados=grados.items()
        cantidad_de_los_grados.sort()
        cantidad_de_los_grados.reverse() #ordenados del mas a menos peligroso
        print cantidad_de_los_grados
        grado_predominante=0
        for cuadrante in cuadrantes: #se identifica el cuadrante con mas naves
                if cuadrantes[cuadrante]>maxnaves:
                        cuadranteP=cuadrante
                        maxnaves=cuadrantes[cuadrante]

        for grado in grados:
                if grados[grado]==cantidad_de_los_grados[0][1]: #si es el grado mas peligroso
                        grado_predominante = grado
        
        return coords_disp(cuadranteP,grado_predominante,x,y)
