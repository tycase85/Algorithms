def pascal(n, k):
    total = 0
    if k is 0 or k is n:
        return 1
    if k >= 0 and n-1 >= k:
        return pascal(n-1, k-1) + pascal(n-1, k)


print pascal(10, 3)
print pascal(5, 4)
