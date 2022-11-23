from math import factorial as f


def z(n, an, bn):
    result = 0
    for i in range(3, n):
        result += 3 ** i / ((1 + an[i - 1] ** 2 + bn[i - 1] ** 2) * f(i))

    return result


n = int(input("n = "))

a1 = b1 = 2
a2 = 3 * b1
b2 = 2

an = [a1, a2]
bn = [b1, b2]
for i in range(3, n):
    ai = 2 * b1 + a1
    bi = 3 * a1 + 0.5 * b1
    a1 = a2
    b1 = b2
    a2 = ai
    b2 = bi
    an.append(ai)
    bn.append(bi)

print(an)
print(bn)
print(z(n, an, bn))
