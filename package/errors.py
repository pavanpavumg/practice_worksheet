# try:
#     age = int(input("enter your age"))
#     span_year = 100 - age

#     if span_year > 0:
#         print(f"you will be alive 100 out of {span_year} years")
#     elif span_year == 0:
#         print("100 years old")
#     else:
#         print(f"you turned{-span_year} years ago.")
# except ValueError:
#     print("invalid input value verify your va;ue")

# print(age)


try:
    n1=int(input("enter first number"))
    n2 = int(input("enter second nimber"))

    div = n1 / n2

except ZeroDivisionError:
    print("it would be not speicfying")
     
print(n1,n2,div)

    