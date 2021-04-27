#Addition of two matrices
import numpy as np
a1=np.array([[11,12,13],[14,15,16],[17,18,19]])
a2=np.array([[1,2,3],[5,6,7],[4,10,20]])
print("The given matrix is \n ",a1)
print("")
print(a2)
a_add=a1+a2
print("Result of addition of two matrices:")
print(a_add)


#Subtration of two matrices
a_sub=a1-a2
print("Result of substration of two matrices:")
print(a_sub)


#Multiplication of two matrices
result=np.array([[0,0,0],[0,0,0],[0,0,0]])
for i in range(len(a1)):
    for j in range(len(a2[0])):
        for k in range(len(a2)):
            result[i][j]+=a1[i][k]*a2[k][j]
print("Result of multiplication of two matrices:")
for r in result:
    print(r)
