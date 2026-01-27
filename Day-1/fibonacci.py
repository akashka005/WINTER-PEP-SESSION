#function: input must be in number and it prints the first 5 numbers of fibonacci series
def fib_s(n):
    if n<=0:
        return
    else:
        a, b = 0, 1
        count = 0
        while count < 5:
            print(a, end = ' ')
            a, b = b, a + b
            count += 1
num = int(input("Enter a number: "))
fib_s(num)

#using recursion

def fib_sr(n, a = 0, b = 1, c = 0):
    if c == n:
        return
    print(a, end = ' ')
    fib_sr(n, b, a+b, c+1)

num = int(input("Enter a number: "))
if num > 0:
    fib_sr(num)
else:
    print("Enter a positive number")
