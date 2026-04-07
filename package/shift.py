#writ a prgram to binary and shifting operation

def printBinary(number:int):
    no_of_bit=number.bit_length()
    print(f"number of bits={no_of_bit}")

    mask = 1
    mask = mask<<no_of_bit-1

    for _ in range(no_of_bit):
        if(number&mask):
            print("1", end=" ")
        else:
            print("0", end="")

            mask= mask>>1




#invok function
printBinary(84)