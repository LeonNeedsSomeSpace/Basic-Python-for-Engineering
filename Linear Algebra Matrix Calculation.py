#Create a program that can allows matrix inputs as well as perform matrix multiplication as well as matrix addition
#Define a function that allows the user to enter the desired size of the matrices
def get_matrix(name):
    size = input(f"Enter the size of matrix {name} (such as 2x2 or 3x3): ")
    try:
        rows, cols = map(int, size.lower().split('x')) #This will split the input string at x and converts them into rows = m and cols = n
    except ValueError:
        print("Invalid format. Please use format mxn (such as 2x2 or 3x3).")
        return get_matrix(name)

#It's row-by-row input, therefore there is an input string for each row of the matrix
    print(f"Enter the values for {name} matrix row by row (each row should have {cols} numbers): ")
    matrix = [] #This initializes an empty string so the digits of the matrix can be stored inside
    for i in range(rows):
        while True:
            row_enter = input(f"Row {i + 1}: ") #This asks the user to input the values for the number of rows
            row_values = row_enter.strip().split()
            if len(row_values) != cols:
                print(f"Please enter exactly {cols} values. ") #Error message, should the input length and the defined column lenght not be equal
                continue
            try: #Convert all values to float numbers and add them to the output
                row = [float(value) for value in row_values]
                matrix.append(row)
                break
            except ValueError: #Error message if there is an input that is not a number
                print("Please enter valid numbers.")
    return matrix, rows, cols

def print_matrix(matrix, name): #Before further operation, the matrix gets printed out
    print(f"\n{name}:")
    for row in matrix:
        print(" ".join(f"{val:.2f}" for val in row))

#This function will perform addition if option 1) is chosen (later)
def matrix_addition(mat1, mat2):
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))  #It loops through each row adn column elements
#This function will multiply matrices if option 2) is chosen (later)
def matrix_multiplication(mat1, mat2):
    result = []
    for i in range(len(mat1)): #For each cell (i, j) in the result, it calculates the dot product of row i in matrix 1 and column j in matrix 2
        row = []
        for j in range(len(mat2[0])):
            total = sum(mat1[i][k]*mat2[k][j] for k in range(len(mat1))) #Formula for the dot product
            row.append(total)
        result.append(row)
    return result

#Call the functions that will return values from the matrices
#rows1, rows2 for the number of rows in the respective matrices
#cols1, cols2 for the number of columns in the respective matrices
matrix1, rows1, cols1 = get_matrix("#1")
matrix2, rows2, cols2 = get_matrix("#2")


#Visualize
print_matrix(matrix1, "First Matrix")
print_matrix(matrix1, "Second Matrix")

#Chose one of the two operation (whether addition or multiplication)
print("\n Choose operation (Only addition and multiplication possible): ")
print("1) Add matrices\n")
print("2) Multiply matrices\n")
choice = input("Enter 1 or 2: ")

if choice == '1':
    if rows1 == rows2 and cols1 == cols2: #Option 1) only gets carried out if rows and columns of both matrices are equal
        result = matrix_addition(matrix1, matrix2)
        print_matrix(result, "Sum of Matrices")
    else:
        print("Error. Matrices need to be the same size to perform addition")
elif choice == '2':
    if columns1 == rows2: #Only if colums in matrix 1 and rows in matrix 2 are equal, option 2) can be executed
        result = matrix_multiplication(matrix1, matrix2)
        print_matrix(result, "Product of Matrices")
    else:
        print("Error: Number of colums of matrix 1 must equal rows of matrix 2 for multiplication")

else: #For all inputs that are not 1 or 2, an error message will pop up
    print("Invalid choice")
