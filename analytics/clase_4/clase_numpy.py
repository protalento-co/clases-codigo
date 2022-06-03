import numpy as np

# import pandas as pd
# import matplotlib.pyplot as plt

# import scipy

vector = np.array([1, 2, 5])
resultado = np.array([2, 4, 10])
multiplicador = 2
resultado_prueba = multiplicador * vector
print(f"{resultado_prueba=}")
print(f"{vector+resultado=}")
print(f"{vector*resultado=}")
print(f"{np.dot(vector,resultado)=}")
print(f"{np.cross(vector,resultado)=}")

# I > ay > eye (ay)
unitaria_2 = 2 * np.eye(3)
resultado_prueba = np.matmul(vector, unitaria_2)

print(f"{resultado_prueba=}")
