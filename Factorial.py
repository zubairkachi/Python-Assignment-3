def factorial(n):
    if n<1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter a number: "))
fact=factorial(num)
print("Factorial of ",num,"is : ",fact)