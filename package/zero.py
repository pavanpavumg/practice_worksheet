n = int(input("Enter a number: "))
place = 1
temp = 0

while n > 0:
    dig = n % 10
    if dig == 0:
        dig = 1
    temp += dig * place
    place *= 10
    n = n // 10

print("Modified number:", temp)
