Actual_Cost = float(input("Please enter the Actual Product Price."))
Sales_Amount = float(input("Please enter the Sales Amount."))
if (Sales_Amount > Actual_Cost):
    Amount = Sales_Amount - Actual_Cost
    print ("Total Profit = {0}".format(Amount))
else:
   print ("No Profit!!!")