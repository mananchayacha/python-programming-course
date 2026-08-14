"""
เขียน FUNCHTIONแปลงหน่วยสกุลเงิน ที่สามารถแปลงเงินจาก 
THB <->USD...1 USA = 32 THB

โดยใช้ชื่อและการใช้งาน
function convert_currency(100, "USA")
100 THB = 3.3 USD

และทดสอบการใช้งาน functon ที่ตัวเองเขียน
"""

def convert_currency(a, b):
    if b == "USA":
     print(f"{a} THB = {a / 32.0} USD")
    else:
     print(a, "USD =", a * 32.0, "THB")

convert_currency(100, "USD")
convert_currency(100, "THB")
