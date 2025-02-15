# Get user input
customer_id = input("Enter Customer ID: ")
customer_name = input("Enter Customer Name: ")
units = float("Enter Units Consumed: ")
 # Determine charges per unit 
if units <= 199:
    rate = 1.20
elif units < 400:
    rate = 1.50
elif units < 600:
    rate = 1.80
else:
    rate = 2.00

# Calculate total bill
bill = units * rate

# Apply 15% surcharge if bill exceeds 400
if bill > 400:
    bill += bill * 0.15
    
# Ensure minimum bill is 100 Kshs
bill =  max(bill, 100)
 # Display the bill
print(f"\nCustomer ID: {customer_id}")
print(f"Customer Name: {customer_name}")
print(f"Units Consumed: {units}")
print(f"Charge per Unit: Kshs {rate}")
print(f"Total Amount to Pay: Kshs {bill:.2f}")
