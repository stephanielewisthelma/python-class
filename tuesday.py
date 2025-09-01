# #when an object takes or behave many forms is know as polimophism




# from inheritance import Employee





# class Developer(Employee):
#     def _init_(self, name, salary, language):
#         super()._init_(name, salary)
#         self.language = language

#     def show_details(self):
#         super().show_details()
#         print(f"Language: {self.language}")

#     def calculate_bonus(self):
#         # Example: Developers get 15% bonus
#         return self.salary 


# class Employee:
#     def _init_(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def show_details(self):
#         print(f"Employee Name: {self.name}")
#         print(f"Salary: {self.salary}")

# # Encapsulation is the process of bunding data (variables) and the methods (functions)
# # that operate on that data into a single unit (class), while restricting direct access to the internal 
# # details#



# class BankAccount():
#     def _init_(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance +=amount
    
#     def get__balance(self):
#         return self.__balance
    
# from Manager import Manager
# from developer import Developer
# from Polimophism import Calculator
# from Encapsulation import BankAccount




# emp1 = Manager("Ofega", 5000, 'IT')
# emp2 = Developer('Daniel', 2300, 'HTML')

# emp1.show_details()
# print('')
# print()
# emp2.show_details()


# calc = Calculator()
# print(calc.add(5,8))
# print(calc.add(5,8,3,3))
# print(calc.add(5,8,3,3,8,6))  #In java or C# this method is called Method Overloading


# acc = BankAccount('Price', 4500)
# acc.deposit(4500)
# print(acc.get__balance())
# print(acc.owner)


# from inheritance import  Employee

# class Manager(Employee):
#     def _init_(self, name, salary, department):
#         super()._init_(name, salary)
#         self.department = department

#     def show_details(self):
#         super().show_details()
#         print(f"Department: {self.department}")

#     def calculate_bonus(self):
#         # Example: Managers get 10% bonus
#         return self.salary * 0.10                       