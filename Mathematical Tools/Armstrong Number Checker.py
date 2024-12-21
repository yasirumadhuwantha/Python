print("======================================================")
print("               Armstrong Number Checker               ")
print("======================================================")
# User Inputs & Variables
number = input("Enter a number : ")
print("-----------------------------------------------------")
length = len(number)
n = int(number)  # Declared for Calculations
powers = 0  # Sum of Powers
count = n
# Loop
while n > 0:
    digits = n % 10
    powers = powers + digits ** length
    n = n // 10
if powers == count:
    print(number, "is an Armstrong Number")
else:
    print(number, "is not an Armstrong Number")
# End
print("======================================================")
