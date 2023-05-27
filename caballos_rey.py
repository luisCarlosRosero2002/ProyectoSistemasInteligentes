
Cerrados = []
Abiertos = []
Eactual = []

def ValorHeuristica(CaballoActual,rey,vectorjaque):

    herustica = (abs( rey[0]["x"] - CaballoActual["x"] ) + abs( rey[0]["y"] -  CaballoActual["y"]) )* 10
    

    # if CaballoActual == Eactual :
        # ejecucion += 1
    PMovimientos = movimientoCaballo(CaballoActual,rey,vectorjaque)

    conjunto_PMovimientos = {tuple(d.items()) for d in PMovimientos}
    conjunto_vectorjaque = {tuple(d.items()) for d in vectorjaque}
    # conjunto_rey = {tuple(d.items()) for d in rey}


    union = conjunto_PMovimientos & conjunto_vectorjaque

    if len(union) > 0:
        herustica -= len(union) * 10

    if rey[0] in PMovimientos:
        herustica +=50

    if CaballoActual in vectorjaque :
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
    # Caballos = []
    # Rey = []
    # vector_jaque = []
    Caballos = [{"x": "A", "y": 8},{"x": "H", "y": 7},{"x": "G", "y": 1},
                {"x": "H", "y": 1}] 
    # Caballos = [{"x": "H", "y": 1}] 
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

    print(Caballos)
    
    for i in Caballos:

        # moves = movimientoCaballo(i,Rey,vector_jaque)
        Eactual = i

        while True :

            movimientosParciales = movimientoCaballo(Eactual,Rey,vector_jaque)
            conjunto_moves = {tuple(d.items()) for d in movimientosParciales}
            conjunto_vectorjaque = {tuple(d.items()) for d in vector_jaque}
            union = conjunto_moves & conjunto_vectorjaque

            for j in movimientosParciales:
                j["h"] = ValorHeuristica(j,Rey,vector_jaque)
            
            print(movimientosParciales)

            nodoPadre = Eactual
            menor = min(movimientosParciales, key= lambda x:x["h"])
            Eactual = menor if menor["h"] < Eactual["h"] else Eactual
            
            print(Eactual)
            if Eactual["h"] <= nodoPadre["h"] and len(union) > 0 : break



    # print(movimientosParciales)

    print(Caballos)





main()
# imprimirTablero()



