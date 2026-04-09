n = 5
for i in range (n): # i = 0, 1, 2, 3, 4 
    print(" " * (n - 1 -i) + "*" * (i+1)) #
#     *
#    **
#   ***
#  ****
# *****
# *****
#  ****
#   ***
#    **
#     *

for i in range(n):
    print(" " * i + "*" * (n-i))

for i in range(n):
    print("*" * (i+1))

for i in range(n):
    print("*" * (n-i))

# *
# **
# ***
# ****
# *****
# *****
# ****
# ***
# **
# *