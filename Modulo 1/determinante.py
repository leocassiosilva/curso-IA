import numpy as np 

# Create a 4x4 matrix
matriz = np.array([
                    [1, 2, 3, 4],
                    [9, 6, 7, 8],
                    [9, 7, 5, 8],
                    [5, 5, 2, 8]
                ])

print("Matriz Original")
print(matriz)

# Determinante 
determinante =  np.linalg.det(matriz)
print("Determinante: " + determinante)
