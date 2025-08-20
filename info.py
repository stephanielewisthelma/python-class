class info():
    greet ="how are you?"
    
    
    
    
# print (info)

info1 =info()

# print (info1.greet)

class Person():
    def __init__(self,firstname, lastname):
        self.firstname = firstname
        self.lastname =lastname

p1 = Person("Ade" ,"Zion ")
p2 = Person("lewis", "steph")

# print(p1.firstname)
# print (p1.lastname)
print (p2.firstname)

# print (p1)


class Laptop():
    def __init__(self,laptopType, color, ram, serialNumber, year):
        self.laptopType = laptopType
        self.color =color
        self.ram =ram

l1 = Laptop("dell" ,"blue" , "16gb", "SN-LPT-9X3H2K47","2010")
l2 = Laptop("HP", "ash", "64gb", "SN-HPQ-7M2D8P11","2019")
l3 = Laptop("Acer", "red", "32gb" ,"SN-DELL-5A9R4T62", "2020")
l4 = Laptop("macbook", "ash", "12gb" ,"SN-LEN-3W8Q7C90","2005")
l5 = Laptop("asus", "black", "8gb", "SN-ASU-6B1K5F84","")


print(l1.laptopType)
print(l1.color)
print(l1.ram)


print(l2.laptopType)
print(l2.color)
print(l2.ram)


print(l3.laptopType)
print(l3.color)
print(l3.ram)


print(l4.laptopType)
print(l4.color)
print(l4.ram)


print(l5.laptopType)
print(l5.color)
print(l5.ram)