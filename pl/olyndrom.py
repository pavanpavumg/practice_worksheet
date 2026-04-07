def isPolindrom(string: str)->bool:
    leftIndex = 0
    righttIndex =len(string)-1
    result = True

    while(leftIndex < righttIndex):
        if string[leftIndex] != string[righttIndex]:
            result = False
            # break

        leftIndex+=1
        righttIndex-=1
    return result

input1 = "abdcba"
input2 = ""

poly = isPolindrom(input1)

if poly:
    print("String is polundrom")
else:
    print("String is not a polyndrom")
    

