CP=int(input("Enter the cost price:"))
SP=int(input("Enter the selling price:"))
if SP>CP:
    amount=SP-CP
    print("Profit is",amount)
else:
    print("No profit")