# [] Para decirle que es una lista
my_ports = []

# .append para agregar elementos a la lista, pero solo se puede 1 argumento por línea
my_ports.append(23)
my_ports.append(24)
my_ports.append(25)
my_ports.append(26)

# forma 2 de agregar elementos directamente en la lista
my_ports = [1, 2, 3, 4, 5, 6, 7, 8]

# forma 3 de agregar elementos .extend
my_ports.extend([1, 2, 3])

# forma 4 de agregar elementos
my_ports += [1, 3, 5]

# Índices van del 0,1,2,3,etc. para las listas
print(my_ports[1])

# forma optima para recorrer una lista es con un bucle for
for port in my_ports:
    print(port)

# len para decirle que me de la longitud de una variable
print(len(my_ports))

# sorted para organizar una lista
my_ports = sorted(my_ports)

# del para borrar elementos de una lista por el índice
del my_ports[0]

# [:X] te devuelve la cantidad de registros dados hasta ese valor
my_ports[:2]

# [0:0] te define el rango de valores a mostrar, pero el último es -1, en este caso solo muestra el 0,1
my_ports[0:2]

# [-x] te trae el valor de atras hacia delante
my_ports[-1]

# .insert(posicion a reemplzar, nuevo valor)
my_ports.insert(2, "hola")

# .pop elimina el ultimo registro
my_ports.pop()

# .index para saber el position por su valor, pero si hay repetidos solo te trae el mas cercano al comienzo
my_ports.index(5)

# enumerate() te permite saber el índice y el valor de una lista dentro de un objeto
enumerate(my_ports)

# .count para contar cuantas veces se repite un valor dentro de la lista
my_ports.count(12)