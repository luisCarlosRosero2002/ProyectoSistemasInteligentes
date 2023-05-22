Numlet = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H"}
letNum = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}


# def herustica():

# def movimientoCaballo(caballos , rey , vectorjaque):



def orderVector(caballos,rey):
    resultado = []

    for i in caballos:
        distancia = ((abs( letNum.get(rey[0]["x"]) - letNum.get(i["x"]) ) ) + abs(( rey[0]["y"]- i["y"]))) * 10
        resultado.append({"x":i["x"], "y":i["y"], "distancia": distancia})

    resultado.sort(key = lambda x: x["distancia"])
    return resultado

            
def vectorJaque(rey):

    posiciones = []

    posiciones.append({"x":(letNum.get(rey[0]["x"]))-1,"y":rey[0]["y"]})
    posiciones.append({"x":(letNum.get(rey[0]["x"]))+1,"y":rey[0]["y"]+1})
    posiciones.append({"x":(letNum.get(rey[0]["x"])),"y":rey[0]["y"]+1})
    posiciones.append({"x":(letNum.get(rey[0]["x"]))-1,"y":rey[0]["y"]+1})
    posiciones.append({"x":(letNum.get(rey[0]["x"]))+1,"y":rey[0]["y"]})
    posiciones.append({"x":(letNum.get(rey[0]["x"]))+1,"y":rey[0]["y"]-1})
    posiciones.append({"x":(letNum.get(rey[0]["x"])),"y":rey[0]["y"]-1})
    posiciones.append({"x":(letNum.get(rey[0]["x"]))-1,"y":rey[0]["y"]-1})

    return list(
        map(lambda objeto : {"x":Numlet.get(objeto["x"]),"y":objeto["y"]},
            filter(
                lambda elemento: (elemento["x"] < 9 and elemento["x"] > 0)  and  (elemento["y"] < 9 and elemento["y"] > 0 ) , posiciones)
            )
        )

def imprimirTablero(caballos, rey):
    
    
    for y in range(8,0,-1):
        for x in range(1,9):
            coordenada = {"x": Numlet.get(x),"y":y}
            if coordenada in caballos:
                print(f"|{caballos.index(coordenada)+1}|",end="")
            elif coordenada in rey:
                print(f"|R|",end="")
            else:
                print("|_|",end="")
        print()
    


def main():
    # Caballos = []
    # Rey = []
    # vector_jaque = []
    Caballos = [{"x": "C", "y": 7},{"x": "E", "y": 8},{"x": "D", "y": 6},
                {"x": "H", "y": 1}] 
    Rey = [{"x": "D", "y": 8}]
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
   
    imprimirTablero(Caballos, Rey)
    vector_jaque = vectorJaque(Rey)
    Caballos = orderVector(Caballos,Rey)
    # movimientoCaballo(Caballos,Rey,vector_jaque)

    print(Caballos)





main()
# imprimirTablero()



