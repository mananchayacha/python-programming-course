name = input("Enter name: ")
vowels = ('a', 'e', 'i', 'o', 'u')
count = 0

for c in name.lower():
    if c.isalpha() and c not in vowels:
     count = count + 1
print ("consonant count: ", count)