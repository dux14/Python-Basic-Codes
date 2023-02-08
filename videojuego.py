import random

def run():
    numero_aleatorio = random.randint(1,100) #Numero generado por rng
    numero_elegido = int(input("Elige un numero del 1 al 100: ")) #Opcion de usuario
    while numero_elegido != numero_aleatorio: #se hace la comparacion
        if numero_elegido < numero_aleatorio:
            print("Busca un numero mas grande")
        else:
            print("Busca un numero mas pequeño")
        numero_elegido = int(input("Elige otro numero: "))  
    print("Ganaste")


if __name__ == "__main__":
    run()