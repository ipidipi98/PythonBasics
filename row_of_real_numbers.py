number_list = []
n = int(input())
for i in range(n):
    number = int(input())
    number_list.append(number)
    i = i + 1

max_number = number_list[0]
min_number = number_list[0]

for i in range(len(number_list)):
    if number_list[i] > max_number:
        max_number = number_list[i]
    if number_list[i] < min_number:
        min_number = number_list[i]
    i = i + 1

print ("Max number:", max_number)
print ("Min number:", min_number)

