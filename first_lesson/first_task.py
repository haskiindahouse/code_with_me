n = int(input("n = "))
a = 1
b = 2
result = 1
for i in range(0, n):
    c = a / b
    result *= c
    a += 2
    b += 2

print(result)
