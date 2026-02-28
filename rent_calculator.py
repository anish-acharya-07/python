#room rent
#internet fee
#water bill
#electricity bill

ROOM_RENT = 4500
INTERNET_BILL = 150
ELECTRICITY_RATE = 15
WATER_BILL = 250

print("\n**********WELCOME TO RENT CALCULATOR PROGRAM**********\n")

electricity_unit = float(input("enter your electricity usage (unit) : "))

print("\n")

electricity_bill = ELECTRICITY_RATE * electricity_unit

print(f"your this month electricity bill is : {ELECTRICITY_RATE} * {electricity_unit} = {electricity_bill}")
print(f"your this month internet bill is : {INTERNET_BILL}")
print(f"your this month water bill is : {WATER_BILL}")
print(f"your this month room rent is : {ROOM_RENT}")

total = ROOM_RENT + INTERNET_BILL + WATER_BILL + electricity_bill

print("\n")

print(f"your total bill for this month is : {total}")

print("\n")






