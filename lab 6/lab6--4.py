num = 8642

last = num % 10

first = num
while first >= 10:
    first //= 10

print("First digit:", first)
print("Last digit:", last)
