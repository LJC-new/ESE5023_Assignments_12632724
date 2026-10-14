def Find_expression(target):
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    results = []
    for code in range(3 ** 8):
        choice = []
        c = code
        for _ in range(8):
            choice.append(c % 3)
            c = c // 3
        expr = str(digits[0])
        value = digits[0]
        last = digits[0]
        for i in range(8):
            d = digits[i + 1]
            if choice[i] == 0:              
                expr = expr + "+" + str(d)
                value = value + d
                last = d
            elif choice[i] == 1:            
                expr = expr + "-" + str(d)
                value = value - d
                last = -d
            else:                            
                expr = expr + str(d)
                if last >= 0:
                    new_last = last * 10 + d
                else:
                    new_last = last * 10 - d
                value = value - last + new_last
                last = new_last
        if value == target:
            results.append(expr)
    for expr in results:
        print(expr + "=" + str(target))
    return results
Find_expression(50)

import matplotlib.pyplot as plt
def Find_expression(target, show=False):
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    results = []

    for code in range(3 ** 8):
        choice = []
        c = code
        for _ in range(8):
            choice.append(c % 3)
            c = c // 3

        expr = str(digits[0])
        value = digits[0]
        last = digits[0]

        for i in range(8):
            d = digits[i + 1]
            if choice[i] == 0:              
                expr = expr + "+" + str(d)
                value = value + d
                last = d
            elif choice[i] == 1:            
                expr = expr + "-" + str(d)
                value = value - d
                last = -d
            else:                            
                expr = expr + str(d)
                if last >= 0:
                    new_last = last * 10 + d
                else:
                    new_last = last * 10 - d
                value = value - last + new_last
                last = new_last

        if value == target:
            results.append(expr)

    if show:
        for expr in results:
            print(expr + "=" + str(target))

    return results

Total_solutions = []
for i in range(1, 101):
    Total_solutions.append(len(Find_expression(i)))

print("Total_solutions =")
print(Total_solutions)
print()

max_count = max(Total_solutions)
min_count = min(Total_solutions)

max_numbers = []
min_numbers = []
for idx in range(100):
    if Total_solutions[idx] == max_count:
        max_numbers.append(idx + 1)
    if Total_solutions[idx] == min_count:
        min_numbers.append(idx + 1)

print("最大解数量：", max_count)
print("对应的数：", max_numbers)
print()
print("最小解数量：", min_count)
print("对应的数：", min_numbers)

plt.figure(figsize=(15, 6))
plt.bar(range(1, 101), Total_solutions, color="steelblue", edgecolor="black")
plt.xlabel("Integer i (1 ~ 100)")
plt.ylabel("Number of solutions")
plt.title("Total_solutions: number of solutions for each integer 1~100")
plt.xticks(range(1, 101, 5))
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()