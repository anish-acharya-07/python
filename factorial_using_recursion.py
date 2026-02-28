#factorial using recursion

def factorial(number):
    if number < 0 :
         print("\nfactorial isn't defined for negative numbers \n")
         return "non defined"

    if number == 0 or number == 1 :
         return 1
    
    else :
         return number * factorial(number - 1)

print("\nwelcome to my program \n")

number = int(input("enter a number to calculate its factorial : "))

ans = factorial(number)
print(f"the factorial of {number} is {ans}\n")