def prime_composite(number):
    
    for i in range(2,number):

        if number % i == 0:
            return 1


def main():
    
    number = int(input("\nEnter a number to check whether it is prime or composite : "))

    check = prime_composite(number)

    if check != 1:
        print(f"the given number ({number}) is prime.")
    else:
        print(f"the given number ({number}) is composite.")



if __name__ == "__main__":
    main()