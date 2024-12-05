"""
1. Calcular precio y tipo en funcion de la edad y guardarlo en algun sitio para luego... OK

2. Pedir la edad -> OK
    Validar que sea entero positivo -> OK
    Pedir edades hasta que se introduzca ""

3. Calcular el precio total del grupo

4. mostrar el precio total y el desglose por tipo de entrada

"""

precioTotal = 0
grupoPersonas = []

GRATUITA = 0
NINYOS = 1
ADULTOS = 2
JUBILADOS = 3

def calculoPrecioYTipoBillete(edad: int):
    entrada = 0
    tipo = GRATUITA
    if edad >=3 and edad <= 12:
        entrada = 14
        tipo = NINYOS
    elif edad >= 13 and edad < 65:
        entrada = 23
        tipo = ADULTOS
    elif edad >= 65:
        entrada = 18
        tipo = JUBILADOS

    return entrada, tipo

def validaEnteroPositivo(dato: str):
    """
    Debe devolver True si dato es entero mayor o igual que cero
                  False en otro caso
    """
    res = False
    try:
        int(dato)
        res = True
    except ValueError:
        res = False
    return res


"""
Bucle de peticion de edades, para cada edad debe imprimir precio y tipo
y acabar cuando se introduzca ""
"""
while True:
    edad = input("Cuantos años tienes: ")
    if edad == "":
        break
    elif validaEnteroPositivo(edad):
        grupoPersonas.append(calculoPrecioYTipoBillete(int(edad)))

print(grupoPersonas)

