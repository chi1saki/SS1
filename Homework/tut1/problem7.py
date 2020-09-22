purchase = float(input("Enter the amount of a purchase: "))
statesaleTax = purchase*0.5
countysaleTax = purchase*0.25
totalsaleTax = statesaleTax + countysaleTax
totalsale = purchase + statesaleTax + countysaleTax
print("The amount of state sales tax is: ",format(statesaleTax,'.2f'))
print("The amount of county sales tax is: ",format(countysaleTax,'.2f'))
print("The total of sales tax is: ",format(totalsaleTax,'.2f'))
print("The toal of the sale is: ",format(totalsale,'.2f'))
