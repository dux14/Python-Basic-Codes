# lista iterable
numbers = [1, 2, 3, 4, 5]

# funcion que va a ser la iteradora


def suma(n):
    return n + n


result = map(suma, numbers)
print(list(result))

# map te permite usar listas y funciones en si misma como objetos, en donde la lista es el objeto iterable que va
# a ser usado por la funcion que le pasaste en este caso a numbers le pasamos la funcion suma
# dando por resultado la operacion de suma para numbers

