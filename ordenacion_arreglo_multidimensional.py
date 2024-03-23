def ordenar_fila_ascendente(matriz, fila):
    """
    Ordenar una fila específica de una matriz en orden ascendente.
    """
    fila_ordenada = sorted(matriz[fila])
    matriz[fila] = fila_ordenada
    return matriz

def imprimir_matriz(matriz):
    """
    Función para imprimir la matriz.
    """
    for fila in matriz:
        print(fila)

# Definir una matriz de ejemplo (3x3)
matriz = [
    [3, 1, 4],
    [9, 5, 2],
    [7, 8, 6]
]

# Mostrar matriz original
print("Matriz original:")
imprimir_matriz(matriz)
print()

# Fila que se desea ordenar (0, 1 o 2)
fila_a_ordenar = 1

# Llamar a la función para ordenar la fila específica
matriz_ordenada = ordenar_fila_ascendente(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print(f"Matriz con la fila {fila_a_ordenar} ordenada orden ascendente:")
imprimir_matriz(matriz_ordenada)
