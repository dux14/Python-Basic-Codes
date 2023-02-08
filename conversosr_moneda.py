pesos_col = input("Cuantos pesos colombianos tienes?: ")
dolares = input("Cuantos dolares tienes?: ")
pesos_col = float(pesos_col)
dolares = float(dolares)
tipo_operacion = input("1. Convertir Cop a Usd 2. Convertir Usd a Cop \nQue deseas hacer?: ")



if tipo_operacion == "1":
    valor_dolar = pesos_col / 3930
    valor_dolar = round(valor_dolar,0)
    valor_dolar = str(valor_dolar)
    print("Tienes $"+valor_dolar+" Dolares")
else :
    valor_peso = dolares * 3930
    valor_peso = round(valor_peso,0)
    valor_peso = str(valor_peso)
    print("Tienes $"+valor_peso+" Pesos Colombianos")





