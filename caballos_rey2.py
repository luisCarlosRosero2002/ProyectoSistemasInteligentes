Abiertos = [[],[],[],[]]
Cerrados = [[],[],[],[]]
E_actual = []
Caballos = []
Rey = []
indice = 0


def agregar_o_reemplazar(abiertos,movimientos):

    if len(abiertos) > 0:
        for i in movimientos:
            for j in abiertos:
                if i == j:
                    indice = abiertos.index(i)
                    abiertos[indice] = i

            if i not in abiertos:
                abiertos.append(i)
    else:
        return movimientos

    return  abiertos 

# def VerMovivientosCaballos():


#     # for i in E_actual:
#     #     print("Caballo #")

def FinalizarJuego(vectorJaque):

    global E_actual, Rey

    for i,elemento in enumerate(E_actual):
        movimientos = MovimientoCaballo(elemento)
        for j in movimientos:
            if j == Rey[0]:
                return True and FinalizacionVectorJaque(vectorJaque)
    
    return False



def FinalizacionVectorJaque(vectorJaque):

    global E_actual

    conjunto_vectorjaque = {tuple(d.items()) for d in vectorJaque}
    conjunto_cubiertas = {}

    for i in E_actual:
        movimientos = MovimientoCaballo(i)
        conjunto_moves = {tuple(d.items()) for d in movimientos}
        conjunto_cubiertas = set(conjunto_cubiertas) | (conjunto_moves & conjunto_vectorjaque)

    # conjunto_cubiertas = set(conjunto_cubiertas)

    if conjunto_cubiertas ==  conjunto_vectorjaque  : return True

    else: return False


def ValorHeuristica(CaballoActual,vectorjaque):

    # Valor heuritico por la distancia
    herustica = (abs( Rey[0]["x"] - CaballoActual["x"] ) + abs( Rey[0]["y"] -  CaballoActual["y"]) )* 10

    # Posibles movimientos de dicho caballo para saber las casillas que cubre
    PosiblesMovimientos = MovimientoCaballo(CaballoActual)
    
    # Transformacion de listas a conjuntos para realizar intersecciones  
    conjunto_PMovimientos = {tuple(d.items()) for d in PosiblesMovimientos}
    conjunto_vectorjaque = {tuple(d.items()) for d in vectorjaque}
    conjunto_rey = {tuple(d.items()) for d in Rey}
    
    # Intersecciones de los movimientos con el vector jaque 
    interseccionVectorJaque_Mov = conjunto_PMovimientos & conjunto_vectorjaque 
    interseccionVectorJaque_Mov = [dict(tupla) for tupla in interseccionVectorJaque_Mov]

    # Intersecciones de los movimientos con el rey
    interseccionRey_Mov = conjunto_PMovimientos & conjunto_rey
    interseccionRey_Mov = [dict(tupla) for tupla in interseccionRey_Mov]
 
    ######################### REGLAS ##########################

    # Restar 30 pts si cubre mas de 1 casilla del vector jaque
    if len(interseccionVectorJaque_Mov) > 1 :
        herustica -= 30
    # Restar 10 pts si cubre solo 1 casilla del vector jaque
    if len(interseccionVectorJaque_Mov) == 1:
        herustica -= 10
    # Restar 10 pts si se cubre al rey cuando ya se halla completado el vector jaque
    # Revisar
    if len(interseccionRey_Mov) > 0 and FinalizacionVectorJaque(vectorjaque):
        herustica -= 10
    # Sumar 900 pts si se cubre al rey y no esta completado el vector jaque 
    if len(interseccionRey_Mov) > 0 and not FinalizacionVectorJaque(vectorjaque):
        herustica += 900
    # Sumar 900 pts si la posicion del caballo actual esta encima del vector jaque
    if CaballoActual in vectorjaque :
        herustica += 900

    return herustica


def MovimientoCaballo(caballo):

    global indice

    movimientos = []

    # Se generan los 8 movimientos
    movimientos.append({"x":(caballo["x"])-1,"y":(caballo["y"])+2})
    
    movimientos.append({"x":(caballo["x"])-2,"y":(caballo["y"])+1})
    
    movimientos.append({"x":(caballo["x"]) -2,"y":(caballo["y"])-1})
    
    movimientos.append({"x":(caballo["x"])-1,"y":(caballo["y"])-2})
    
    movimientos.append({"x":(caballo["x"])+1,"y":(caballo["y"])-2})
    
    movimientos.append({"x":(caballo["x"])+2,"y":(caballo["y"])-1})
    
    movimientos.append({"x":(caballo["x"])+2,"y":(caballo["y"])+1})
    
    movimientos.append({"x":(caballo["x"])+1,"y":(caballo["y"])+2})
    
    # Se filtran los movimietos de 1 a 9 
    movimientos = list(filter(lambda elemento: (elemento["x"] < 9 and elemento["x"] > 0)  and  
                              (elemento["y"] < 9 and elemento["y"] > 0 ) , movimientos))
    
    # Se filtra los movimientos para que no queden encima de otro caballo
    for i in E_actual:
        coordenada = {"x":i["x"],"y":i["y"]}
        movimientos = list(filter(lambda elemento: elemento != coordenada , movimientos))
    
    # Se filtra los movimientos para que no queden encima del rey
    # movimientos = list(filter(lambda elemento: elemento not in Rey , movimientos))

    # Se filtra los movimientos para que no que no visiten otro estado visitado
    for i,x in enumerate(Cerrados[indice]):
        if len(x) > 0:
            # for j,y in enumerate(x):
            coordenada = {"x":x["x"],"y":x["y"]}
            movimientos = list(filter(lambda elemento: elemento != coordenada , movimientos))    

    # movimientos = list(filter(lambda elemento: elemento not in Pfinales , movimientos))



    return movimientos

def OrderVector(caballos,vectorjaque):

    resultado = []
    aux = []

    for i in caballos:
        
        if i in vectorjaque:
            aux.append({"x":i["x"], "y":i["y"], "h": ValorHeuristica(i, vectorjaque),"padre":None})
        else:
            resultado.append({"x":i["x"], "y":i["y"], "h": ValorHeuristica(i, vectorjaque),"padre":None})

    resultado.sort(key = lambda x: x["h"],reverse=True)
    resultado = aux + resultado

    return resultado

def VectorJaque(rey):

    posiciones = []

    posiciones.append({"x":rey[0]["x"]-1,"y":rey[0]["y"]})
    posiciones.append({"x":rey[0]["x"]+1,"y":rey[0]["y"]+1})
    posiciones.append({"x":rey[0]["x"],"y":rey[0]["y"]+1})
    posiciones.append({"x":rey[0]["x"]-1,"y":rey[0]["y"]+1})
    posiciones.append({"x":rey[0]["x"]+1,"y":rey[0]["y"]})
    posiciones.append({"x":rey[0]["x"]+1,"y":rey[0]["y"]-1})
    posiciones.append({"x":rey[0]["x"],"y":rey[0]["y"]-1})
    posiciones.append({"x":rey[0]["x"]-1,"y":rey[0]["y"]-1})

    return list(
        map(lambda objeto : {"x":objeto["x"],"y":objeto["y"]},
            filter(
                lambda elemento: (elemento["x"] < 9 and elemento["x"] > 0)  and  (elemento["y"] < 9 and elemento["y"] > 0 ) , posiciones)
            )
        )


def ImprimirTablero(caballos, rey):
    
    for y in range(8,0,-1):
        for x in range(1,9):
            coordenada = {"x": x,"y":y}
            if coordenada in caballos:
                print(f"|{caballos.index(coordenada)+1}|",end="")
            elif coordenada in rey:
                print(f"|R|",end="")
            else:
                print("|_|",end="")
        print()

def Traductor(posicion):

    Numlet = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H"}
    letNum = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}

    for i in posicion:
        i["x"] = letNum.get(i["x"])

    return posicion

def main ():

    global Caballos, Rey, Abiertos, Cerrados, E_actual, indice

    H_totales = []
    H_parciales = []
    H_inicial = 0


    vectorJaque = []
    
    #Iniciacion de variables 
    Caballos = [{"x": "G", "y": 8},
                {"x": "H", "y": 8},
                {"x": "G", "y": 7},
                {"x": "H", "y": 7}
                ] 
    Rey = [{"x": "E", "y": 1}]

    # Traduccion de letras a numeros
    Caballos = Traductor(Caballos)
    Rey = Traductor(Rey)

    # Impresion del tablero de ajedrez
    ImprimirTablero(Caballos, Rey)
    
    # Creacion del vector Jaque donde se guradan las posiciones que se deben cubrir los caballos
    vectorJaque = VectorJaque(Rey)

    # Organizacion de los turnos de los caballos
    Caballos = OrderVector(Caballos,vectorJaque)

    # Se agrega los estados iniciales a los cerrados
    # Cerrados = Caballos

    # Se agrega los estados iniciales a estados actuales
    E_actual = Caballos.copy()

    H_totales = Caballos.copy()

    # Calculo de la heuristica total

    for i in H_totales:
        H_inicial += i["h"]
    


    while(True):

        # Condicion que finaliza el juego
        if FinalizarJuego(vectorJaque): break

        for i,elemento in enumerate(E_actual):
            
            indice = i
            auxE_actuales = E_actual.copy()
            heuristicaAux = 0
            Cerrados[i] += [elemento]
            movimientosParciales = MovimientoCaballo(elemento)

            for j in movimientosParciales:
                j["h"] = ValorHeuristica(j,vectorJaque)
                j["padre"] = elemento

            Abiertos[i] = agregar_o_reemplazar(Abiertos[i], movimientosParciales)

            menorAbiertos = min(Abiertos[i], key= lambda x:x["h"])

            for s in E_actual:
                if {"x":s["x"],"y":s["y"]} == {"x":menorAbiertos["x"],"y":menorAbiertos["y"]}:
                    indice = Abiertos[i].index(menorAbiertos)
                    Abiertos[i][indice]["h"] += 900
                    menorAbiertos = min(Abiertos[i], key= lambda x:x["h"])
        

            # E_actual[i] = menorAbiertos

            auxE_actuales[i] = menorAbiertos.copy()

            for j in auxE_actuales:
                heuristicaAux += j["h"]

            # print("Siguiente")
            aux = menorAbiertos.copy()

            aux["Htotal"] = heuristicaAux
            H_totales[i] = aux

        

        menorTotales = min(H_totales, key= lambda x:x["Htotal"])


        for j,elemento in enumerate(E_actual):
            if elemento["x"] == menorTotales["padre"]["x"] and elemento["y"] == menorTotales["padre"]["y"] and elemento["h"] == menorTotales["padre"]["h"]:
                aux = {"x":menorTotales["x"],"y":menorTotales["y"],"h":menorTotales["h"],"padre":E_actual[j]}
                del Abiertos[j][Abiertos[j].index(aux)]
                E_actual[j] = {"x":menorTotales["x"], "y":menorTotales["y"], "h":menorTotales["h"],"padre":E_actual[j]}
                

        
    # VerMovivientosCaballos()
    print(E_actual)


        



main()






