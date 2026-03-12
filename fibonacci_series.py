number = int(input("\nenter a number to generate fibonacci series to N th term : "))

first_term = 0
second_term = 1

print(f"{first_term}\n{second_term}")

for i in range (number):

    third_term = first_term + second_term
    first_term = second_term
    second_term = third_term 

    print(f"{third_term}")       

print("\n")