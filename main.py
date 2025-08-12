# print("hello")
# a = 6
# print(a + 3)
# # logical operators
# print(2!=1)

# def add(a,b):
#     return a + b

# def subtract(a,b):
#     return a - b

# print(add(2,3))
# print(subtract(5,2))

def userAge(age):
    if age < 12:
        return "age of consent slightly missed but we'll consider you😉"
    return "congratulations, you're qualified to be groomed🙂"

print(userAge(12))

def trafficLaws(speed, birthday):
    fine = ""
    if speed <= 60 :
        fine = "not fine"
    elif speed >60 and speed <= 80 and birthday == False:
        fine = "small fine"
    elif speed > 80 and birthday:
        fine = "small fine"    
    else:
        print("big fine")
    return fine



shii = trafficLaws(85, False)
print(shii)