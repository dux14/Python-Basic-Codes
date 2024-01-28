mi_funcion = lambda: "Hola Mundo"

print(mi_funcion())

cuadrado_numero = lambda x: (x ** 2)

print(cuadrado_numero(89))

double_argument = lambda num1, num2: num1 + num2

print(double_argument(1, 3))

numbers = [1, 2, 3, 4, 5]

square_numbers = list(map(lambda x: x ** 2, numbers))
print(square_numbers)

numbers = [1, 2, 3, 4, 5]

odd_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(odd_numbers)

from functools import reduce
numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x * y, numbers)

print(result)