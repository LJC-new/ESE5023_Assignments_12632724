a = float(input("请输入 a : "))
b = float(input("请输入 b : "))
c = float(input("请输入 c : "))
def Print_values(a, b, c):
    if a > b:
        if b > c:
            print(f"{a}, {b}, {c}")
        else:  # b <= c
            if a > c:
                print(f"{a}, {c}, {b}")
            else:  # a <= c
                print(f"{c}, {a}, {b}")
    else:  # a <= b
        if b > c:
            print(f"{c}, {a}, {b}")
        else:  # b <= c
            print(f"{c}, {b}, {a}")
Print_values(a, b, c)




