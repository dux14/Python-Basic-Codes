# funciones

def saludo(nombre):
    print(f"Hola {nombre}")


saludo('Samuel')


def suma(x, y):
    return x + y


resultado = suma(2, 8)
print(f"El resultado de la suma es: {resultado}")


def mi_function():
    variable_local = "Soy local"
    print(variable_local)


mi_function()


variable = "Soy global"


def mi_function():
    global variable
    variable = "Soy global y he sido modificado"
    print(variable)


mi_function()
print(variable)
