numbers_count = int(input())
even_sum = 0
odd_sum = 0

for i in range(1, numbers_count +1 ):
    current_sum = int(input())

    if i % 2 == 0:
        even_sum += current_sum
    else:
        odd_sum += current_sum

if even_sum == odd_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    diff = abs(even_sum - odd_sum)
    print('No')
    print(f'Diff = {diff}')