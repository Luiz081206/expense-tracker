# Expense Tracker - Installment 3: tracker does math
# Author: Luiz Mandy R. Moldes
# Asks for a name, two expenses, a tax rate and a budget, then prints a summary

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print("\t[1] Add an expense\t(coming soon)")
print("\t[2] View all expenses\t(coming soon)")
print("\t[3] Show total spent\t(coming soon)")
print("\t[4] Exit\t\t(coming soon)")

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
tax = subtotal * tax_percent / 100
total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

print()
print("-" * 40)
print("SUMMARY")
print(f"\t- {item1}:\t${amount1}")
print(f"\t- {item2}:\t${amount2}")
print(f"Subtotal:\t\t${subtotal}")
print(f"Average:\t\t${average}")
print(f"Tax ({tax_percent}%):\t\t${tax}")
print(f"Grand total:\t\t${total}")
print(f"Over budget?\t\t{over_budget}")
print(f"Left in budget:\t\t${left}")
print("-" * 40)
print("Made by: Luiz Mandy R. Moldes | Installment 3")
print("=" * 40)