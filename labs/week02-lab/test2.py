print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

# input
second = int(input("input second is:"))

#process
hour = second // 3600
second_remain = second % 3600

minute = second_remain // 60
minute_remain = second_remain % 60

#output
  print ("Hour is:", hour)
  print ("minute is:", minute)
  print ("second is:", minute_remain)
  print(f"hour = {hour} and minute = {minute} and second ={minute_remain}")
