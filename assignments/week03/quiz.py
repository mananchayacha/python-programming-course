# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
if age <=12 :
    print("Child")
elif age <=19 :
    print("teenager")
elif age <=59 :
    print("Adult")
else :
    print("Senior")




# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance") #เงินในบัญชี
        print("2. Withdraw") #ถอนเงิน
        print("3. Deposit") #ฝากเงิน
        print("4. Exit") 
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
if choice == "1":
    print("Balance", Balance, "บาท")
elif choice == "2":
    withdarw = float(input("Amout: "))
    Balance = Balace - witdraw
elif choice == "3":
    desposit = float(input("Amout: "))
    Balance = Balace + desposit
elif choice == "4":
    break
     
else:
    print("Invalid PIN")
