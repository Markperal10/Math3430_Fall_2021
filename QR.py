import LA

#Problem 1
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

# Problem 2

def orthonormal_vectors(matrix1: list[list[complex]])-> list[list[complex]]:
    """Returns an orthonormal list of vectors from our input matrix
    Q is set to equal the stable_Gram_schmidt function which is from our QR file. Using the
    stable_Gram_Schmidt we can already calculate the orthonormal list of vectors for our input matrix
    which is Q. We only want to return Q, so only the first column in Q noted as Q[0] which stores the list
    that e want to return.

    Args:
        matrix1: A amtrix stored as a list of lists with complex and real numbers

    Returns:
        Q which is set to equal the orthonormal list of vectors of the matrix inputted.

    """
    Q : list[list[complex]] = stable_Gram_Schmidt(matrix1)
    return Q[0]



