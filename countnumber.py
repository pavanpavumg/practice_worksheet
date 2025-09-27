def getwordscount(string):
    if len(string.strip()) == 0:
        return 0  

    counter = 1  

    for char in string:
        if char == ' ' or char == '\t' or char == '\n':
            counter += 1

    return counter

def invoke_getwordcount():
    input = ""
    count = getwordscount(input)
    print(f"Count of words = {count}")

invoke_getwordcount()
