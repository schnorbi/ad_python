def ggt(m, n):
    if m < 0 or n < 0 or (m == 0 and n == 0) or m % 1 != 0 or n % 1 != 0:
        return -1
    elif n != 0:
        return ggt(n, m % n)
    elif n == 0:
        return int(m)

#Testcases
print(ggt(15, 5))
print(ggt(-3, 2))
print(ggt(15, 0))
print(ggt(5, 15))
print(ggt(15.3, 3))
print(ggt(0, 0))
print(ggt(243, 13))
print(ggt(99, 11))
print(ggt(2, 8.0))