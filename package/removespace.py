#function to remove space from string

def spacerRemove(String):
    output = ""

    for character in String:
        if character!= " " and character != '\t' and character!='\n':
            output=output+character
    print(output)

def invokw_remove():
    input="hwll h"
    spacerRemove(input)

invokw_remove()
