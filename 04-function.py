def min_max(a, b, c):
    min = a
    max = a
    if b < min:
        min = b
    if c < min:
        min = c
    if b > max:
        max = b
    if c > max:
        max = c
    return min, max
min, max = min_max(100, 200, 300)
print(min)
print(max)
print("min is:",min,"\nmax is:",max)  # 可以就是分开写的print函数就是