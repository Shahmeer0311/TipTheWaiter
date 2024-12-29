def Tip (billAmount,T):
    total = billAmount * (1 + 0.01 * T)
    total = round(total,2)
    print("Please pay ", total)
billAmount = float(input("Enter the total Bill"))
T = float(input("Enter Tip"))
Tip(billAmount,T)