def add_vectors(vector_a: list[float],
                vector_b: list[float]) -> list[float]:
    """Adds the two input vectors.

    Creates a result vector stored as a list of 0's the same length as the input
    then overwrites each element of the result vector with the corresponding
    element of the sum of the input vectors. Achieves this using a for loop over
    the indices of result.

    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector, the same length as vector_a, stored as a list.

    Returns:
       The sum of the input vectors stored as a list.
    """
    result: list[float] = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result


# End Example
# Problem 1
def scalar_vec_multi(vector1: list[float], scalar1: float) -> list[float]:
    """ Multiplies the input vector to the value of the scalar.

    Creates a result vector as empty list. The length of the result vector will return
    the same amount of elements in the vector. Then zeros are appended to the result list.
    Then it sets the result equal to the product of vector times the value of the scalar.
    Achieved using a for loop for the number of indices that are in the input vector.

    Args:
        vector1: A vector stored as a list.
        scalar1: A single value scalar.

    Returns:
        The product of the input vector and scalar stored as a list

    """
    result: list[float] = []
    for c in range(len(vector1)):
        result[c] = result.append(0)
    for c in range(len(vector1)):
        result[c] = (vector1[c] * scalar1)
    return result


# Problem 2
def scalar_matrix_multi(matrix1: list[list[float]], scalar1: float) -> list[list[float]]:
    """Multiplies the input matrix to the value of the scalar.

    Overrides the initial indices of matrix1 with the product of matrix1 and the value
    of the scalar. Achieved by using a for loop using the exact amount of indices that
    are in each row and column in the inputted matrix1.The initial values for matrix1
    are then override by the product as each indice in the matrix is multiplied by the scalar using the
    scalar_vec_multi function.

    Args:
        matrix1: A matrix stored as a list of lists
        scalar1: A single value scalar stored as a float

    Returns:
        The product of the input matrix and scalar stored as list of lists.
    """
    for c in range(len(matrix1)):
        matrix1[c]= (scalar_vec_multi(matrix1[c],scalar1))
    return matrix1


# Problem 3
def matrix_add(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
    """Adds the two input matrices.

    Overrides the initial indices of matrix1 with the sum of matrix1 and matrix2.
    Achieved by using a for loop using the exact amount of indices that
    are in each column in the inputted matrix1. The initial values for matrix1
    are then override by the sum as matrix1 is being added to matrix2 using the add_vectors function.

    Args:
        matrix1: A matrix stored as a list of lists
        matrix2: A matrix stored as a list of lists

    Returns:
        The sum of the input matrices stores as a list of lists.
    """
    matrix_result: list[list[float]] = [([0]*(len(matrix1[0]))) for i in range(len(matrix1))]
    for c in range(len(matrix1)):
        matrix_result[c] = add_vectors(matrix1[c], matrix2[c])
    return matrix_result



# Problem 4
def matr_vec_multi(matrix1: list[list[float]], vector1: list[float]) -> list[float]:
    """Multiples the input matrix by the input vector.

    Creates a result matrix stored as a list of lists. Zero's are then appended to the list
    for the same amount of indices in the input matrix. Creates a result vector stored as a
    list of zeros with the same amount of elements in the input vector. Used in the previous function, scalar_vec_multi,
    we now use it to overwrite each column in matrix1 with the product of the matrix1 lists and vector1 elements. Next step
    is to override the matrix_result by using the add_vectors function. This functions adds matrix_result[c] to matrix_result[(c + 1)].
    Last override the vector_result with the last column in the matrix_result.Achieved using a for loop to compute add_vectors and
    scalar_vec_multi.


    Args:
        matrix1: A matrix stored as a list of lists
        vector1: A vector stored as a list
    Returns:
        The product of the the input vector and input matrix stored as a list
    """
    matrix_result: list[list[float]] = [([0] * (len(matrix1[0]))) for c in range(len(matrix1))]
    vector_result: list[float] = []
    for c in range(len(vector1)):
        vector_result[c] = vector_result.append(0)

        matrix_result[c] = scalar_vec_multi(matrix1[c], vector1[c])

    for c in range(len(matrix_result) - 1):
        matrix_result[c + 1] = add_vectors(matrix_result[c], matrix_result[(c + 1)])

    vector_result = matrix_result[len(matrix_result) - 1]

    return vector_result


# Problem 5
def matr_matr_multi(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
    """Multiplies the two input Matrices

    Creates a matrix_result stored as a list of lists which contains zero's for same row length in matrix1
    and same column length in matrix2. Then overwrites all the columns in matrix_result with the corresponding product
    of matrix1 and the columns in matrix2. Computed using a for loop to keep the same column length of matrix2.
    With the function matr_vec_multi within the for loop it then overrides the indices in matrix_result.

    Args:
        matrix1: A matrix stored as a list of lists
        matrix2: A matrix stored as a list of lists

    Returns:
        The product of the two input matrices stored as a list of lists

    """
    matrix_result: list[list[float]] = [([0] * (len(matrix1[0]))) for c in range(len(matrix2))]
    for c in range(len(matrix2)):
        matrix_result[c] = matr_vec_multi(matrix1, matrix2[c])

    return matrix_result

# Homework 04

# Problem 1
def abs_value(scalar: complex)->complex:
    """ Computes the absolute value of a scalar

    Creates a scalar set to take both real and complex numbers.
    Creates a result equal to complex numbers which takes the real and imaginary
    numbers and squares them. Then takes the sum of the two and takes the square
    root to give the absolute value.

    Args:
         scalar: A scalar stored as real and complex numbers

    Returns:
        The absolute value stored as a complex or real number

    """
    scalar = complex(scalar)
    result: complex = scalar.real**2 + scalar.imag**2
    result = result**(.5)
    return result

# Problem 2
def p_norm(vector_A:list[float], p:float = 2)->float:
    """Computes the p-norm for a vector and an initialized p value

    Creates a result variable as a float assigned to zero. For the elements in vector_A add 0, the initial result value,
    to the first element in the vector.That sum is squared by the integer value of p which is 2. Run same process by adding
    the next element in the input vector to the previous value that was squared. Creates a variable, power,
    to take the absolute value of 1/p which equals 1/2. The result is then computed by using the sum of the elements after
    they are squared in vector_A and multiplied by the power result.

    Args:
        vector_A: A vector stored as a list
        p: float value stored as 2
    Returns:
        A result stored as a float of the product between result and power

    """
    result: float = 0
    for element in vector_A:
        result = result + element**(abs_value(p))
    power: float = abs_value(1/p)
    result = result**(power)
    return result

#Problem 3
def inf_norm(vector_A: list[float])->float:
    """Computes the infinity norm of the input vector 
    
   Creates a result variable as a float assigned to zero. For the elements in vector_A add 0, the initial result value,
    to the first element in the vector.That sum is squared by the absolute value of p which is 2. Overrides result by adding
    the next element in the input vector using the same process to the previous value that was squared.Runs for the amount of
    elements in the input vector. Creates a variable,power,to take the absolute value of 1/p which equals 1/2.
    The result is then set to equal the sum of the elements after they are squared in vector_A and multiplied by the power result.
    
    Args: 
        vector_A: A vector stored as a list
    
    Returns: 
        The element with the largest absolute value of the vector stored as a float
    """
    result: float = 0
    compare: float= 0
    for element in vector_A:
        compare = abs_value(element)
        if (compare > result):
            result = compare
    return result

#Problem 4
def P_inf_norm_result(vector_A: list[float], p:float =2, boolean:bool =False)->float:
    """Returns the p-norm or the infinity norm of the vector and p value.

    A boolean value set to False. The function returns the p-norm of the input vector.This would mean once the elements
    in vector_A are squared then added the square root is then taken.If the boolean value is changed to True
    the function will call the previous function inf_norm to calculate the infinity norm of vector_A.
    This would be the highest absolute value in vector_A.

    Args:
        vector_A: A vector stored as a list
        p: A float value set to 2
        boolean: A boolean value set to false
    Returns:
        The p-norm or infinity norm of vector_A stored as a float

    """
    if (boolean == False):
        result = p_norm(vector_A, p)
    else:
        result = inf_norm(vector_A)
    return result

#Problem 5
def Inner_product(vector_A: list[float], vector_B: list[float])->float:
    """Computes the inner product of two input vectors

    Creates a result variable set to zero as a float. For the same length of vector_A
    a corresponding vector_B is multiplied. Each element in vector_A is multiplied to each
    corresponding element in vector_B. Then the sum of the product of the elements in both vectors are added
    to result 0.

    Args:
        vector_A: A vector stored as a list
        vector_B: A vector stored as a list
    Returns:
         The inner product of two input vectors stored as a float

    """
    result:float = 0
    for element in range(len(vector_A)):
        result = result + (complex(vector_A[element]) * complex(vector_B[element]))
    return result







