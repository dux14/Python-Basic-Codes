try:
    num = 5 / 0

except ZeroDivisionError:

    print('No Se puede dividir un numero entre 0')

except TypeError:

    print("Solo numeros para operaciones matematicas")

else:

    print(f"La division da {num}")

finally:

    print("Siempre estoy aqui")

x = -5

if x < 0:
    raise Exception("No se pueden usar numeros negativos")

