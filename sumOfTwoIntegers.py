def sumOfTwoIntegers(a, b):
    sum = a + b
    return sum

num1 = int(input('Please enter a number: '))
num2 = int(input('Please enter a number: '))
result = sumOfTwoIntegers(num1, num2)
print(str(num1) + " + " + str(num2) + " = " + str(result))