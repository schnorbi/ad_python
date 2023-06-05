A = [2, 4, 5, 20, 6]

def first_second_el(A):
    a = max(A)
    i = 1

    while i > 0:
        if a-1 in A:
            return a-1
        else:
            a = a - 1

def other_second_el(A):
    A.sort()
    return A[-2]

print(first_second_el(A))
print(other_second_el(A))