######################################
#
# My Main program 
# Assignment #3
# Use this to testing your module
######################################

#Here I am importing your module
from MyLib import *


# Define Arrays A and B
A = [[25, 54, 17],[23, 45, 2],[15, 34, 51]]
B = [[3, 96, 31],[46, 57, 24],[32, 92, 27]]


### Perform Matrix addition ###
C = add_Mat(A,B)
print('Matrix A + Matrix B = ',C,'\n')

### Perform Matrix subtraction ###
C = sub_Mat(A, B)
print('Matrix A - Matrix B = ',C,'\n')

### Peform Matrix Dot Mutliplication ###
C = dmult_Mat(A,B)
print('Matrix A .* Matrix B = ',C,'\n')

### Perform Matrix cross product ###
C = cmult_Mat(A,B)
print('Matrix A x Matrix B = ',C,'\n')

### Chech Equality ###
if(isEqual(A,B)):
    print("Matrices are Equal")
else:
    print("Matrices are Not Equal")

### Scalar multiplication ###
var = 3.5
C = scale_Mat(A,var)
print(var,'* A = ',C,'\n')

### Matrix Determinant ###
detA = calc_det(A)
print("|A| = ",detA)


### Calculate the Inverse of a Matrix ###

C = inv_Mat(A)
print("The inverse of A is ",C)

### Calculate the Trace of a Matrix ###
C = trace_Mat(A)
print("Trace(A) = ", C)


### Calculate the transpose of a Matrix ###
C = trans_Mat(A)
print("Transpose(A) = ",C)










        
