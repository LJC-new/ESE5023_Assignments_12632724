import random

M1 = []
for i in range(5):
    row = []
    for j in range(10):
        row.append(random.randint(0, 50))
    M1.append(row)
    
M2 = []
for i in range(10):
    row = []
    for j in range(5):
        row.append(random.randint(0, 50))
    M2.append(row)

print("M1 (5x10):")
for row in M1:
    print(row)

print("\nM2 (10x5):")
for row in M2:
    print(row)
    
def Matrix_multip(A, B):
    m = len(A)          
    n = len(B)          
    p = len(B[0])      
    result = []
    for i in range(m):
        row = []
        for j in range(p):
            row.append(0)
        result.append(row)
    for i in range(m):
        for j in range(p):         
            total = 0
            for k in range(n):      
                total = total + A[i][k] * B[k][j]
            result[i][j] = total

    return result

M3 = Matrix_multip(M1, M2)
print("\nM1 * M2 (结果为 5x5):")
for row in M3:
    print(row)