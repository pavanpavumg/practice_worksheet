
# try:
#     filename = input("entare your file name")
#     f = open(filename,"r")
#     print("open file ")
# except FileNotFoundError:
#     print("eror: file does not found")

# finally:
#     print("program end")

file_search = input("enter file to search")

try:
    f = open("friend.text" "r")
    for line in f:
        if file_search in line:
            print("found")
            
        
except FileNotFoundError:
    print("file not found")




