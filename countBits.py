def countBits(n):
    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n = n - (n % 2)
        n = n / 2
    return count