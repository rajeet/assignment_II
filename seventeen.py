# Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.


try:
    x = float(input("Enter First Number: "))
    y = float(input("Enter Second Number: "))
    op = int(input("Enter operand: \n 1: add \n 2: subtract \n 3: multiply \n 4: Division\n"))
except ValueError:
    print("Enter proper number")
print("===============================================")
if op == 1:
    print(x+y)
elif op == 2:
    print(x - y) 
elif op == 3:
    print (x*y)
elif op == 4:
    try:
        print(x/y)
    except ZeroDivisionError:
        print("number cannot devide by zero")
        
else:
    print("operand error")