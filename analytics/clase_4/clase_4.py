# mi_lista = [1, 2, 5, 6, 9]
# mi_lista2 = ["hola", "chao", True, [1,2,3]]

# print(mi_lista[1])


vector = [1, 2, 5, 6, 9, 10, 15, 0, 11, 22]
resultado = [2, 4, 10, 12, 18, 2, 0, 1, 10, 4]

# resultado_prueba = 2 * vector


def funcion_multiplicar(numero):
    return numero * 2


# resultado_prueba = []
# multiplicador = 2
# for elemento in vector:
#     # print(elemento)
#     resultado = funcion_multiplicar(elemento, multiplicador)
#     resultado_prueba.append(resultado)

# print(f"{resultado_prueba=}")

resultado_prueba = []
multiplicador = 2
# resultado_prueba = list(map(funcion_multiplicar, vector))

# función anónima (lambda function en python)
# resultado_prueba = list(map(lambda elemento: elemento * multiplicador, vector))

# list comprehension
# resultado_prueba = [elemento * multiplicador for elemento in vector]


# print(f"{resultado_prueba=}")
# print(f"{vector+resultado=}")

# slice notation
# print(f"{vector=}")
# print(f"{vector[1]=}")
# print(f"{vector[1:7]=}")
# print(f"{vector[1:7:2]=}")
# print(f"{vector[7:1:2]=}")
# print(f"{vector[7:1:-2]=}")
# print(f"{vector[1::2]=}")
# print(f"{vector[:7:3]=}")
# print(f"{vector[:len(vector):-1]=}")
# print(f"{vector[::-1]=}")

# palindromo = "ana"
palindromo = "anita lava la tina"
palindromo_sin_espacios = palindromo.replace(" ", "")
print(f"{palindromo=}")
print(f"{palindromo_sin_espacios=}")
# print(palindromo == palindromo[::-1])
print(palindromo_sin_espacios == palindromo_sin_espacios[::-1])
pal_lista = list(palindromo)
pal_lista.reverse()
print(pal_lista)
