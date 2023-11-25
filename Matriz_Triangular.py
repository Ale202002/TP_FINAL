import numpy as np

matriz_patron = np.empty((6, 6), dtype=str)

for i in range(6):
    for j in range(i + 1):
        if (j + 1) % 2 == 0:
            matriz_patron[i][j] = 'B'
        else:
            matriz_patron[i][j] = 'A'

print("Matriz Inferior Triangular")
print(matriz_patron)