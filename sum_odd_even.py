sum_a = 0
sum_b = 0
sum_diff = 0

n = int(input())
for i in range(n):
    number = int(input())
    if (i % 2) == 0:
        sum_a = sum_a + number
    else:
        sum_b = sum_b + number
    i = i + 1

if sum_a == sum_b:
    print("Yes")
    print("Sum =", sum_a)
elif sum_a > sum_b:
    sum_diff = sum_a - sum_b
    print("No")
    print("Diff =", sum_diff)
else:
    sum_diff = sum_b - sum_a
    print("No")
    print("Diff =", sum_diff)