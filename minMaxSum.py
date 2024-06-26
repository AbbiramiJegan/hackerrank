def miniMaxSum(arr):
    min_element = arr[0]
    max_element = arr[0]
    sum = 0

    for i in range(len(arr)):
        sum = arr[i] + sum
        if arr[i] < min_element:
            min_element = arr[i]
        if arr[i] > max_element:
            max_element = arr[i]

    min_sum = sum - max_element
    max_sum = sum - min_element

    print(min_sum, max_sum)

arr = [1, 2, 3, 4, 5]
miniMaxSum(arr)