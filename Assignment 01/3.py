def Pascal_triangle(k):
    hang = [1]
    for i in range(1, k + 1):
        xin_hang = [1]
        for j in range(1, i):
            xin_hang.append(hang[j - 1] + hang[j])
        xin_hang.append(1)
        hang = xin_hang
    return hang
print(Pascal_triangle(100))

print(Pascal_triangle(200))