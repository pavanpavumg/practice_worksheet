def sum_of_digits(n):
    temp = 0
    while n > 0:
        dig = n % 10
        temp += dig
        n = n // 10
    return temp

num1 = int(input("enter n1 number: "))
num2 = int(input("enter n2 number: "))

sum1 = sum_of_digits(num1)
sum2 = sum_of_digits(num2)

sum1 = sum_of_digits(num1)
sum1 = sum_of_digits(num2)

print("Sum of digits of first number:", sum1)
print("Sum of digits of second number:", sum2)


