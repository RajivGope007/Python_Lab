principle=float(input("Enter the Princple:-"))
rate=float(input("Enter the Rate:- "))
time=float(input("Enter number of years:-"))
Amount = principle * (pow((1 + rate / 100), time))
print("Amount is Rs.",Amount)