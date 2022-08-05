#Factorial
#5!=5*4*3*2*1

num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial *i
print(f"The factorial of the number is :{factorial}")
