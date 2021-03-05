a = [3, -1, 6, 2, -7, 2, 1, 9, -5]
b = [5, -4, -2, 8, -7, 4, -10, 7, -6, 4]
x = [5, -6, 8, -7, 4, -10, 7, -6, 4]
arr = [-1, -1, -1, -1]

Max_sum = arr[0]
sum = arr[0]
for i in range(1, len(arr)):
    sum += arr[i]
    if sum < 0:
        sum = 0
    else:
        Max_sum = max(Max_sum, sum)

print(Max_sum)
