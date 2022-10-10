sum_a = 0
sum_b = 0
sum_diff = 0

n = int(input())
for i in range(n):
    number = int(input())
    sum_a = sum_a + number
    i = i + 1
for i in range(n):
    number = int(input())
    sum_b = sum_b + number
    i = i + 1

if sum_a == sum_b:
    print("Yes, sum =", sum_a)
elif sum_a > sum_b:
    sum_diff = sum_a - sum_b
    print("No, diff =", sum_diff)
else:
    sum_diff = sum_b - sum_a
    print("No, diff =", sum_diff)