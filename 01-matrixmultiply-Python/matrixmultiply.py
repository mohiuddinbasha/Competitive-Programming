# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    for x in m1:
        if len(x) != len(m2):
            return None
    l = []
    for x in range(len(m1)): #Final rows length means length of matrix1
        temp = []
        for y in range(len(m2[0])): #Final columns length means length of matrix2 element
            s = 0
            for z in range(len(m2)): #Loop through matrix2
                s += (m1[x][z] * m2[z][y]) #Remember this and try to get this by using examples on paper
            temp.append(s)
        l.append(temp)
    return l



