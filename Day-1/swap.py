#swap case (input should store in string)

def swap(n):
    result = ""
    for char in n:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char
    return result
inp  = input("Enter a string: ")
print(swap(inp))


#or

a = input("Enter the input: ")
print(a.swapcase())