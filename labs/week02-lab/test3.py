shopping_calculator = '''
# Shopping Calculator Template

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

# TODO: Calculate subtotal ราคาเต็มเท่าไหร่
subtotal = item_price * quatity 

# TODO: Calculate discount amount ได้ส่วนลด
discond = subtotal * (discount_prrcent / 100)

# TODO: Calculate price after discountราคาหลังส่วนลด
price = subtotal - discount

# TODO: Calculate tax amount ภาษีเท่าไหร่
tax = price * (tax_percent / 100)

# TODO Calculate final total สรุปต้องจ่ายเท่าไหร่
final_total = price + tax

# TODO: Display itemized receipt พ่นออกมาทางหน้าจอ
print("subtotal =", subtotal)
print("discound =", + str(discount))
print ("price after discount =", price)
print(f"Tax amount = {tax} and final total = {final_total}")