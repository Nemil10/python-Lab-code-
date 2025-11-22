num = 234
product = 1

while num > 0:
    digit = num % 10
    product *= digit
    num //= 10

print("Product of digits is:", product)