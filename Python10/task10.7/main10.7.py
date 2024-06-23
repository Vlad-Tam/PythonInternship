"""
Создать матрицу случайных чисел и сохранить ее в json
файл. После прочесть ее, обнулить все четные элементы
и сохранить в другой файл
"""

import numpy as np
import json

if __name__ == "__main__":
    matrix = np.random.randint(0, 11, size=(3, 3))

    with open('./matrix.json', 'w') as file:
        json.dump({'matrix': matrix.tolist()}, file, indent=2)

    with open('./matrix.json', 'r') as file:
        loaded_data = json.load(file)
        loaded_matrix = np.array(loaded_data["matrix"])
        print(loaded_matrix)

    for i in range(loaded_matrix.shape[0]):
        for j in range(loaded_matrix.shape[1]):
            if loaded_matrix[i, j] % 2 == 0:
                loaded_matrix[i, j] = 0
    print(loaded_matrix)

    with open('./changed_matrix.json', 'w') as file:
        json.dump({'changed_matrix': loaded_matrix.tolist()}, file, indent=2)
