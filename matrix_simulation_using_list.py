rows = int(input("enter the number of rows of the matrix:"))
coloumns = int(input("enter the number of coloumns of the matrix:"))
matrix =[]
print(f"enter the entries row by row (seperated by spaces)")
for i in range(rows):
    row = list(map(int,input(f"row {i+1}:").split()))
    if len(row) != coloumns:
        print(f"Error: You must enter exactly {cols} numbers.")
        break

    matrix.append(row)
    print("\n your matrix")
    print(matrix)
print("row sums")
for i, row in enumerate(matrix):
    row_sum= sum(row)
    print(f"Sum of Row {i+1}: {row_sum}")
print("coloumn sums")
for j in range(coloumns):
    cols_sum = 0
    for i in range(rows):
        cols_sum += matrix[i][j]
    print(f"Sum of Column {j+1}: {cols_sum}")
print("daigonal sums:")
primary_sums=0
for i in range(rows):
    primary_sums += matrix[i][i]
print(f"Sum of Primary Diagonal: {primary_sums}")