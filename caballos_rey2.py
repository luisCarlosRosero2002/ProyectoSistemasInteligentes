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

# Imprime las coordenas de los movimientos que realizo cada caballo con su total de movimientos
def VerMovivientosCaballos(caballosIniciales):

    pasosCaballo = []
    totalMoves = 0
    
    for i,x in enumerate(E_actual):
        cont = 0
        aux = x
        flat = True
        res = []

        while flat:
            res.append({"x":aux["x"],"y":aux["y"]})
            if aux["padre"] == None:
                flat = False
            else:
                cont += 1
                aux = aux["padre"]

         
 

        res.reverse()

        NumeroCaballo = caballosIniciales.index({'x':res[0]['x'],'y':res[0]['y']}) +1

        print("*********************************************\n")
        print(f"Caballo {NumeroCaballo}")
        res = Traductor(res)

        tam = len(res)
        con = res[tam-1]
        pasosCaballo.append(con.copy()) 
        pasosCaballo[i]['id'] = NumeroCaballo
        

        print(res)
        totalMoves += cont
        print(f"Movimientos : {cont}")

        res = Traductor(res)
        ImprimirTablero(res,NumeroCaballo)

    print("*************** MATRIZ FINAL *****************\n")

    pasosCaballo = Traductor(pasosCaballo)
    MatrizFinal(pasosCaballo)
    print(f"\nTotal Movimientos: {totalMoves}")

# Retorna un boolean que verifica si el juego termina esto significa que verifica 
# que se cubrieon las posiciones adyacentes a rey y se lo cubre a el
def FinalizarJuego(vectorJaque):

    global E_actual, Rey

    for i,elemento in enumerate(E_actual):
        movimientos = MovimientoCaballo(elemento)
        for j in movimientos:
            if j == Rey[0]:
                return True and FinalizacionVectorJaque(vectorJaque)
    
    return False


# Retorna un boolean que verifica si se cubrieron todas las posiciones del rey
# menos a el 
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

# Retorna el valor heuristica segun como se planteo la heuristica
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
    if len(interseccionRey_Mov) > 0 and FinalizacionVectorJaque(vectorjaque):
        herustica -= 10
    # Sumar 900 pts si se cubre al rey y no esta completado el vector jaque 
    if len(interseccionRey_Mov) > 0 and not FinalizacionVectorJaque(vectorjaque):
        herustica += 900
    # Sumar 900 pts si la posicion del caballo actual esta encima del vector jaque
    if CaballoActual in vectorjaque :
        herustica += 900
    if CaballoActual in Rey:
        herustica += 900

    return herustica


# Retorna una lista con los posibles movimientos filtrados de un caballo en cierta posicion 
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

# Organiza el orden de los caballos
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

# Crea una lista que contiene las posiciones a cubir de rey
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

# Imprime el tablero de ajedrez con la posicion inicial de cada caballo
def ImprimirTablero(caballos,i=0):
    
    for y in range(8,0,-1):
        for x in range(1,9):
            coordenada = {"x": x,"y":y}
            if i == 0:
                if coordenada in caballos:
                    print(f"|{caballos.index(coordenada)+1}|",end="")
                elif coordenada in Rey:
                    print(f"|R|",end="")
                else:
                    print("|_|",end="")
            else:
                if coordenada in caballos:
                    print(f"|{i}|",end="")
                elif coordenada in Rey:
                    print(f"|R|",end="")
                else:
                    print("|_|",end="")
            

        print()
    
    print("\n")

# Imprime el jaque mate del rey
def MatrizFinal(caballos):

    for y in range(8,0,-1):
        for x in range(1,9):
            flat = True
            coordenada = {"x": x,"y":y}
            for i in caballos:
                if coordenada == {"x":i['x'],"y":i['y']}:
                    print(f"|{i['id']}|",end="")
                    flat = False
            if coordenada in Rey:
                print(f"|R|",end="")
            elif flat:
                print("|_|",end="")

        print()

# Cambia las coordenas que entran en letras por numeros
def Traductor(posicion):

    Numlet = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H"}
    letNum = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}

    if type(posicion[0]["x"]) == str:
        for i in posicion:
            i["x"] = letNum.get(i["x"])
    else:

        for i in posicion:
            i["x"] = Numlet.get(i["x"])

    return posicion

# Funcion Principal
def main ():

    global Caballos, Rey, Abiertos, Cerrados, E_actual, indice

    H_totales = []
    H_inicial = 0


    vectorJaque = []
    
    #Iniciacion de variables 
    # Caballos = [{"x": "A", "y": 1},
    #             {"x": "A", "y": 3},
    #             {"x": "F", "y": 5},
    #             {"x": "C", "y": 3}
    #             ] 
    # Rey = [{"x": "E", "y": 1}]


    # ******************INGRESAR LOS EJES X EN LETRAS MAYUSCULAS Y LOS EJES Y EN NUMEROS*****************

    for i in range(1,5):
        print(f"\nIngrese las posiciones del caballo {i}")
        x = input("Eje x: ")
        y = int(input("Eje y: "))
        Caballos.append({"x":x,"y":y})

    Rey.append({"x":input("\nIngrese la posicion en x del rey: "),"y":int(input("Ingrese la posicion en y del rey: "))})
    

    CaballosIniciales = Caballos.copy()
    # Traduccion de letras a numeros
    Caballos = Traductor(Caballos)
    Rey = Traductor(Rey)

    # Impresion del tablero de ajedrez
    print("\n************** POSICIONES INICIALES *****************\n")
    ImprimirTablero(Caballos)
    
    # Creacion del vector Jaque donde se guradan las posiciones que se deben cubrir los caballos
    vectorJaque = VectorJaque(Rey)

    # Organizacion de los turnos de los caballos
    Caballos = OrderVector(Caballos,vectorJaque)

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
            # Se añade el EA a los cerrados
            Cerrados[i] += [elemento]
            # Se generan los posibles estados
            movimientosParciales = MovimientoCaballo(elemento)

            # Calculo de la la heristica de cada estado
            for j in movimientosParciales:
                j["h"] = ValorHeuristica(j,vectorJaque)
                j["padre"] = elemento

            # Se añaden los estados generados a la lista abierta
            Abiertos[i] = agregar_o_reemplazar(Abiertos[i], movimientosParciales)

            # Se selecciona el estado con menor valor heuristico
            menorAbiertos = min(Abiertos[i], key= lambda x:x["h"])

            # Si la coordenada del estado con menor valor heuristico seleccinado esta ocupada por otro caballo
            # se suma 900 pts a su heuristica 
            for s in E_actual:
                if {"x":s["x"],"y":s["y"]} == {"x":menorAbiertos["x"],"y":menorAbiertos["y"]}:
                    indice = Abiertos[i].index(menorAbiertos)
                    Abiertos[i][indice]["h"] += 900
                    menorAbiertos = min(Abiertos[i], key= lambda x:x["h"])

            auxE_actuales[i] = menorAbiertos.copy()

            for j in auxE_actuales:
                heuristicaAux += j["h"]

            aux = menorAbiertos.copy()

            aux["Htotal"] = heuristicaAux
            H_totales[i] = aux

        

        menorTotales = min(H_totales, key= lambda x:x["Htotal"])

        indice = H_totales.index(menorTotales)

        E_actual[indice] = menorTotales

        del menorTotales['Htotal']

        del Abiertos[indice][Abiertos[indice].index(menorTotales)]


        # Se actulicen los estados actuales
        # Elimina es estado actual de la lista abierta
        # for j,elemento in enumerate(E_actual):

            # if elemento["x"] == menorTotales["padre"]["x"] and elemento["y"] == menorTotales["padre"]["y"] and elemento["h"] == menorTotales["padre"]["h"]:
            #     aux = {"x":menorTotales["x"],"y":menorTotales["y"],"h":menorTotales["h"],"padre":E_actual[j]}
            #     del Abiertos[j][Abiertos[j].index(aux)]
            #     E_actual[j] = {"x":menorTotales["x"], "y":menorTotales["y"], "h":menorTotales["h"],"padre":E_actual[j]}
            # if elemento["padre"] != None:
            #     if elemento["padre"]["x"] == menorTotales["padre"]["x"] and elemento["padre"]["y"] == menorTotales["padre"]["y"] and elemento["padre"]["h"] == menorTotales["padre"]["h"]:
            #         aux = {"x":menorTotales["x"],"y":menorTotales["y"],"h":menorTotales["h"],"padre":menorTotales["padre"]}
            #         del Abiertos[j][Abiertos[j].index(aux)]
            #         E_actual[j] = aux

                

    # Imprime la trayectoria de cada caballo
    VerMovivientosCaballos(CaballosIniciales)

main()






