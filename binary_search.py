numbers = []

print("\n\nentering numbers in list\n")

for i in range(10):
    while True: 
        try:
            value = int(input(f"enter number for index a[{i}] : ")) 
            numbers.append(value)
            break

        except ValueError:
            print("\ninvalid input....\n")

# binary search

numbers.sort()


target = int(input("\nenter a numbers to search in array : "))

low = 0
high = len(numbers) - 1

while low <= high :

    middle = low + (high - low) // 2

    if numbers[middle] == target  :
        print(f"\n\nnumber ({target}) found at index {middle}\n")
        break

    elif numbers[middle] > target :
        high = middle - 1

    else :
        low = middle + 1
        
else:
    print("number not found")
    