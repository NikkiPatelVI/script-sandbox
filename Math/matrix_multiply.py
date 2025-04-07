# Function to multiply two matrices
def matrix_multiply(A, B):
    # Get the number of rows and columns for both matrices
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Check if multiplication is possible (columns of A must match rows of B)
    if cols_A != rows_B:
        raise ValueError("Matrix multiplication is not possible. Number of columns of A must equal number of rows of B.")

    # Create a result matrix initialized with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or k in range(rows_B)
                result[i][j] += A[i][k] * B[k][j]

    return result

# Example matrices for multiplication
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

# Perform the multiplication
result = matrix_multiply(A, B)

# Display the result
print("Result of matrix multiplication:")
for row in result:
    print(row)
