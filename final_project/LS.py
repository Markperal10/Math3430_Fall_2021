import LA
import QR




def back_sub(matrix1: list[list[complex]], vector2 : list[complex]) -> list[complex] :
    """ Computes the back substitution of the input matrix and vector.
    Create a result set to equal an empty list. Then result is overwritten with the first solution in back substitution.
    Then by using a for loop using a variable name current that goes from the length of matrix1 -2 ,-1,-1. Create a
    variable labeled as temp that stores vector2[current] within the variable. Another for loop is then created labeled index
    using the range of the length of the result. Within the for loop temp is overwritten with temp solution. This causes
    the index for loop to end and from there temp is overwrite again with 1 / coeffecient of the variable we are solving
    for. Then append temp into result.

    Args:
        matrix1: A matrix stored as a list of lists with complex or real numbers
        vector1: A vector stored as list of complex numbers or real numbers.
    Returns:
        The least square of the input variables stored as a list


    """
    result : list = [vector2[-1] * (1/(matrix1[-1][-1]))]
    for current in range(len(matrix1)-2,-1,-1):
        temp : float = vector2[current]
        for index in range(len(result)):
            temp -= matrix1[len(matrix1)-1-index][current]*result[current]
        temp *= 1/(matrix1[current][current])
        result.append(temp)
    result = result[::-1]
    return result


def least_squares(matrix1: list[list[complex]],vector1: list[complex]) -> list[complex]:
    """Calculates the Least Squares of out input matrix and vector
    Q_R is created and set to be the Q and R of matrix1. To get our Q and R we use the stable_Gram_Schmidt function
    from our QR file. Then create con_trans_Q and set it to equal the conjugate transpose of Q using the function
    from our QR file. Multi is then created and is set to equal the matrix vector multiplication of con_trans_q which
    would be the matrix and vector1 for the vector. This is worked out using the matr_vec_multi function from our QR file.
    Last result is created and set to equal the back substitution of matrix1 and vector1 which is done using the back_sub function.

    Args:
        matrix1: A matrix stored as a list of lists with complex or real numbers
        vector1: A vector stored as a list of complex or real numbers.
    Returns:
        The least squares of the input variables stored as a list


    """
    Q_R : list[list[list[complex]]] = QR.stable_Gram_Schmidt(matrix1)
    Q : list[list[complex]] = Q_R[0]
    R : list[list[complex]] = Q_R[1]
    conju_trans_Q : list[list[complex]] = QR.con_transpose(Q)
    Multi: list[complex] = LA.matr_vec_multi(conju_trans_Q,vector1)
    result : list[complex] = back_sub(R, Multi)
    return result
