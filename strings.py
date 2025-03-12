"""This file covers python tutorial Strings"""
# print("It's alright")
# print("He is called 'Johnny'")
# print('He is called "Johnny"')
#
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)
#
# a = "Hello, World!"
# # print(a[1])
#
# for x in "banana":
#   print(x)

# a = "Hello, World!"
# print(len(a))
#
# txt = "The best things in life are free!"
# print("free" in txt)

# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")
#
# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is not in txt.")

#Slicing
# b = "Hello, World!"
# print(b[2:5])
# print(b[:5])
# print(b[6:])
# print(b[-5:-2])

#modify strings
# a = "Hello, World!"
# print(a.upper())
# # print(a.lower())
# b = "           Hello, World!        "
# print(b.strip()) # returns "Hello, World!"

# a = "Hello, World!"
# print(a.replace("H", "J"))
#
# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']

# #Concatenation
# a = "Hello"
# b = "World"
# c = a + b
# print(c)

#format string
# age = 30
# txt = f"My name is John, I am {age}"
# print(txt)

# price = 59
# txt = f"The price is {price} dollars"
# print(txt)

# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

# txt = f"The price is {20 * 59} dollars"
# print(txt)

#escape characters
# txt = "We are the so-called \"Vikings\" from the north."
# txt = "Hello\rWorld!"
# txt = "Hello\nWorld!"
# txt = "Hello\t World!"
# txt = "Hello \\ World!"
# print(txt)

#A backslash followed by three integers will result in a octal value:
# txt = "\110\145\154\154\157"

#A backslash followed by an 'x' and a hex number represents a hex value:
# txt = "\x48\x65\x6c\x6c\x6f"
# print(txt)

#String - Method
# txt = "Hello World"
# txt1 = txt.casefold()
# txt2 = txt.center(50)
# print (txt1)
# print (txt2)

# Define a sample string for testing
# sample_str = "Hello World"
# sample_num_str = "123"
# sample_space_str = "   "
# sample_list = ["a", "b", "c"]
#
# # Apply different string methods
# txt1 = sample_str.capitalize()
# txt2 = sample_str.casefold()
# txt3 = sample_str.center(20, '-')
# txt4 = sample_str.count('l')
# txt5 = sample_str.encode()
# txt6 = sample_str.endswith('!')
# txt7 = "Hello\tWorld".expandtabs(4)
# txt8 = sample_str.find('l')
# txt9 = "My name is {name}".format(name='John')
# txt10 = "My name is {name}".format_map({'name': 'John'})
# txt11 = sample_str.index('l')
# txt12 = "Hello123".isalnum()
# txt13 = "Hello".isalpha()
# txt14 = "Hello".isascii()
# txt15 = sample_num_str.isdecimal()
# txt16 = sample_num_str.isdigit()
# txt17 = "Hello".isidentifier()
# txt18 = "Hello".islower()
# txt19 = sample_num_str.isnumeric()
# txt20 = sample_str.isprintable()
# txt21 = sample_space_str.isspace()
# txt22 = "Hello World".istitle()
# txt23 = "HELLO".isupper()
# txt24 = "-".join(sample_list)
# txt25 = sample_str.ljust(20, '-')
# txt26 = sample_str.lower()
# txt27 = "   Hello".lstrip()
# txt28 = str.maketrans('H', 'h')
# txt29 = sample_str.partition(' ')
# txt30 = sample_str.replace('l', 'L')
# txt31 = sample_str.rfind('l')
# txt32 = sample_str.rindex('l')
# txt33 = sample_str.rjust(20, '-')
# txt34 = sample_str.rpartition(' ')
# txt35 = sample_str.rsplit(' ')
# txt36 = "Hello   ".rstrip()
# txt37 = sample_str.split(' ')
# txt38 = "Hello\nWorld".splitlines()
# txt39 = sample_str.startswith('H')
# txt40 = "   Hello   ".strip()
# txt41 = "Hello".swapcase()
# txt42 = sample_str.title()
# txt43 = "Hello".translate({72: 104})
# txt44 = sample_str.upper()
# txt45 = "42".zfill(5)
#
# # Print all outputs
# # for i in range(1, 46):
#     print(f"txt{i}:", locals()[f"txt{i}"])

#f-strings formatting
# price = 59
# txt = f"The price is {price:.3f} dollars"
# print(txt)
#
# price = 59
# tax = 0.25
# txt = f"The price is {price + (price * tax)} dollars"
# print(txt)

# price = 57
# txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
#
# print(txt)
#
# fruit = "apples"
# txt = f"I love {fruit.upper()}"
# print(txt)
#
# def myconverter(x):
#   return x * 0.3048
#
# txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
# print(txt)
#
# price = 59000
# txt = f"The price is {price:,} dollars"
# print(txt)
#
# #Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:
#
# txt = f"The temperature is between {-3: } and {7: } degrees celsius."
#
# print(txt)

# age = 36
# name = "John"
# txt = "His name is {1}. {1} is {0} years old."
# # print(txt.format(age, name))
#
# myorder = "I have a {carname}, it is a {model}."
# print(myorder.format(carname = "Ford", model = "Mustang"))