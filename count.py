# n = int(input("Enter a number: "))
# x = int(input("enter a"))
# temp = 0

# while n > 0:
#     dig = n % 10
#     temp += dig
#     n = n // 10

# print("Sum of digits:", temp)




def sum_of_digits(n):
    temp = 0
    while n > 0:
        dig = n % 10
        temp += dig
        n = n // 10
    return temp

# Take two inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate and display sum of digits
sum1 = sum_of_digits(num1)
sum2 = sum_of_digits(num2)

print("Sum of digits of first number:", sum1)
print("Sum of digits of second number:", sum2)
