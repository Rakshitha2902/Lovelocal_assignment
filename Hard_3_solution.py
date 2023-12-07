def count_digit_one(n):
    count = 0
    factor = 1
    i = 1
    
    while i <= n:
        divider = i * 10
        count += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
        i *= 10

    return count
n = int(input())
result = count_digit_one(n)
print(result)