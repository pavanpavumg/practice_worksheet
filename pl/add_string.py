def counting_string(char):
    readIndex = 0
    writeindex = 0
    n = len(char) - 1

    while readIndex < n:
        current_char = char[readIndex]
        count = 0

        while readIndex < n and char[readIndex] == current_char:
            readIndex+=1
            count+=1
            char[writeindex] = current_char
            writeindex+=1

            if count > 1:
                for digit in str(count):
                    char[writeindex] = digit
                    writeindex+=1
            del char[writeindex:]
            return len(char)
if __name__ == "__main__":
    data = ["a","a","a","a","b","b","c"] 
    counting_string(data)       
          