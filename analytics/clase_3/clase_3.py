# a,b = 10,20


# a = 10
# b = 20

# suma = a + b
# multiplicacion = a * b

# print(a, b, suma, multiplicacion)

# a2 = 30
# b2 = 50

# suma2 = a2 + b2
# multiplicacion2 = a2 * b2

# print(a2, b2, suma2, multiplicacion2)


def suma_multiplicacion(numero1, numero2):
    suma = numero1 + numero2
    multiplicacion = numero1 * numero2
    return (suma, multiplicacion)


# numero1, numero2 = 10, 20
# resultado = suma_multiplicacion(numero1, numero2)
# print(numero1, numero2, resultado)

# print(1, 2, suma_multiplicacion(1, 2))
# print(3, 4, suma_multiplicacion(3, 4))
# print(40, 50, suma_multiplicacion(40, 50))
# print(10, 5, suma_multiplicacion(10, 5))
# print(3, 6, suma_multiplicacion(3, 6))
# print(60, 10, suma_multiplicacion(60, 10))
# print(100, 1000, suma_multiplicacion(100, 1000))
# print(0, 1, suma_multiplicacion(0, 1))
# print(0, 0, suma_multiplicacion(0, 0))

numeros1 = (2, 4, 7, 4, 5, 4, 11, 8, 3, 10, 11, 985, 544)
numeros2 = (9, 8, 7, 6, 4, 6, 4, 5, 3, 1, 2, 3)
print(f"{numeros1=}")
print(f"{numeros2=}")
a = "hols"

print(f"{len(numeros1)=}")
print(f"{len(numeros2)=}")
# print(f"{len(a)=}")

# for numero in numeros1:
#     print(f"{numero=}")

# print(numeros1[0])


# print(list(range(9)))
# print(list(range(1, 9)))
# print(list(range(2, 9, 2)))

# for i in range(len(numeros1)):
#     resultado = suma_multiplicacion(numeros1[i], numeros2[i])
#     print(numeros1[i], numeros2[i], resultado)


# for i, numero in enumerate(numeros1):
# print(i, numero)
# for i, numero in enumerate(numeros1):
#     print(i, numero)

# for indice, (numero1, numero2) in enumerate(zip(numeros1, numeros2)):
#     resultado = suma_multiplicacion(numero1, numero2)
#     print(indice, numero1, numero2, resultado)

resultado = []
for indice, (numero1, numero2) in enumerate(zip(numeros1, numeros2)):
    if numero1 % numero2 == 0 or numero2 % numero1 == 0:
        resultado.append((indice, numero1, numero2))

# print("\n".join(str(x) for x in resultado))


def existe_suma(numeros1, numeros2, suma):
    resultado = []
    for indice, (numero1, numero2) in enumerate(zip(numeros1, numeros2)):
        if numero1 + numero2 == suma:
            resultado.append((indice, numero1, numero2))
    return resultado


res = existe_suma(numeros1, numeros2, 14)
# print("\n".join(str(x) for x in res))
print(res)
