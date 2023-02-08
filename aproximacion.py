def run():
    objetivo = int(input("Escoge un numero: ")) #Se le pide el valor al usuario
    epsilon = 0.01 #Que tan cerca esto de la respuesta
    paso = epsilon**2 #Que tanto nos acercamos en cada iteracion
    respuesta = 0.0 #la respuesta

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        #cada vez nos acercamos mas al objetivo                    Evita numeros negativos
       
        respuesta += paso
    

    
    if abs(respuesta**2  - objetivo)>=epsilon:
        print(f"No se encontro la raiz cuadrada de {objetivo}")
    else:
        print(f"La raiz cuadrada de {objetivo} es {respuesta}")




if __name__ == "__main__":
    run()