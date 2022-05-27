print("Hola mundo")

# from datetime import date, datetime

# print(f"{type(10)=}")
# print(f"{type(5.5)=}")
# print(f"{type('hola')=}")
# print(f"{type(True)=}")
# print(f"{type([1,2,3,4,5])=}")
# print(f"{type((1,2,3,4,5))=}")
# my_set = {1, 2, 3, 3, 3, 3}
# print(f"{type(my_set)=}, {my_set=}")
# print(f"{type({'hola': 2, 'chao': 1})=}")

# cliente_1 = {
#     "identificacion": 1020123456,
#     "nombre": "diego",
#     "celular": 3001234567,
#     "fecha_facturacion": 15,
# }
# cliente_2 = {
#     "identificacion": 1020123457,
#     "nombre": "daniel",
#     "celular": 3111234567,
#     "fecha_facturacion": 10,
# }

# clientes = [cliente_1, cliente_2]

# print(f"{clientes=}")


# # "2022-05-19 19:05:10" datestring

# print(datetime.now().isoformat())


x = 10
y = 3

# print(type(x))  # int = Integer
# print(type(y))  # float = Floating point number
# print(x.__class__)  # int = Integer
# print(y.__class__)  # float = Floating point number

# z = x + y
# x = 3
# y = "hola"
# z = x + y
# print(z)
# z = x - y
# print(z)
# z = x * y
# print(z)
# z = x / y
# print(z)
# z = x**y
# print(z)
# z = x % y  # modulo, mod, residuo
# print(z)
# z = x // y  # floor division
# print(z)
# z = x // y + 1
# print(z)
# >, >>, <, <<, >=, <=, @, ^, %, ~, ==, !, !=

# 1 @ 2

# print(type(z))


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre=},{self.edad=}"

    def __add__(self, other):
        return self.edad - other.edad


persona_1 = Persona("Diego", 28)
persona_2 = Persona("Daniel", 25)

print(persona_1)
print(persona_2)

print(persona_1 + persona_2)
