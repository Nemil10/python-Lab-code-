num = 12345
last = num % 10

first = num
while first >= 10:
    first //= 10

middle = num % (10 ** (len(str(num)) - 1))
middle = middle // 10

new_num = (last * (10 ** (len(str(num)) - 1))) + (middle * 10) + first
print("Number after swapping first and last digits:", new_num)
