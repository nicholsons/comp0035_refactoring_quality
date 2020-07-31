# Adapted from Java example from COMP0010 by Sergey Mechtaev

sum_a = 0
list_a = []

for x in range(3):
    list_a.append(x)
    sum_a += x

avg_a = sum_a / 3

sum_b = 0
list_b = []

for x in range(4):
    list_b.append(x)
    sum_b += list_b[x]

avg_b = sum_b / 4

print(avg_a)
print(avg_b)


# Refactored code
def calculate_average(a, n):
    sum = 0
    for x in range(n):
        sum += a[x]
    return sum / n


avg_a = calculate_average(list_a, 3)
avg_b = calculate_average(list_b, 4)
print(avg_a)
print(avg_b)
