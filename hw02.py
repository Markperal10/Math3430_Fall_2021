# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 20:45:17 2021

@author: markj
"""
#Mark Peralta
#Homework 02
#Problem 00

#Problem 00
#Q1: What do we have?

#A1: Two vectors stored as lists. Denoted by the names vector_a and vector_b. 

#Q2: What do we want?

#A2: Their sum stored as a list.

#Q3: How will we get there?

#A3: We will create an empty list of the appropriate size and store the sums of
#the corresponding components of vector_a and vector_b. 

#-PsuedoCode

#def add_vectors(vector_a,vector_b):

#Initialize a result vector of 0's which is the same size as vector_a. Call this
#vector result.

# Set each element of result to be equal to the desired sum.
#for index in range(length(result)):
# result[index] = vector_a[index] + vector_b[index]

#Return the desired result.

def add_vectors(vector1,vector2):
  result = [0 for element in vector1]
  for index in range(len(result)):
    result[index] = vector1[index] + vector2[index]
  return result

#Test Inputs

test_vector_01 = [3, 2, 6]
test_vector_02 = [4, 6, 8]
test_vector_03 = [5, 1, 7]


# add_vectors(test_vector_01,test_vector_02) should output [4,3,6]
print('Test Output 1 for add_vectors: ' + str(add_vectors(test_vector_01,test_vector_02)))
print('Should have been [7,8,14]')
# add_vectors(test_vector_01,test_vector_03) should output [8,3,13]
print('Test Output 2 for add_vectors: ' + str(add_vectors(test_vector_01,test_vector_03)))
print('Should have been [8,3,13]')

#Problem #1

#Write an algorithm to implement scalar-vector multiplication.
#Q1: What do we have?

#A1: We have a vector and a scalar stored in a computer. vector1 and scalar1

#Q2: What do we want?

#A2: We want to multiply the vector we have stored in the computer by the scalar to change the values of the given vector 

#Q3: How will we get there?

#A3: We will get there by using the input of the vector1 and multiply it by scalar1. Multiplying vector1 to  the value of scalar1 . Each element [] in vector1 is being multiplied by scalar1 and vector1 is then changing to the product of vector1 * scalar1.

#def scalar_vec_multi(vector1,scalar1)
#Initialize the result
#result = []
#The length of the vector will return the same amount of index's in vector1 
#for c in range(length(vector1)): 
#The result is set to equal the index's appended to the list
#result[c] = result.append(0)
#Set result equal to the product of vector1 times the value of the scalar
#result[c] = vector1[c]*scalar1[s]

#Returns the new elements of the vector1 after being multiplied by the scalar
#return result

def scalar_vec_multi(vector1,scalar1):
    result = []
    for c in range(len(vector1)):
        result[c] = result.append(0)
    
        result[c] = (vector1[c]*scalar1)
    return result
    
#test input 1
vector1 = [3, 2, 6]
scalar1 = 2
print('Test Output 1 for scalar_vec_multi:',(scalar_vec_multi(vector1,scalar1)))
print('Should have been [6,4,12]')
#test input 2
vector2 = [2, 4, 5]
scalar2 = 4
print('Test Output 2 for scalar_vec_multi:',(scalar_vec_multi(vector2,scalar2)))
print('Should have been [8,16,20]')
#Problem #2

#Write an algorithm to implement scalar-matrix multiplication.

#Q1: What do we have?

#A1: We have a scalar and a matrix stored in a computer, matrix1 and scalar1

#Q2: What do we want?

#A2: We want to multiply the matrix that was inputed and stored into the computer to  be multiplied by the value of the scalar. 

#Q3: How will we get there?

#A3: We will get there by multiplying each element in matrix1 by the value inputed for scalar1. The matrix1 will be stored as a set of columns and rows c and r and will then be multiplied by the scalar1 value. 

#def scalar_matrix_multi(matrix1, scalar1).

#The columns c is going to be the length of the input for matrix1
#for c in range(length(matrix1)):

#The number of rows r will be the length of the number of rows inputed for matrix1
#	for r in range(length(matrix1)):
#In order to multiply the rows (r) and columns (c) store them with the matrix and then multiply the entire matrix1 it by scalar1 value. 
#It will run through each list in the matrix1 and multiply it by scalar1
#		matrix1[c][r] = matrix1[c][r] * scalar1
#Return the value for matrix1 which will be changed with the scalar1 multiplied to it
#return matrix1

        
def scalar_matrix_multi(matrix1,scalar1):
    for c in range(len(matrix1)):
        for r in range(len(matrix1[0])):
            matrix1[c][r] = (matrix1[c][r]*scalar1)
    return matrix1
#test input 1
matrix1 = [[3,2,6],[4,3,4],[1,2,3]]
scalar1 = 2
print('Test Output 1 for scalar_matrix_multi:',(scalar_matrix_multi(matrix1,scalar1)))
print('Should have been [6,4,12],[8,6,8],[2,4,6]')
#test input 2
matrix2 = [[6,2,1],[8,4,2],[4,5,6]]
scalar2 = 3
print('Test Output 2 for scalar_matrix_multi:',(scalar_matrix_multi(matrix2,scalar2)))
print('Should have been [18,6,3],[24,12,6],[12,15,18]')

#Problem #3

#Write an algorithm to implement matrix addition.

#Q1: What do we have?

#A1: We have two matrices that have the same dimensions stored in the computer, matrix1 and matrix2.

#Q2: What do we want?

#A2: We want to add the matrices of the same dimensions and get the sum of the matrices into one matrix and store it in the computer.

#Q3: How will we get there?

#A3: We will get there by using the input of matrix1 and store it and then add the input of matrix2. This means the rows and columns must be of the same dimension (length) as matrix1 list in order to be added.

#def matrix_add(matrix1,matrix2)

#Using the for loop to find the number of columns to read each column individually 
#for c in range(length(matrix1)):

#Using the for loop to find the number of rows to then return the same number of elements in the list that were assigned to matrix1
#	for r in range(length(matrix1[])):

#Sets matrix1 equal to matrix1 plus matrix2 with the same dimensions and number of elements in the list as matrix1
#Finding the placement of each number in our matrix and by using the for loops we are able to detremine the index's. 		
#matrix1[c][r]= matrix1[c][r]+matrix2[c][r]


#Returns the sum of the matrices as matrix1
#return matrix1

def matrix_add(matrix1,matrix2):
    for c in range(len(matrix1)):
        for r in range(len(matrix1[0])):
            matrix1[c][r] = matrix1[c][r]+matrix2[c][r]
    return matrix1
#test input 1 
matrix1 = [[4,7],[2,8]]
matrix2 = [[3,5],[1,6]]
print('Test Output 1 for matrix_add:',matrix_add(matrix1,matrix2))
print('Should have been [7,12],[3,14]')

#test input 2
matrix3 = [[8,9],[5,2]]
matrix4 = [[3,4],[5,6]]
print('Test Output 2 for matrix_add:',matrix_add(matrix3,matrix4))
print('Should have been [11,13],[10,8]')

#Problem #4

#Write an algorithm to implement matrix-vector multiplication using the linear
#combination of columns method. You must use the algorithms from Problem #0 and
#Problem #1.  

#Q1: What do we have?

#A1: We have a vector and a matrix stored in the computer, vector1 and matrix1 for a 2x2 matrix.

#Q2: What do we want? 

#A2: We want to mutlipy the matrix1 and vector1 using the linear combination of columns method.

#Q3: How will we get there?

#A3: We will get there by using the functions of vector addition() and scalar vector multiplication().  
#First using the function def scalar_vec_multi(vector1,scalar1) by multiplying the first list (column) stored in the matrix1 to the first index in vector1. Once appended to matrix_result,multiply the second 
#list in matrix1 by the second index in the vector1. After storing the answers to result_matrix add the answers of (list 1  in matrix1* first index vector1) + (list 2  in matrix1* second index vector1). This is done using the function def add_vectors(vector1,vector2).
#Return a new vector2 with the products and summations.

#def matr_vec_multi

# Initialize the matrix_result to be same length of matrix1
#matrix_result = [([0]*(length(matrix1[0]))) 

# Initialize the vector_result as an empty list
#vector_result = []

# Store the same amount of index within the range of vector1 with the solutions
#for c in range(length(vector1)):
#	vector_result[c] = vector_result.append[0]

# Sets the matrix_result equal to the function multiplying the first list(column) in matrix1 to the first element in vector1.Then going on with the second list and storing each continous product as matrix_result as it starts counting at 0 then goes on.
#for c in range (length(vector1)):
#	matrix_result[c] = scalar_vec_multi(vector1[c],matrix1[c])

# The vector result is set to equal the sum of both lists (columns) stored in to give the final vector by adding the two lists of the 2x2 matrix.
#vector_result = add_vectors(matrix_result[0],result_matrix[1])

# Return the new vector 
#return vector_result

def matr_vec_multi(matrix1,vector1):
    matrix_result = [([0]*(len(matrix1[0]))) for c in range(len(matrix1))]
    vector_result = []
    for c in range(len(vector1)):
        vector_result[c] = vector_result.append(0)
    
        matrix_result[c] = scalar_vec_multi(matrix1[c],vector1[c])
        
    for c in range(len(matrix_result)-1):
        matrix_result[c+1] = add_vectors(matrix_result[c],matrix_result[(c+1)])
        
    vector_result = matrix_result[len(matrix_result)-1]
    
    return vector_result
#test input 1
matrix1 = [[3,4],[5,6]]
vector1 = [2,4] 

print('Test Output 1 for matr_vec_multi:',matr_vec_multi(matrix1,vector1))
print('Should have been [26,32]') 

#test input 2
matrix2 = [[2,8],[3,9]]
vector2 = [4,5] 
print('Test Output 2 for matr_vec_multi:',matr_vec_multi(matrix2,vector2))
print('Should have been [23,77]') 

#Problem #5

#Write an algorithm to implement matrix-matrix multiplication using your
#algorithm from Problem #4. 

#Q1 : What do we have?

#A1 : We have two matrices stored within the computer

#Q2 : What do we want?

#A2 : We want to multiply the matrices stored in the computer and create a new matrix giving the result. 

#Q3 : How will we get there?

#A3: We will get there by first using the algorithm from Problem #4 which includes the add_vectors, scalar_vec_multi, and matr_vec_multi functions. This algorithm sets up the matrices so that we multiply both columns in matrix1 
#by the first column in matrix2. This product is then stored into a new matrix_result with two numbers from the product.
#These are then added and stored into the first column(vector) of the matrix_result. This process will run through again multiplying both columns in matrix1 and multiply them by the second column in matrix2. This will store the product of matrix1 times the second column in matrix2. 
#We will then add the products and store them as the second column(vector) into our matrix_result. This multiplcation process will be done with a for loop using the length of the columns matrix2.


# Initialize the matrix_result to be same length of matrix1
#matrix_result = [([0]*(length(matrix1[0]))) 

# Initialize the vector_result as an empty list
#vector_result = []

# Store the same amount of index within the range of vector1 with the solutions
#for c in range(length(vector1)):
#	vector_result[c] = vector_result.append[0]

# Sets the matrix_result equal to the function multiplying the first list(column) in matrix1 to the first element in vector1.Then going on with the second list and storing each continous product as matrix_result as it starts counting at 0 then goes on.
#for c in range (length(vector1)):
#	matrix_result[c] = scalar_vec_multi(vector1[c],matrix1[c])

# The vector result is set to equal the sum of both lists (columns) stored in to give the final vector by adding the two lists of the 2x2 matrix.
#vector_result = add_vectors(matrix_result[0],result_matrix[1])

# Return the new vector 
#return vector_result


#def matr_matr_multi(matrix1,matrix2):

#The result matrix is then going to have the same amount of columns of matrix1 as we cannot alter matrix1. 
#The for loop is to identify the number of columns in the matrix1 so that the matrix_result is the same.
#matrix_result = [([0] * (length(matrix1))) for i in range(length(matrix1))]

#The number of columns in matrix2 is then used in a for loop to multiply each vector(column) in matrix2. 
#The matrix_result is set to equal to the function of matr_vec_multi(matrix1,matrix2[i]) using each column of matrix2. This will run through if the number of columns is the same and go through each one individually.
#for c in range(length(matrix2)):
#	matrix_result[c] = matr_vec_multi(matrix1,matrix2[i])
#Returns the result of the matrices being multiplied
#return matrix_ersult
def matr_vec_multi(matrix1,vector1):
    matrix_result = [([0]*(len(matrix1[0]))) for c in range(len(matrix1))]
    vector_result = []
    for c in range(len(vector1)):
        vector_result[c] = vector_result.append(0)
    
        matrix_result[c] = scalar_vec_multi(matrix1[c],vector1[c])
        
    for c in range(len(matrix_result)-1):
        matrix_result[c+1] = add_vectors(matrix_result[c],matrix_result[(c+1)])
        
    vector_result = matrix_result[len(matrix_result)-1]
    
    return vector_result

def matr_matr_multi(matrix1,matrix2):
    
    matrix_result = [([0] * (len(matrix1[0]))) for c in range(len(matrix2))]
    for c in range(len(matrix2)):
        matrix_result[c] = matr_vec_multi(matrix1,matrix2[c])
         
    return matrix_result


#test input 1
matrix1 = [[3,4],[5,6]]
matrix2= [[2,4],[5,7]] 

print('Test Output 1 for matr_matr_multi:',matr_matr_multi(matrix1,matrix2))
print('Should have been [[26,32],[50,62]]')

#test input 2
matrix3 = [[8,2],[3,1]]
matrix4 = [[1,6],[9,7]] 

print('Test Output 2 for matr_matr_multi:',matr_matr_multi(matrix3,matrix4))
print('Should have been [[26,8],[93,25]]')





