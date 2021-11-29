import LS


def test_least_squares():
    matrix1 = [[3,4,0],[-6,-8,1]]
    vector1 = [-1,7,2]
    matrix2 = [[4, 5, 0, 6], [2, -6, 3, 5]]
    vector2 = [-1,7,2,9]
    assert LS.least_squares(matrix1,vector1) == [(1+0j), (1.9999999999999991+0j)]
    assert LS.least_squares(matrix2,vector2) == [(1.1038961038961037+0j), (-0.02502662406815772+0j)]
