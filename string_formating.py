name = "dux"
edad = 18

print('Hola me llamo %s y tengo %d' % (name, edad))  # %s para string y %d para numeros

# .format damos las variables a usar y dentro de {} el indice de cada una de las variables a usar
print("Hola me llamo {0} y tengo {1} de verdad tengo {1}".format(name, edad))

# poniendo f al comienzo ya podemos incrustar la variable dentro de las {}
print(f"Hola me llamo {name}")



