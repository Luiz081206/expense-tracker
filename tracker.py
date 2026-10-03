# Expense Tracker - Installment 2
# Author: Luiz Mandy R. Moldes
# Asks for the user's name and two expenses, then prints a summary

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

name = input("Enter your name: ")
print(f"\nWelcome, {name}! Let's log two expenses.\n")

print("MAIN MENU")
print("\t[1] Add an expense\t(coming soon)")
print("\t[2] View all expenses\t(coming soon)")
print("\t[3] Show total spent\t(coming soon)")
print("\t[4] Exit\t\t(coming soon)")
print()

item1 = input("Expense 1 - item name: ")
amount1 = float(input("Expense 1 - amount: "))
item2 = input("Expense 2 - item name: ")
amount2 = float(input("Expense 2 - amount: "))

total = amount1 + amount2
average = total / 2

print("-" * 40)
print("SUMMARY")
print(f"{item1:<25}{amount1:>10.2f}")
print(f"{item2:<25}{amount2:>10.2f}")
print(f"{'Total spent':<25}{total:>10.2f}")
print(f"{'Average':<25}{average:>10.2f}")
print("-" * 40)
print(f"Made by: {name} | Installment 2")
print("=" * 40)