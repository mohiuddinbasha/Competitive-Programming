# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    for x in m1:
        if len(x) != len(m2):
            return None

    temp = [None]*len(m1)
    l = [temp for _ in range(len(m2[0]))]
    print(l)
    for x in range(len(m1)):
        for y in range(len(m2[0])):
            s = 0
            for z in range(len(m2)):
                s += (m1[x][z] * m2[z][y])
            print(s)
            l[x][y] = s
    return l
    




print(fun_matrixmultiply([[1,2,3],[4,5,6]],[[1,4],[2,5],[3,6]]))





