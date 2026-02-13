import numpy as np

array = np.random.rand(6,6)

print("6*6 Random Array:")
print(array)

rank=np.linalg.matrix_rank(array)

print("\nRank of the matrix: ",rank)