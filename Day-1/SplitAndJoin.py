#program that replaces "space" with "-". Split and join method is used.
#test case 1)othere shouldn't be multiple "-"  2) what'll be the output if we have a newline in between? 3)create a text file with multiple lines and test it.

def replace(a):
    b = a.split(" ")
    c = "-".join(b)
    return c
string = input("Enter a string: ")
print(replace(string))


#or

def replace2(a):
    parts = a.split()
    return "-".join(parts)

filename = "test_input.txt"

with open(filename, 'r') as file:
    content = file.read()
result = replace2(content)
print("Processed text: ")
print(result)