name ='king'
# print (name[0])

sentence = """
This is the girl i truly love 
but the religion is standing between
 us oh God
"""
# print (sentence)


# lenght of the string
school = "aptech port harcourt"
# for x in school:
#     print (x)

# print (len(school))

# how to check if port exist

# if "port" in school:
#     print ("please specify, which of the port")
# else:
#     print("port does not exist")   

# slicing/\
message = "this is the place"
# print (message[12:])
# print (message[-5:-2])
# print(message.upper())
# print (message.lower())

msg ="     hello"
# print(len(msg))
# print(len(msg.strip()))

ex ="Uche, Bimbo, Mario"
# print (ex. replace("Bimbo", "Ada"))
newStr = ex.split(",")
# print (type(newStr))
# print (newStr)


# format string
name = "Stephanie"
age = 22
# print(f"My name is {name} and I am {age} years old.")

text = f"the most  handsome guy is {name}"

# print (text)

price = 45
txt2 = f"the current price is {price: .2f} naira"
# print(txt2)

qyt= 6
unit_price = 400
total_sale = f"Total is: {qyt * unit_price}"
# print(total_sale)

user_name = "daniel dog door"
# print(user_name.capitalize())
# print(user_name.count('d', 5, 9))
# print (user_name.endswith("door"))

account_number = "abcd"
# print(account_number.isalnum())

# reverse string

# hello =>olleh

def reverseStr(str):
    return str [::-1]
# print (reverseStr("hello"))    

def ispalidrone(str):
 new_str = str.lower()
 return new_str


# print(ispalidrone("ebuBE"))


name = "james"
# print(len(name)) 

# print (name.upper())
# print(name.lower())

sentence = "programming in class"
# print (sentence[3:7])
# print (sentence.replace("class", "school"))
# print (sentence.replace(" ", ""))

# if"class" in sentence: print("true")

# Write a program that asks for a user’s first name and last name, then prints:
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
total_letters = len(full_name.replace(" ", ""))

print(f"Hello {full_name}! Your name has {total_letters} letters.")
