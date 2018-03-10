matrix1 = [[2, 3], [4, 7]]
matrix2 = [[-3, 5], [-3, 7]]
matrix3 = []


def matmult(first, second):
    matrix3.append([(first[0][0] * second[0][0] + first[0][1] * second[1][0]),
                    (first[0][0] * second[0][1] + first[0][1] * second[1][1])])
    matrix3.append([(first[1][0] * second[0][0] + first[1][1] * second[1][0]),
                    (first[1][0] * second[0][1] + first[1][1] * second[1][1])])
    print matrix3


matmult(matrix1, matrix2)
