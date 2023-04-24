def sieb(lower=2, n=1000):
    upper = n
    A = []

    if lower < 2:
        return -1
    if lower > upper:
        return -1

    for i in range(lower, upper + 1):
        a = 2
        A.append(i)
        while a < upper + 1:
            if i % a == 0 and i != a:
                a = upper + 1
                A.remove(i)
            a = a + 1

    return A

print(sieb(5,100))
#print(sieb(n=10001))

#print(sieb(2,100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])


