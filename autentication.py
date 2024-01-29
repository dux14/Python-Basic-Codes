import random

def generar_contrasena():

    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    caracteres = numeros

    contrasena = []

    for i in range(3):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena + " " + contrasena)


if __name__ == "__main__":
    run()

    # linea para revisar el pusb