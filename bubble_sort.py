Size = 5

numbers = []

#taking input from users

print("\nentering elements in list \n")

for i in range(Size):
    while True:
        try:
            value = int(input(f"enter value for index numbers[{i}] : "))
            numbers.append(value)
            break
        except ValueError:
            print("\ninvalid input...\n")

#bubble sorting

for i in range(Size-1):

    swapped = 0

    for j in range(Size-i-1):
        if(numbers[j] > numbers[j+1]):
            numbers[j] , numbers[j+1] = numbers[j+1] , numbers[j]
            swapped = 1

    if(swapped == 0):
        break

#displaying numbers

print("the sorted number list is : \n")
print(numbers)
print("\n")