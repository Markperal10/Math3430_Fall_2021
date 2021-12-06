import LA
import QR
import LS

print("Hello My name is Mark Peralta and I am a Mathematics Major. My library contains three python files "
      "LA.py, QR.py, and LS.py which demonstrate different linear algebra methods.")

# LA.py
print("The first file is LA.py which demonstrates 10 different functions that perform linear algebra.")
print("The first function is add_vectors which adds two vectors together.")
print("Ex: if vector1 = [3,2,6] and vector2 = [4,6,8] then add_vectors will return")
vector1 = [3,2,6]
vector2 = [4,6,8]
print(LA.add_vectors(vector1,vector2))
print("\n")

print("The second function is scalar_vec_multi which multiplies a scalar and a vector and returns the product")
print("Ex: if vector1 = [3,2,6] and scalar1 = 2 then scalar_vec_multi will return")
vector1 = [3,2,6]
scalar1 = 2
print(LA.scalar_vec_multi(vector1,scalar1))
print("\n")

print("The third function is scalar_matrix_multi which multiplies the scalar and matrix and returns the product")
print("Ex:if matrix1 = [[3, 2, 6], [4, 3, 4], [1, 2, 3]] and scalar1 = 2 then scalar_matrix_multi will return")
matrix1 = [[3, 2, 6], [4, 3, 4], [1, 2, 3]]
scalar1 = 2
print(LA.scalar_matrix_multi(matrix1,scalar1))
print("\n")

print("The fourth function is matrix_add which adds two matrices together and returns the sum")
print("Ex: if matrix1 = [[4, 7], [2, 8]] and matrix2 = [[3, 5], [1, 6]], then \n"
      "matrix_add will return")
matrix1 = [[4, 7], [2, 8]]
matrix2 = [[3, 5], [1, 6]]
print(LA.matrix_add(matrix1,matrix2))
print("\n")

print("The fifth function is matr_vec_multi which computes the product of a matrix and a vector.")
print("Ex: if matrix1 = [[3, 4], [5, 6]] and vector1 = [2, 4] then ,matr_vec_multi will return")
matrix1 = [[3, 4], [5, 6]]
vector1 = [2, 4]
print(LA.matr_vec_multi(matrix1,vector1))
print("\n")

print("The sixth function is matr_matr_multi which computes the product of two matrices")
print("Ex: if matrix1 = [[3, 4], [5, 6]] and matrix2 = [[2, 4], [5, 7]] then matr_matr_multi will return")
matrix1 = [[3, 4], [5, 6]]
matrix2 = [[2, 4], [5, 7]]
print(LA.matr_matr_multi(matrix1,matrix2))
print("\n")


print("The seventh function is p_norm which calculates the p norm of a vector" )
print("Ex: if vector_B = [2,4,6] and p = 2 then p_norm will return")
vector_B = [2,4,6]
p = 2
print(LA.p_norm(vector_B,p))
print("\n")

print("The eighth function is inf_norm which computes the infinity norm of a vector")
print("Ex : if vector_1 = [4, 7, -9, 1] then inf_norm will return")
vector_1 = [4, 7, -9, 1]
print(LA.inf_norm(vector_1))
print("\n")

print("The ninth function is P_inf_norm_result which finds the p norm or infinity norm based "
      "off a given boolean.")
print("Ex : if vector_B = [2,4,6] , p =2, and boolean = False, then p_inf_norm_result will return")
vector_B = [2, 4, 6]
p = 2
boolean = False
print(LA.P_inf_norm_result(vector_B,p,boolean))
print("\n")

print("The tenth function is Inner_product which calculates the inner product of two vectors.")
print("Ex: vector1 = [3,4,5] and vector2 = [2,1,4] then inner_product will return")
vector1 = [3, 4, 5]
vector2 = [2, 1, 4]
print(LA.Inner_product(vector1,vector2))
print("\n")

# Pytests for each function in LA.py

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
    assert LA.matr_matr_multi(matrix1, matrix2) == [[26, 32], [50, 62]]
    assert LA.matr_matr_multi(matrix3, matrix4) == [[26, 8], [93, 25]]

def test_p_norm():
    p: int = 2
    vector_A = [1, 2, 3]
    vector_B = [2, 4, 6]
    assert LA.p_norm(vector_A, p) == 3.7416573867739413
    assert LA.p_norm(vector_B, p) == 7.483314773547883


def test_inf_norm():
    vector_1 = [4, 7, -9, 1]
    vector_2 = [3, -5, 7, 2]
    assert LA.inf_norm(vector_1) == 9
    assert LA.inf_norm(vector_2) == 7


def test_p_inf_norm_result():
    vector_B = [2, 4, 6]
    p: int = 2
    boolean = False
    boolean2 = True
    assert LA.P_inf_norm_result(vector_B, p, boolean) == 7.483314773547883
    assert LA.P_inf_norm_result(vector_B, p, boolean2) == 6


def test_inner_product():
    vector1 = [3,4,5]
    vector2 = [2,1,4]
    vector3 = [7,8,9]
    assert LA.Inner_product(vector1,vector2) == 30
    assert LA.Inner_product(vector2,vector3) == 58

# QR.py
print("The second python file is QR.py which contains three complex methods in linear algebra such as Gram-Schmidt,"
      "Orthonormal lists, and the Householder method.")

print("The eleventh function is stable_Gram_Schmidt which calculates the Q and R for QR factorization")
print("Ex : if matrix1 = [[1, 0, 1], [2, 1, 0]] and matrix2 = [[4, 3], [5, 6]] then stable_gram_schmidt will return")
matrix1 = [[1, 0, 1], [2, 1, 0]]
matrix2 = [[4, 3], [5, 6]]
print(QR.stable_Gram_Schmidt(matrix1))
print("\n")

print("The twelfth function is orthonormal_vectors which returns the orthonormal list of vectors from our input matrix.")
print("Ex : if matrix1 = [[5, 12], [15, 25]] then orthonormal_vectors will return")
matrix1 = [[5, 12], [15, 25]]
print(QR.orthonormal_vectors(matrix1))
print("\n")

print("The Thirteenth function is householder_ortho which implements Householder orthogonalization to calculate QR"
      " factorization ")
print("Ex :  if matrix7 = [[2,2,1],[-2,1,2],[1,3,1]] then householder_ortho will return")
matrix7 = [[2, 2, 1], [-2, 1, 2], [1, 3, 1]]
print(QR.householder_ortho(matrix7))
print("\n")

print(" #14 A pytest for each function in QR.py")
print("\n")
def test_stable_gram_schmidt():
    matrix1 = [[1, 0, 1], [2, 1, 0]]
    matrix2 = [[4,3],[5,6]]
    assert QR.stable_Gram_Schmidt(matrix1) == [[[0.7071067811865475, 0.0, 0.7071067811865475], [(0.577350269189626+0j), (0.5773502691896258+0j), (-0.5773502691896257+0j)]], [[1.4142135623730951, (1.414213562373095+0j)], [0, (1.7320508075688772+0j)]]]
    assert QR.stable_Gram_Schmidt(matrix2) == [[[0.8, 0.6000000000000001], [(-0.6000000000000008+0j), (0.7999999999999996+0j)]], [[5.0, (7.6000000000000005+0j)], [0, (1.7999999999999994+0j)]]]

def test_orthonormal_vectors():
    matrix1 = [[5,12],[15,25]]
    matrix2 = [[7,14],[20,27]]
    assert QR.orthonormal_vectors(matrix1) == [[0.38461538461538464, 0.9230769230769231], [(0.9230769230769229+0j), (-0.384615384615385+0j)]]
    assert QR.orthonormal_vectors(matrix2) == [[0.4472135954999579, 0.8944271909999159], [(0.8944271909999157+0j), (-0.4472135954999582+0j)]]

def test_householder_ortho():
    matrix1 = [[2,2,1],[-2,1,2],[1,3,1]]
    matrix2 = [[1,2,3],[3,2,1],[2,1,3]]
    assert QR.householder_ortho(matrix1) == [[[(0.6666666666666667+0j), (0.6666666666666666+0j), (0.3333333333333333+0j)], [(-0.7396002616336387+0j), (0.6471502289294337+0j), (0.18490006540840964+0j)], [(-0.09245003270420477+0j), (-0.3698001308168195+0j), (0.9245003270420487+0j)]], [[(0.33333333333333354+0j), (3+0j), (2.3333333333333335+0j)], [(-2.5886009157177354+0j), (-0.27735009811261446+0j), (0.7396002616336386+0j)], [(1.4792005232672785+0j), (2.2188007849009166+0j), (0.09245003270420477+0j)]]]
    assert QR.householder_ortho(matrix2) == [[[(0.2672612419124244+0j), (0.5345224838248488+0j), (0.8017837257372732+0j)], [(0.7246278635248041+0j), (0.4369928535473051+0j), (-0.5328711902064713+0j)], [(-0.6352053903855872+0j), (0.7234106442638908+0j), (-0.27053863271406486+0j)]], [[(3.474396144861517+0j), (2.4053511772118195+0j), (3.7416573867739413+0j)], [(0.9698640437537766+0j), (1.790370243937747+0j), (1.0122628735023032+0j)], [(0.9939492769779554+0j), (-0.0941281249574577+0j), (-1.9938214250350657+0j)]]]

# LS.py
print("The third python file is LS.py which contains one complex method in linear algebra which is used to find the"
      "corresponding least squares solution")

print("The fifteenth function is least_squares which takes a matrix and a vector"
      "and returns the corresponding least squares solution. ")
print(" Ex : if matrix1 = [[3, 4, 0], [-6, -8, 1]] and vector2 = [-1,7,2] then least_squares will return")
matrix1 = [[3, 4, 0], [-6, -8, 1]]
vector1 = [-1, 7, 2]
print(LS.least_squares(matrix1,vector1))
print("\n")

print(" #16 A pytest for each function in LS.py")
def test_least_squares():
    matrix1 = [[3,4,0],[-6,-8,1]]
    vector1 = [-1,7,2]
    matrix2 = [[4, 5, 0, 6], [2, -6, 3, 5]]
    vector2 = [-1,7,2,9]
    assert LS.least_squares(matrix1,vector1) == [(1+0j), (1.9999999999999991+0j)]
    assert LS.least_squares(matrix2,vector2) == [(1.1038961038961037+0j), (-0.02502662406815772+0j)]

