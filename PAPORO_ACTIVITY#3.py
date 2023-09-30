# Get the input from the user
purchase_amount = float(input("Enter purchase amount: "))

# Calculate the sales tax (6%)
sales_tax = purchase_amount * 0.06

# Display the result with two digits after the decimal point
print(f"Sales tax is {sales_tax:.2f}")