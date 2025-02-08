from datetime import datetime 

# Get user input
book_id = input("Enter Book ID: ")
due_date = input("Enter Due Date (YYYY -MM-DD): ")
return_date = input("Enter Return Date (YYYY -MM-DD): ")

# Convert dates to datetime objects
due_date = datetime.strptime(due_date, "%Y -%m -%d")
return_date = datetime.strptime(return_date, "%Y -%m -%d")

# Calculate overdue days
overdue_days = (return_date - due_date).days

# Determine fine
if overdue_days <= 0:
    fine = 0
    elif overdue_days <= 7:
        fine = overdue_days * 20
        elif overdue_days <= 14:
            fine = overdue_days * 50
            else:
                fine = 1000
                # Display results
                print("\nLibrary Fine Details")
                print(f"Book ID       : {book_id}")
                print(f"Days Overdue  : {max(overdue_days, 0)}")
                print(f"Fine Amount   : Kshs {fine}")
                