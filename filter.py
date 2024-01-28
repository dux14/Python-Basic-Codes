numbers = [1, 2, 3, 4, 5]

odd_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(odd_numbers)

# filter se le pasa 2 parametros una funcion o un condicional y un objeto iterable en este caso una lista
# para nuestro ejemplo queremos traer los elementos pares de mi lista numbers
# filter solo va a mostrar en odd_numbers los valores de numbers que cumplan el condicional que le pasamos
