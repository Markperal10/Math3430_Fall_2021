import LA


def con_transpose(matrix1:list[list[complex]])->list[list[complex]]:
    """ Calculates the conjugate transpose
    Creates a variable a set to take complex numbers set to zero. Create a result set to equal the length of the rows in
    the input matrix. Then using two for loops using the same length of the columns and rows in the input matrix
    set a equal to the number of rows and columns the matrix contains. Then a is set to equal the sum of a real number
    and the imag-1j. The result with the same number of columns and rows in the matrix is set to equal a.

    Args:
        matrix1: A matrix stored as a list of lists of complex or real numbers
    Returns:
        The conjugate transpose of the input matrix stored as a list of complex numbers

    """
    a: complex = 0
    result: list[list[float]] = [([0] * (len(matrix1))) for i in range(len(matrix1[0]))]
    for column in range(len(matrix1)):
        for row in range(len(matrix1[0])):
            a = matrix1[column][row]
            a = a.real + (a.imag*-1j)
            result[row][column] = a
    return result


def matrix_ident(matrix1:list[list[complex]])->list[list[int]]:
    """ Computest he matrix identity
    Creates a result set to equal the length of the rows in the input matrix. All elements in the input matrix are zero.
    For the elements in the length of the input matrix set the result equal to 1 using the same number of elements
     within the matrix creating the diagonal line of 1's.

    Args:
        matrix1: A matrix stored as a list of lists of complex numbers

    Returns:
        The identity matrix of matrix1 stored as a list of integers

    """
    result : list[list[float]] = [([0]* (len(matrix1[0]))) for i in range(len(matrix1[0]))]
    for element in range(len(matrix1)):
        result[element][element] = 1
    return result

def diagonal_column(matrix1:list[list[complex]], num_col:int)-> list[complex]:
    """ Computes the diagonal column of matrix1
    Creates a result set to equal an empty list. It will then run a for loop that will use the length
    of matrix1 minus 1. Within the for loop replace the elements with 0 and then set the result equal to
    the elements in matrix1 ar [num_col][element+num_col].

    Args:
        matrix1: A matrix stored as a list of lists
        num_col: An integer
    Returns:
        The diagonal column of matrix1 stored as a list of complex numbers

    """
    result: list[float] = []
    for element in range((len(matrix1[num_col]))-num_col):
        result[element] = result.append(0)
        result[element] = matrix1[num_col][element+num_col]
    return result

def calc_V(e_vector:list[int], sub_x:list[complex])-> list[complex]:
    """ Calculates V for Householder factorization
    Creates a x_norm set to equal the p_norm which is used in our LA.py file using sub_x.
    Then creates x_e_vector which is set to equal the scalar vector multiplication of e_vector and x_norm using our
    function from our LA.py. Then creates negative_sub_x which is set to equal the scalar vector multiplicaiton of sub_x
    and -1. V is then set to equal the sum of the vectors of x_e_vector and negative_sub_x using the add_vectors function
    from the LA.py file.

    Args:
        e_vector: A vector stored as a list of integers
        sub_x: A vector stored as a list of complex numbers
    Returns:
        The calculation for V stored as a list of complex numbers

    """
    x_norm: list[complex] = LA.p_norm(sub_x)
    x_e_vector: list[complex] = LA.scalar_vec_multi(e_vector,x_norm)
    negative_sub_x :list[complex] = LA.scalar_vec_multi(sub_x,-1)
    V: list[complex] = LA.add_vectors(x_e_vector,negative_sub_x)
    return [V]

def calc_F(V: list[complex])-> list[complex]:
    """Calcualte F for the householder factorization
    Creates v_transpose which is set to equal the conjugate transpose of V using the con_transpose function. Then creates
    v_multi which is set to equal the matrix matrix multiplication of V and v_transpose using matr_matr_multi from LA.py.
    Creates ident which is equal to matrix identity of v_multi using the matrix_ident function. Then v_inner is created
    and is set to equal the inner product of V[0] and V[0] using the inner_product function from LA.py. Then creates scale_matr
    which equals the scalar matrix multiplication of v_multi and 2/v_inner usinf our scalar_matrix_multi from LA.py.
    Creates negative_scal_matrix which stoeds the scalar matrix multiplication of scale_matr and -1. Last F is set to
    equal the matrix addition of ident and negative_scal_matrix.

    Args:
         V: A vector stored as a list of complex numbers
    Returns:
        The calculation for F stored as a vector or matrix with complex numbers

    """
    v_transpose: list[complex] = con_transpose(V)
    v_multi: list[complex] = LA.matr_matr_multi(V,v_transpose)
    ident : list[list[int]]= matrix_ident(v_multi)
    v_inner: complex = LA.Inner_product(V[0],V[0])
    scale_matr: list[list[complex]] = LA.scalar_matrix_multi(v_multi ,(2/v_inner))
    negative_scal_matrix: list[list[complex]]= LA.scalar_matrix_multi(scale_matr,-1)
    F: list[list[complex]] = LA.matrix_add(ident,negative_scal_matrix)
    return F
    Q = identity_matrix

def cal_Q(identity_matrix: list[list[int]], F:list[list[complex]], i: int)-> list[list[complex]]:
    """Calculates Q for the householder factorization
    Creates Q which is set to equal the length of the columns in the identity matrix and sets the elements to zero.
    using a for loop for the columns and rows in the identity_matrix Q is then set to equal the identity matrix which contains
    the correct amount of columns and rows. After that using another for loop for the columns and rows using the length
     of Q-1. Q is then set to equal F using the number of columns and rows plus i.

     Args:
         identity_matrix: A matrix stored as a list of lists of integers
         F: Matrix stores as a list of lists of complex numbers
         i: an integer
    Returns:
        The calculations for Q stored as a list of list of complex numbers


    """
    Q : list[list[float]] = [([0] * (len(identity_matrix[0]))) for i in range (len(identity_matrix))]
    for column in range(len(identity_matrix)):
        for row in range(len(identity_matrix[0])):
            Q[column][row] = identity_matrix[column][row]
    for column in range(len(Q)-i):
        for row in range(len(Q[0])-i):
            Q[column+i][row+i] = F[column][row]
    return Q

def cal_final_Q(Q_List: list[list[list[complex]]])-> list[list[complex]]:
    """Calculates the final Q for the householder factorization
    Creates a Q set to equal Q-List[0]. Then for the number of index within the length of Q_List -1 Q is set to equal the
    matrix matrix multiplication of Q and Q_List[index+1] using matr_matr_multiplication from LA.py

    Args:
          Q_list: A matrix stored as list of lists of complex numbers
    Returns:
        Final calultion of Q stored as a list of lists of complex numbers

    """

    Q: list[list[complex]]= Q_List[0]
    for index in range(len(Q_List)-1):
        Q = LA.matr_matr_multi(Q,Q_List[index+1])
    return Q

def householder_ortho(matrix1:list[list[complex]])->list[list[complex]]:
    """Calculates the householder orthonormal
    Creates R set to equal an empty list. Then creates Q_list which is set to equal an empty list. The identity_matrix
    is then set to equal the matrix_ident of matrix1. Then using a for loop with the elements in matrix1 append the
    elements to R. For i in the range of the length of matrix1-1 set the identity_matrix equal to matrix_ident of matrix1.
    Then the identity_column is set to equal the diagonal_column of the identity_matrix and i. X is then set to equal the
    diagonal_column of R and i. V is set to equal calc_V of the identity_column and x. F is set to equal cal_F of V. Q
    is set to equal calc_Q of the identity_matrix, F and i. R is set to equal the matrix matrix multiplication of R and Q.
    Last Q is overwrite to equal the cal_final_Q of the Q_List.
    
    Args:
        matrix1: A matrix stored as a list of lists of complex numbers
    Returns:
        QR factorization using the householder method stored as a list of lists of complex numbers.


    """
    R:list[list[complex]] = []
    Q_List : list[complex] = []
    identity_matrix: list[list[int]] = matrix_ident(matrix1)
    for element in matrix1:
        R.append(element)
    for i in range(len(matrix1)-1):
        identity_matrix = matrix_ident(matrix1)
        identity_column:list[int] = diagonal_column(identity_matrix, i )
        x: list[complex] = diagonal_column(R, i)
        V: list[complex] = calc_V(identity_column,x)
        F: list[list[complex]] = calc_F(V)
        Q: list[list[complex]] = cal_Q(identity_matrix,F,i)
        Q_List.append(Q)
        R = LA.matr_matr_multi(R,Q)
    Q = cal_final_Q(Q_List)
    return [Q,R]

print(householder_ortho([[2,2,1],[-2,1,2],[1,3,1]]))






