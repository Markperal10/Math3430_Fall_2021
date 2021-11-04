import LA


# Problem 1
def unstable_Gram_Schmidt(matrix1: list[list[complex]])->list[list[complex]]:
    """ Finds the Q and R for QR factorization using the unstable Gram Schmidt method
    Creates four seperate variables, Q being a blank list, V being a matrix stored as the same size as matrix,
    R being stored as a matrix using the same amount of columns from matrix1, and a scalar which is a blank list.
    The first for loop will then run for the number of columns in matrix1.
    Within the for loop V[outer_for] is replaced with matrix1[outer_for]. Within that for loop another for loop is created
    and will run within the range of zero to what the outer for loop is at.
    This for loop then stores the product of Q and V using out function from our LA.py file.
    From there it will compute the the scalar vector multiplication of Q and -R form out scalar_vec_multi function from LA.py
    From there V is then set to equal the sum of the vector V and the scalar using the add_vectors function from LA.py.
    R is then set to equal the p norm of V using the p_norm function from LA.py.Then the scalar_vec_multi  of V and 1/R
    is then appended to Q.

     Args:
         matrix1: A matrix stored as a list of lists with complex and real numbers

     Returns:
         The Q and R for QR factorization

    """
    Q: list[float] = []
    V: list[list[float]] = [([0] * (len(matrix1[0]))) for i in range(len(matrix1))]
    R: list[list[float]] = [([0] * (len(matrix1))) for i in range(len(matrix1))]
    scalar: list[float] = []

    for outer_for in range(len(matrix1)):
        V[outer_for] = matrix1[outer_for]
        for inner_for in range(0,outer_for):
            R[outer_for][inner_for] = LA.Inner_product(Q[inner_for],V[outer_for])
            scalar = LA.scalar_vec_multi(Q[inner_for], -R[outer_for][inner_for])
            V[outer_for] = LA.add_vectors(V[outer_for],scalar)
        R[outer_for][outer_for] = LA.p_norm((V[outer_for]))
        Q.append(LA.scalar_vec_multi((V[outer_for]),(1/R[outer_for][outer_for])))
    return [Q,R]

#Problem 2
def stable_Gram_Schmidt(matrix1:list[list[float]])->list[list[float]]:
    """ Finds the Q and R for QR factorization using the stable Gram Schmidt method
    Creates four seperate variables, Q being a blank list, V being a matrix stored as the same size as matrix,
    R being stored as a matrix using the same amount of columns from matrix1,and vh being a float stored as an empty list.
    R is then set to equal the p norm of V using the p_norm function from LA.py for the number of columns in matrix1.Then
    the scalar_vec_multi of V and 1/R is then appended to Q. Using another for loop the inner for loop will
    store the inner product of  Q and V using the function Inner_product from LA.py into R. Then it will store the scalar
    vector multiplication of Q and -R using the scalar_vec_multi from LA.py. V is then override by the sum of V
    and vh using the add_vectors function from LA.py. Once the outer for loop comes to an end it returns Q and R.


     Args:
         matrix1: A matrix stored as a list of lists with complex and real numbers

     Returns:
         The Q and R for QR factorization

    """
    Q: list[complex or float] = []
    V: list[complex or float] = []
    R: list[list[float]] = [([0] * (len(matrix1))) for i in range(len(matrix1))] #square of input matrix
    vh : list[float] = []

    for element in matrix1:
        V.append(element)
    for outer_for in range(len(matrix1)):
        R[outer_for][outer_for] = LA.p_norm((V[outer_for]))
        Q.append(LA.scalar_vec_multi((V[outer_for]), (1/R[outer_for][outer_for])))
        for inner_for in range(outer_for+1,len(matrix1)):
            R[outer_for][inner_for] = LA.Inner_product(Q[outer_for],V[inner_for])
            vh = LA.scalar_vec_multi(Q[outer_for], -R[outer_for][inner_for])
            V[inner_for] = LA.add_vectors(V[inner_for],vh)
    return [Q,R]


