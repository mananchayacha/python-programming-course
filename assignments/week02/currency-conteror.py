"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
# Currency Converter (THB <-> USD)
# Rate: 1 USD = 35.5 THB

print("1. Convert THB to USD")
print("2. Convert USD to THB")

choice = input("Enter choice (1 or 2): ")
amount = float(input("Enter amount: "))

rate = 35.5

if choice == "1":
    result = amount / rate
    print(f"Formula: {amount} / {rate}")
    print(f"Result: {result:.2f} USD")
elif choice == "2":
    result = amount * rate
    print(f"Formula: {amount} * {rate}")
    print(f"Result: {result:.2f} THB")
else:
    print("Invalid choice")