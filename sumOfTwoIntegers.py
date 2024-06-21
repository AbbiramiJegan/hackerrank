def simpleArraySum(arr):
    sum = 0
    for i in range (len(arr)):
        sum = sum + arr[i]
    return sum

arr = [1, 2, 3, 4, 10, 11]
result = simpleArraySum(arr)
print(result)