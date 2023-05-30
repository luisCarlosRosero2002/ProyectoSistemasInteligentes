
Cerrados = []
Abiertos = []
Eactual = []
Pfinales = []
CRey = []
flat = False

def ValorHeuristica(CaballoActual,rey,vectorjaque):

    herustica = (abs( rey[0]["x"] - CaballoActual["x"] ) + abs( rey[0]["y"] -  CaballoActual["y"]) )* 10
    

    # if CaballoActual == Eactual :
        # ejecucion += 1
    PMovimientos = movimientoCaballo(CaballoActual,rey,vectorjaque)

    conjunto_PMovimientos = {tuple(d.items()) for d in PMovimientos}
    conjunto_vectorjaque = {tuple(d.items()) for d in vectorjaque}
    # conjunto_rey = {tuple(d.items()) for d in rey}

    interseccion = conjunto_PMovimientos & conjunto_vectorjaque
    interseccion = [dict(tupla) for tupla in interseccion]
    repetidos = any(elemento in CRey for elemento in interseccion)
# 
    if len(interseccion) > 0 and not repetidos:
        herustica -= len(interseccion) * 10

    if rey[0] in PMovimientos and not flat :
        herustica +=50

    if rey[0] in PMovimientos and  flat:
        herustica -=50

    if CaballoActual in vectorjaque :
        herustica +=50
# 
    if repetidos:
        herustica +=50




    


    return herustica
    
    

def movimientoCaballo(caballo , rey , vectorjaque):

    movimientos = []
    global Abiertos, Eactual

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
    # Abiertos.extend(movimientos)
    # Abiertos.sort(key = lambda x: x["h"], reverse=True)

    # Eactual = min(Abiertos, key= lambda x: x["h"])

    # print(Abiertos)

    return movimientos

def orderVector(caballos,rey,vector_jaque):

    global Eactual ,Cerrados
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

    Caballos = [{"x": "A", "y": 8},{"x": "E", "y": 8},{"x": "H", "y": 8},
                {"x": "B", "y": 5}] 
    # Caballos = [{"x": "H", "y": 1}] 
    Rey = [{"x": "E", "y": 1}]
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

    print(Caballos)
    
    for i in Caballos:

        global flat
        Eactual = i
        Cerrados.clear()

        if Caballos[len(Caballos)-1] == i : flat = True
        while True :

            movimientosParciales = movimientoCaballo(Eactual,Rey,vector_jaque)
            Abiertos.extend(movimientosParciales)

            movimientosParciales = list(filter(lambda elemento: elemento not in Caballos , movimientosParciales))
            conjunto_moves = {tuple(d.items()) for d in movimientosParciales}
            conjunto_vectorjaque = {tuple(d.items()) for d in vector_jaque}
            # conjuntoCubiertas = set(tuple(sorted(diccionario.items())) for diccionario in CRey)
            conjuntoRey = set(tuple(sorted(diccionario.items())) for diccionario in Rey)

            interseccion = conjunto_moves & (conjunto_vectorjaque | conjuntoRey)

            for j in movimientosParciales:
                j["h"] = ValorHeuristica(j,Rey,vector_jaque)

            Cerrados.append(Eactual)
            interseccion = [dict(tupla) for tupla in interseccion]

            repetidos = any(elemento in CRey for elemento in interseccion)

            if (len(interseccion) > 0) and ({"x":Eactual["x"],"y":Eactual["y"]} not in vector_jaque) and not(repetidos) : 
                aux = min(Abiertos, key= lambda x:x["h"])

                if aux["h"] <= Eactual["h"] :
                    movimientosParciales = movimientoCaballo(aux,Rey,vector_jaque)
                    movimientosParciales = list(filter(lambda elemento: elemento not in Caballos , movimientosParciales))
                    conjunto_moves = {tuple(d.items()) for d in movimientosParciales}
                    interseccion = conjunto_moves & (conjunto_vectorjaque | conjuntoRey)
                    Cerrados.append(aux)
                    interseccion = [dict(tupla) for tupla in interseccion]
                    CRey.extend(interseccion)
                    Pfinales.append({"x":aux["x"],"y":aux["y"]})
                    if (len(interseccion) > 0):
                        break


            Abiertos.sort(key= lambda x:x["h"])
            Eactual = min(Abiertos, key= lambda x:x["h"])
            
            del Abiertos[Abiertos.index(Eactual)]

        
        print(Cerrados)
        Abiertos.clear()

        

main()




