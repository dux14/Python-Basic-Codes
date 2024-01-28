# i es la variable
# siempre los valores nuevos se van a escribir en la varibale
# range nos lista numeros dentro de i en un rango de 0 a 4
for i in range(5):
    print(i)

# mientras que x sea menor que 5 se va a imprimir y se va a adicionar 1 hasta que no se cumpla la condicion
x = 0

while x < 5:
    print(x)
    x += 1

# bucles anidados
my_list = [[1, 4, 5], [2, 6, 8], [9, 4, 1]]

for element in my_list:
    print(f"\n[+] Vamos a desglosar la lista {element}\n")
    for element_in_list in element:
        print(element_in_list)

# lista de comprension
odd_list = [1, 3, 5, 7, 9]
cuadrado = [i ** 2 for i in odd_list]

# break y continue
for i in range(10):
    print(i)
    if i == 5:
        break

for i in range(10):
    if i == 5:
        continue
    print(i)

# combinando
numbers = [2, 4, 6, 8, 10, 7, 12, 14]
todos_son_pares = True

for number in numbers:
    if number & 2 != 0:
        todos_son_pares = False
    break

if todos_son_pares:
    print("Todos los elementos de la lista son pares")
else:
    print("Alguno de los elementos de la lista es impar")
