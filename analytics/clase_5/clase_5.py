import pandas as pd

ejemplo = pd.read_csv(
    "analytics/clase_5/pokemon.csv",
    index_col="pokedex_number"
    # , names=["col1", "col2", "col3", "col4"]
)

print(ejemplo.head())
# print(ejemplo.info())
# print(ejemplo.describe())

# ejemplo.to_csv("analytics/clase_5/ejemplo_2.csv", index=False, sep=";")
# ejemplo.to_csv("analytics/clase_5/ejemplo_3.csv", index=False, sep="\t")

# ejemplo["nueva columna"] = ejemplo["edad"] + ejemplo["numero favorito"]


# def paridad(row):
#     numero = row["nueva columna"]
#     if numero % 2 == 1:
#         return numero * 2
#     else:
#         return numero / 2


# ejemplo["paridad"] = ejemplo.apply(
#     (
#         lambda row: row["nueva columna"] * 2
#         if row["nueva columna"] % 2 == 1
#         else row["nueva columna"] / 2
#     ),
#     axis=1,
# )

# ejemplo["paridad_2"] = ejemplo.apply(
#     paridad,
#     axis=1,
# )

# print(ejemplo)


# print(ejemplo["numero favorito"].mean())
# print(ejemplo["numero favorito"].min())
# print(ejemplo["numero favorito"].max())
# print(ejemplo["numero favorito"].sum())
# print(type(ejemplo["numero favorito"]))
# print(type(ejemplo["numero favorito"].mean()))

print(type(ejemplo.iloc[1]["abilities"]))
print(len(pd.eval(ejemplo["abilities"])))
# ejemplo["abilities"] = pd.eval(ejemplo["abilities"])
# print(ejemplo)
