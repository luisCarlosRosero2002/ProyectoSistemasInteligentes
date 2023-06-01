
# Cerrados = []
# Abiertos = []
# Eactual = []

Pfinales = [0,0,0,0]
Cubiertas  = [[],[],[],[]]
CubiertasAntes  = [[],[],[],[]]
indice = 0 



def verificacionVectorJaque(vectorJaque,caballoActual,rey):
    aux = False
    Pmovimientos = movimientoCaballo(caballoActual)

    Cubierta = finalizacionVectorJaque(vectorJaque)

    for i in Pmovimientos:
        if rey[0] == i:
            aux = True and Cubierta
        # for j in Cubiertas:
        #     for l in j:
        #         if i == l:
        #             aux = True
    
    return aux

# Hace que una caballo no cubra una casilla que otro caballo ya cubre
def verificarCubiertasRepetidas(interseccion, cubiertas):
    for i in interseccion:
        for j in cubiertas:
            for l in j:
                if i == l:
                    return True
    return False

def finalizacionVectorJaque(vectorJaque,PMovimientos,rey):
    if not Cubiertas[0] == 0 and not Cubiertas[1] == 0 and not Cubiertas[2] == 0 and not Cubiertas[3] == 0 :
        
        CubiertasAntes = Cubiertas
        conjunto_diccionarios = set()

        conjunto_moves = {tuple(d.items()) for d in PMovimientos}
        conjunto_vectorjaque = {tuple(d.items()) for d in vectorJaque}
        conjuntoRey = set(tuple(sorted(diccionario.items())) for diccionario in rey)
        interseccion = conjunto_moves & (conjunto_vectorjaque | conjuntoRey)
        interseccion = [dict(tupla) for tupla in interseccion]

        Cubiertas [indice] = interseccion


        for lista in Cubiertas:
            for diccionario in lista:
                conjunto_diccionarios.add(tuple(diccionario.items()))

        lista_diccionarios = [dict(items) for items in conjunto_diccionarios]

        conjunto_1 = set(frozenset(diccionario.items()) for diccionario in lista_diccionarios)
        conjunto_2 = set(frozenset(diccionario.items()) for diccionario in vectorJaque)
        conjunto_3 = set(frozenset(diccionario.items()) for diccionario in rey)




        if conjunto_1 ==  conjunto_2  : return True
        elif conjunto_1 == (conjunto_2 | conjunto_3 ): return True
        else: return False

    return False



def finalizacionVectorJaqueYRey(rey):

    if not Cubiertas[0] == 0 and not Cubiertas[1] == 0 and not Cubiertas[2] == 0 and not Cubiertas[3] == 0 :
        
        # existe = False
        # for i in Cubiertas:
        #     for j in i:
        #         if j  == rey[0]:
        #             existe =  True
        #             break
        # for lista in Cubiertas:
        #     if lista == vectorJaque:
        #         return True
        conjunto_diccionarios = set()

        for lista in Cubiertas:
            for diccionario in lista:
                conjunto_diccionarios.add(tuple(diccionario.items()))

        lista_diccionarios = [dict(items) for items in conjunto_diccionarios]

        # conjunto_1 = set(frozenset(diccionario.items()) for diccionario in lista_diccionarios)
        # conjunto_2 = set(frozenset(diccionario.items()) for diccionario in vectorJaque)
        # conjunto_3 = set(frozenset(diccionario.items()) for diccionario in rey)

        if rey[0] in  lista_diccionarios  : return True
        else: return False

    return False

def filtadrorMovimientos(movimientos,rey,vectorjaque):
    aux = False
    for i in movimientos:
        if rey[0] == i and not Cubiertas == vectorjaque: 
            aux = True
    
    return aux



def ValorHeuristica(CaballoActual,rey,vectorjaque):

    herustica = (abs( rey[0]["x"] - CaballoActual["x"] ) + abs( rey[0]["y"] -  CaballoActual["y"]) )* 10
    

    # if CaballoActual == Eactual :
        # ejecucion += 1
    PMovimientos = movimientoCaballo(CaballoActual)

    conjunto_PMovimientos = {tuple(d.items()) for d in PMovimientos}
    conjunto_vectorjaque = {tuple(d.items()) for d in vectorjaque}
    conjunto_rey = {tuple(d.items()) for d in rey}

    interseccion = conjunto_PMovimientos & conjunto_vectorjaque 
    interseccion = [dict(tupla) for tupla in interseccion]

    interseccion2 = conjunto_PMovimientos & conjunto_rey
    interseccion2 = [dict(tupla) for tupla in interseccion2]

    # corregir
    repetidos = verificarCubiertasRepetidas(interseccion,Cubiertas)
# 
    if len(interseccion) > 0 and not repetidos:
        herustica -= len(interseccion) * 10

    if rey[0] in PMovimientos and finalizacionVectorJaque(vectorjaque,PMovimientos,rey):
        # if len(interseccion2) and not finalizacionVectorJaque(vectorjaque,PMovimientos,rey):
        #     herustica +=10
        # elif len(interseccion2) and finalizacionVectorJaque(vectorjaque,PMovimientos,rey):
        #     herustica -=10
        # else:
            herustica -=10

    #Corregir por que aveces suma en ves de restar       
    if not finalizacionVectorJaque(vectorjaque,PMovimientos,rey):
        
        if rey[0] in PMovimientos and not finalizacionVectorJaque(vectorjaque,PMovimientos,rey):
            herustica +=10
        
        if CaballoActual in vectorjaque :
            herustica +=10
    # 
        if repetidos:
            herustica +=10




    


    return herustica
    
    

def movimientoCaballo(caballo):

    movimientos = []

    movimientos.append({"x":(caballo["x"])-1,"y":(caballo["y"])+2,
                        # "h": ValorHeuristica({"x":(caballo["x"])-1,"y":(caballo["y"])+2},rey,vectorjaque)
                        })
    
    movimientos.append({"x":(caballo["x"])-2,"y":(caballo["y"])+1,
                        # "h": ValorHeuristica({"x":(caballo["x"])-2,"y":(caballo["y"])+1},rey,vectorjaque)
                        }
                        )
    
    movimientos.append({"x":(caballo["x"]) -2,"y":(caballo["y"])-1,
                        # "h": ValorHeuristica({"x":(caballo["x"])-2,"y":(caballo["y"])-1},rey,vectorjaque)
                        })
    
    movimientos.append({"x":(caballo["x"])-1,"y":(caballo["y"])-2,
                        # "h": ValorHeuristica({"x":(caballo["x"])-1,"y":(caballo["y"])-2},rey,vectorjaque)
                        })
    
    movimientos.append({"x":(caballo["x"])+1,"y":(caballo["y"])-2,
                        # "h": ValorHeuristica({"x":(caballo["x"])+1,"y":(caballo["y"])-2},rey,vectorjaque)
                        })
    
    movimientos.append({"x":(caballo["x"])+2,"y":(caballo["y"])-1,
                        # "h": ValorHeuristica({"x":(caballo["x"])+2,"y":(caballo["y"])-1},rey,vectorjaque)
                        })
    
    movimientos.append({"x":(caballo["x"])+2,"y":(caballo["y"])+1,
                        # "h": ValorHeuristica({"x":(caballo["x"])+2,"y":(caballo["y"])+1},rey,vectorjaque)
                        })
    
    movimientos.append({"x":(caballo["x"])+1,"y":(caballo["y"])+2,
                        # "h": ValorHeuristica({"x":(caballo["x"])+1,"y":(caballo["y"])+2},rey,vectorjaque)
                        })
    
    movimientos = list(filter(lambda elemento: (elemento["x"] < 9 and elemento["x"] > 0)  and  (elemento["y"] < 9 and elemento["y"] > 0 ) , movimientos))
    movimientos = list(filter(lambda elemento: elemento not in Pfinales , movimientos))


    # movimientos = list(filter(lambda elemento: elemento not in vectorjaque , movimientos))
    # movimientos = list(filter(lambda elemento: elemento not in rey , movimientos))

    return movimientos

def orderVector(caballos,rey,vector_jaque):

    resultado = []
    aux = []

    for i in caballos:
        
        if i in vector_jaque:
            aux.append({"x":i["x"], "y":i["y"], "h": ValorHeuristica(i , rey , vector_jaque)})
        else:
            resultado.append({"x":i["x"], "y":i["y"], "h": ValorHeuristica(i , rey , vector_jaque)})

    resultado.sort(key = lambda x: x["h"],reverse=True)
    resultado = aux + resultado

    return resultado

            
def vectorJaque(rey):

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

def imprimirTablero(caballos, rey):
    
    
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
    
def traductor(posicion):

    Numlet = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H"}
    letNum = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}

    respuesta = []
    for i in posicion:
        respuesta.append({"x":(letNum.get(i["x"])),"y":i["y"]})

    return respuesta


def main():

    global indice

    Abiertos =[[],[],[],[]]
    Cerrados =[[],[],[],[]]

    # Caballos = [{"x": "A", "y": 8},{"x": "E", "y": 8},{"x": "H", "y": 8},
    #             {"x": "B", "y": 5}] 
    Caballos = [{"id":1,"x": "A", "y": 8},{"id":2,"x": "H", "y": 8},{"id":3,"x": "H", "y": 1},
                {"id":4,"x": "D", "y": 5}] 
    Rey = [{"x": "B", "y": 1}]
    # for i in range(1,5):
    #     print(f"\nIngrese las posiciones del caballo {i}")
    #     Caballos.append({"x":input("Eje x: "),
    #             "y":int(input("Eje y: "))})

    # while True:
    #     Rey.append({"x":input("\nIngrese la posicion en x del rey: "),
    #                 "y":int(input("Ingrese la posicion en y del rey: "))})
    #     if (Rey[0]["x"] == "H" or Rey[0]["x"] == "A") and (Rey[0]["y"] == "1" or Rey[0]["y"] == "8"):
    #         break
    #     print("Posiciones invalidas del rey")
    Caballos = traductor(Caballos)

    Rey = traductor(Rey)

    imprimirTablero(Caballos, Rey)

    vector_jaque = vectorJaque(Rey)

    Caballos = orderVector(Caballos,Rey,vector_jaque)

    # print(Caballos)

    Pparciales = Caballos
    
    while True:
        # Si el vector jaque esta cubierto y el rey salir de los ciclos

        if  finalizacionVectorJaqueYRey(Rey) : break

        for i,elemento in enumerate(Pparciales):
            indice = i
            Eactual = elemento
            Cerrados[i] += [elemento]
            CubiertasAntes = Cubiertas.copy()
            movimientosParciales = movimientoCaballo(Eactual)
            # Se filtra solo lo movimientos donde no esten los caballos 
            movimientosParciales = list(filter(lambda elemento: elemento not in Caballos , movimientosParciales))
            movimientosFiltradosParciales = list(filter(lambda elemento: elemento not in Rey , movimientosParciales))
            movimientosFiltradosParciales = list(filter(lambda elemento: elemento not in vector_jaque , movimientosFiltradosParciales))
    
            Abiertos[i] += movimientosFiltradosParciales

            # Se crean conjuntos para aplicar teoria de conjuntos
            conjunto_moves = {tuple(d.items()) for d in movimientosParciales}
            conjunto_vectorjaque = {tuple(d.items()) for d in vector_jaque}
            conjuntoRey = set(tuple(sorted(diccionario.items())) for diccionario in Rey)
            interseccion = conjunto_moves & (conjunto_vectorjaque | conjuntoRey)
            interseccion = [dict(tupla) for tupla in interseccion]
            Cubiertas [i] = interseccion
            # Se calcula la heuristica de los movimientos parciales
            for j in movimientosFiltradosParciales:
                j["h"] = ValorHeuristica(j,Rey,vector_jaque)
            # Se almacenan las posiciones cubiertas hasta el momento del vector jaque y el rey
           
            # repetidos = any(elemento in Cubiertas for elemento in interseccion)
            # Calcular el minimo de los abiertos
            
            while True:

                menorAbiertos = min(Abiertos[i], key= lambda x:x["h"])
                movimientosSiguientes = movimientoCaballo(menorAbiertos)

                Eactual = menorAbiertos if menorAbiertos["h"] < elemento["h"] else elemento
                


                if elemento != Eactual:
                    movimientosParciales = movimientoCaballo(Eactual)
                    conjunto_moves = {tuple(d.items()) for d in movimientosParciales}
                    interseccion = conjunto_moves & (conjunto_vectorjaque | conjuntoRey)
                    estado = filtadrorMovimientos(movimientosSiguientes,Rey,vector_jaque)
                    if not estado : break
                    elif finalizacionVectorJaque(vector_jaque,movimientosParciales,Rey) : break
                    else: del Abiertos[i][Abiertos[i].index(menorAbiertos)]
                else: break


                # conjunto_moves = {tuple(d.items()) for d in movimientosSiguientes}
                # interseccion = conjunto_moves & (conjunto_vectorjaque | conjuntoRey)
                # interseccion = [dict(tupla) for tupla in interseccion]
                # Cubiertas [i] = interseccion
                # estado = filtadrorMovimientos(movimientosSiguientes,Rey,vector_jaque)
            
            # Se asigna el estado con menor heuristica si no es menor de deja el mismo estado 
            # Eactual = menorAbiertos if menorAbiertos["h"] < Eactual["h"] else Eactual

            # if elemento != Eactual:
            #     movimientosParciales = movimientoCaballo(Eactual,Rey,vector_jaque)
            #     conjunto_moves = {tuple(d.items()) for d in movimientosParciales}
            #     interseccion = conjunto_moves & (conjunto_vectorjaque | conjuntoRey)


            interseccion = [dict(tupla) for tupla in interseccion]
            
            Pfinales[i] = {"x":Eactual["x"], "y":Eactual["y"]}

            
            Cubiertas [i] = interseccion

            Pparciales [i] = Eactual

            # movimientosParciales = list(filter(lambda elemento: elemento not in vector_jaque , movimientosParciales))
            # movimientosParciales = list(filter(lambda elemento: elemento not in Rey , movimientosParciales))
            # Abiertos.clear()
            # print(movimientosParciales)
        print(Pparciales)
            






    
    # for i in Caballos:



        # global flat
        # Eactual = i
        # Cerrados.clear()

        # if Caballos[len(Caballos)-1] == i : flat = True
        # while True :

        #     movimientosParciales = movimientoCaballo(Eactual,Rey,vector_jaque)
        #     Abiertos.extend(movimientosParciales)

        #     movimientosParciales = list(filter(lambda elemento: elemento not in Caballos , movimientosParciales))
        #     conjunto_moves = {tuple(d.items()) for d in movimientosParciales}
        #     conjunto_vectorjaque = {tuple(d.items()) for d in vector_jaque}
        #     # conjuntoCubiertas = set(tuple(sorted(diccionario.items())) for diccionario in Cubiertas)
        #     conjuntoRey = set(tuple(sorted(diccionario.items())) for diccionario in Rey)

        #     interseccion = conjunto_moves & (conjunto_vectorjaque | conjuntoRey)

        #     for j in movimientosParciales:
        #         j["h"] = ValorHeuristica(j,Rey,vector_jaque)

        #     Cerrados.append(Eactual)
        #     interseccion = [dict(tupla) for tupla in interseccion]

        #     repetidos = any(elemento in Cubiertas for elemento in interseccion)

        #     if (len(interseccion) > 0) and ({"x":Eactual["x"],"y":Eactual["y"]} not in vector_jaque) and not(repetidos) : 
        #         aux = min(Abiertos, key= lambda x:x["h"])

        #         if aux["h"] <= Eactual["h"] :
        #             movimientosParciales = movimientoCaballo(aux,Rey,vector_jaque)
        #             movimientosParciales = list(filter(lambda elemento: elemento not in Caballos , movimientosParciales))
        #             conjunto_moves = {tuple(d.items()) for d in movimientosParciales}
        #             interseccion = conjunto_moves & (conjunto_vectorjaque | conjuntoRey)
        #             Cerrados.append(aux)
        #             interseccion = [dict(tupla) for tupla in interseccion]
        #             Cubiertas.extend(interseccion)
        #             Pfinales.append({"x":aux["x"],"y":aux["y"]})
        #             if (len(interseccion) > 0):
        #                 break


        #     Abiertos.sort(key= lambda x:x["h"])
        #     Eactual = min(Abiertos, key= lambda x:x["h"])
            
        #     del Abiertos[Abiertos.index(Eactual)]

        
        # print(Cerrados)
        # Abiertos.clear()

        

main()




