from ast import Num


def run():
    num_1 = int(input("Escribe tu edad jugador 1: "))
    num_2 = int(input("Escribe tu edad jugador 2: "))

    nombre_1 = input("Escribe tu nombre jugador 1: ")
    nombre_2 = input("Escribe tu nombre jugador 2: ")

    if num_1 > num_2:
        print("La edad de "+ nombre_1 +" Es mayor que la de "+ nombre_2)
    elif num_1 == num_2:
        print("La edad de "+ nombre_1 +" Es igual que la de "+ nombre_2)
    else:
        print("La edad de "+ nombre_1 +" Es menor que la de "+ nombre_2)

if __name__ == "__main__":
    run()