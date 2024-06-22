def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(3):
        if a[i] > b[i]:
            alice = alice + 1 
        elif b[i] > a[i]:
            bob = bob + 1
    return [alice, bob]

a = [1, 2, 3]
b = [3, 2, 1]
result = compareTriplets(a, b)
print(result)