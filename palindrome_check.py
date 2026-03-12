def palindrome_check(number):

    temp = number 
    reverse = 0
    remainder = 0

    while temp != 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp = temp // 10

    if number == reverse:
        print(f"\nthe given number i.e ({number}) is palindrome.\n")
    else:
        print(f"\nthe given number ({number}) is not palindrome.\n")

    

def main():
    number = int(input("\nEnter a number to check whether the number is palindrome or not : "))

    palindrome_check(number)




if __name__ == "__main__":
    main()
