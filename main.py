import numpy as np

def matrix_input():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    print("Enter the elements row-wise:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    
    return np.array(matrix)

def vector_input():
    elements = list(map(float, input("Enter the vector elements separated by space: ").split()))
    return np.array(elements)

def matrix_operations():
    print("\nMatrix Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Determinant")
    print("5. Inverse")
    print("6. Eigenvalues")
    choice = int(input("Enter your choice (1-6): "))
    
    if choice in [1, 2, 3]:
        print("Give details for matrix1: ")
        matrix1 = matrix_input()
        print("Give details for matrix2: ")
        matrix2 = matrix_input()
        
        if choice == 1:
            result = matrix1 + matrix2
            print("Result:")
            print(result)
        elif choice == 2:
            result = matrix1 - matrix2
            print("Result:")
            print(result)
        elif choice == 3:
            result = np.matmul(matrix1, matrix2)
            print("Result:")
            print(result)
    elif choice in [4, 5, 6]:
        print("Give details for matrix: ")
        matrix1 = matrix_input()
        
        if choice == 4:
            result = np.linalg.det(matrix1)
            print("Determinant:")
            print(result)
        elif choice == 5:
            try:
                result = np.linalg.inv(matrix1)
                print("Inverse:")
                print(result)
            except np.linalg.LinAlgError:
                print("The matrix is singular. Inverse does not exist.")
        elif choice == 6:
            result = np.linalg.eigvals(matrix1)
            print("Eigenvalues:")
            print(result)
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    matrix_operations()