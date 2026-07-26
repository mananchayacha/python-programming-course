"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese
"""

# input
weight = float(intput("Enter weight is:"))
height = float(input("Enter height is:"))

# process
BMI = weight / (hight ** 2)

# output
print ("BMI is:, {bmi:.1f}")

  if bmi < 18.5:
    print("Category: Underweight")
  elif 18.5 <= bmi <= 24.9:
    print("Category: Normol weight")
  elif 25.0 <= bmi  <= 29.9:
    print("Category: Over weight")
  else:
    print("Category: Obese")