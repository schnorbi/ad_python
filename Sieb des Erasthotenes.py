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

#Testcases
print(sieb(1, 100))
print(sieb(2, 100))
print(sieb(2, 13))
print(sieb(n=10001))
print(sieb(lower=0, n=100))
print(sieb(lower=100, n=0))
print(sieb(1,100))
print(sieb(2,100))
print(sieb(2, 13))
print(sieb(n=10001))
print(sieb(lower=0, n=100))
print(sieb(lower=100,n=0))


