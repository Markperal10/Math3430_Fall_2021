import LA


def test_add_vectors():
    test_vector_01 = [3, 2, 6]
    test_vector_02 = [4, 6, 8]
    test_vector_03 = [5, 1, 7]
    assert LA.add_vectors(test_vector_01, test_vector_02) == [7, 8, 14]
    assert LA.add_vectors(test_vector_01, test_vector_03) == [8, 3, 13]


def test_scalar_vec_multi():
    vector1 = [3, 2, 6]
    scalar1 = 2
    vector2 = [2, 4, 5]
    scalar2 = 4
    assert LA.scalar_vec_multi(vector1, scalar1) == [6, 4, 12]
    assert LA.scalar_vec_multi(vector2, scalar2) == [8, 16, 20]


def test_scalar_matrix_multi():
    matrix1 = [[3, 2, 6], [4, 3, 4], [1, 2, 3]]
    scalar1 = 2
    matrix2 = [[6, 2, 1], [8, 4, 2], [4, 5, 6]]
    scalar2 = 3
    assert LA.scalar_matrix_multi(matrix1, scalar1) == [[6, 4, 12], [8, 6, 8], [2, 4, 6]]
    assert LA.scalar_matrix_multi(matrix2, scalar2) == [[18, 6, 3], [24, 12, 6], [12, 15, 18]]


def test_matrix_add():
    matrix1 = [[4, 7], [2, 8]]
    matrix2 = [[3, 5], [1, 6]]
    matrix3 = [[8, 9], [5, 2]]
    matrix4 = [[3, 4], [5, 6]]
    assert LA.matrix_add(matrix1, matrix2) == [[7, 12], [3, 14]]
    assert LA.matrix_add(matrix3, matrix4) == [[11, 13], [10, 8]]


def test_matr_vec_multi():
    matrix1 = [[3, 4], [5, 6]]
    vector1 = [2, 4]
    matrix2 = [[2, 8], [3, 9]]
    vector2 = [4, 5]
    assert LA.matr_vec_multi(matrix1, vector1) == [26, 32]
    assert LA.matr_vec_multi(matrix2, vector2) == [23, 77]


def test_matr_matr_multi():
    matrix1 = [[3, 4], [5, 6]]
    matrix2 = [[2, 4], [5, 7]]
    matrix3 = [[8, 2], [3, 1]]
    matrix4 = [[1, 6], [9, 7]]
    assert LA.matr_matr_multi(matrix1,matrix2) == [[26,32],[50,62]]
    assert LA.matr_matr_multi(matrix3,matrix4) == [[26,8],[93,25]] 