# Expense Tracker - Installment 5: the menu comes alive
# Author: Luiz Mandy R. Moldes
# Shows a menu that repeats until the user chooses Exit

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

# setup questions, asked only once
name = input("\nWhat's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

subtotal = 0
count = 0
choice = ""

while choice != "4":
    print("\nMAIN MENU")
    print("\t[1] Add an expense")
    print("\t[2] View all expenses\t(coming soon)")
    print("\t[3] Show total spent")
    print("\t[4] Exit")
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")
    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")
    elif choice == "3":
        tax = subtotal * tax_percent / 100
        total = subtotal + tax
        over_budget = total > budget
        left = budget - total
        print(f"Expenses:\t\t{count}")
        print(f"Subtotal:\t\t${subtotal}")
        print(f"Tax ({tax_percent}%):\t\t${tax}")
        print(f"Grand total:\t\t${total}")
        if over_budget:
            print(f"Over budget by ${total - budget}!")
        elif total > budget * 0.9:
            print(f"Careful: only ${left} left.")
        else:
            print(f"Within budget. ${left} left.")
    elif choice == "4":
        print(f"Goodbye, {name}!")
    else:
        print("  Please choose 1, 2, 3 or 4.")

print("-" * 40)
print("Made by: Luiz Mandy R. Moldes  |  Installment 5")
print("=" * 40)