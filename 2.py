num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(f"{num1}+{num2} = {num1 + num2}")
print(f"{num1}-{num2} = {num1 - num2}")
print(f"{num1}*{num2} = {num1 * num2}")
if (num2 != 0):
    print(f"{num1}/{num2} = {num1 / num2}")
else:
    print("Error: Division by zero")

