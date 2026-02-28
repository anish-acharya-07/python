import sys

def main(operator , first_num , second_num ) :

    if operator == "+" :
       answer = first_num + second_num
    
    elif operator == "-" :
        answer = first_num - second_num
    
    elif operator == "*" :
        answer = first_num * second_num
    
    else :
        answer = first_num / second_num

    print(f"{first_num} {operator} {second_num} = {answer}")



print("\n**********WELCOME TO TEXT BASED CALCULATOR**********\n")

print("what would you like to do ? (+ , - , * , /) \n")

operator = input("enter your operator : ")

print("\n")
 
if operator not in ("+" , "-" , "*" , "/") :
   print("invalid syntax..\n")
   sys.exit()


first_num = int(input("enter first number : "))
second_num = int(input("enter second number : "))

if operator == "+" :
   main(operator,first_num,second_num)
elif operator == "-" :
    main(operator,first_num,second_num)
elif operator == "*" :
    main(operator,first_num,second_num)
else :
    main(operator,first_num,second_num)

 