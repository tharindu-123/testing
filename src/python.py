row_col_a=input().split()
rows_a=int(row_col_a[0])
cols_a=int(row_col_a[1])
matrix_a=[]
for row_num in range (0,rows_a):
    row_a=input().split()
    matrix_a.append(row_a)
print(matrix_a)    
row_col_b=input().split()
rows_b=int(row_col_b[0])
cols_b=int(row_col_b[1])
matrix_b=[]
for row_num in range (0,rows_b):
    row_b=input().split()
    matrix_b.append(row_b)
print(matrix_b)
