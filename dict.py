car = {
    "brand":"toyota",
    "model":"corolla",
    "year":"2020",
    "automatic-trans":True,
    "year":2030,
    "colors":["red","blue","white"]
}
# print (car)
# print(type(car))
# print(len(car))
# print(car.get("model"))

# get all keys
# ky = car.keys();
# print(ky)

# va = car.values();
# print(va)

car ["tinted"]=["factory","grade 0", "grade 1"]
# print(car)
# print(car.items())

if "year" in car:
    car["year"] = 2025
    # print(car)


    # remove from dictionary
# del car
# print (car)

# for x in car:
    # print (x)

# for x in car:
#     if x.startswith("b"):
#         result = x.upper
#         print(result)

for key in car.keys():print(key)

mycopy = car.copy()
# print(mycopy)

user1 ={
    "name":"korede",  "gender":"female"}
user2 ={
    "name":"korry",  "gender":"male"}
user3 ={
    "name":"ade", "gender":"female"}
users ={"first":user1,"second":user2,"third":user3}
print (users)