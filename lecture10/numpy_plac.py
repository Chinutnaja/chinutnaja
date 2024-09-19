import numpy as np 

random_matrix = np.random.randint(1,11,size=(3,3))
print("Rando 3x3 Matrix:\n", random_matrix)

matrix_sum = np.sum(random_matrix)
print(f"\nSum od all elements: {matrix_sum}")

matrix_mean = np.mean(random_matrix)
print(f"\nMean of the Matrix: {matrix_sum}")

transposed_matrix = np.transpose(random_matrix)
print("\nTransposed Matrix:\n", transposed_matrix)