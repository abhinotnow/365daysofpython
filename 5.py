num = int(input("Enter a number: "))
tablelength = int(input("Enter length of table: "))

for i in range(1,tablelength+1):
    print(f"{num}*{i} = {num*i}")
