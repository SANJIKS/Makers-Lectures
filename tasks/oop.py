""" Введение в ООП """

#2
# class Circle:
#     color = 'blue'
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
    
#     def get_area(self):
#         return self.pi * self.radius **2 

# circle = Circle(2)
# circle.color = 'red'
# circle.get_area()

#3
# class BankAccount:
#     balance = 0
#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f'Ваш баланс: {self.balance} сом')
#     def deposit(self, amount):
#         self.balance += amount
#         print(f'Ваш баланс: {self.balance} сом')
    
# account = BankAccount()
# account.deposit(100000)
# account.withdraw(1000)

#4
# class Taxi:
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km

#     def get_total_cost(self, km):
#         res = km * self.cost_km + self.cost
#         return f'Такси {self.name}, стоимость поездки: {res} сом'

# taxi1 = Taxi('Namba', 10, 5)
# taxi2 = Taxi('Yandex', 8, 8)
# taxi3 = Taxi('Jorgo', 15, 4)

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))    

#5
# class Phone:
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone
    
#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')

# contact = Phone('Jhon', 'Snow', +88005553535)
# contact.get_info()

#6
# class Salary:
#     percent = 8
#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience
    
#     def count_percent(self):
#         res = float(self.salary / 100 * self.percent * self.experience)
#         return res

# obj = Salary(10000, 10)
# print(obj.count_percent())

#7
# import datetime

# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner

#     def get_year(self):
#         dt_now = datetime.datetime.now()
#         res = dt_now.year - self.year
#         return f'выиграл {res} лет назад'  




# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())

  
# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())

# 8
# symbols = ['@', '#', '&', '$', '%', '!', '~', '*']
# class Password:
#     def __init__(self, pwr):
#         self.pwr = pwr
    

#     def validate(self):
#         if len(self.pwr) < 8 or len(self.pwr) > 15:
#             raise TypeError("Password should be longer than 8, and less than 15")

#         elif any(i.isdigit() for i in self.pwr) == False:
#             raise TypeError("Password should contain numbers too")

#         elif any(i.isalpha() for i in self.pwr) == False:
#             raise TypeError("Password should contain letters as well") 

#         # elif all(self.pwr.find(i) for i in symbols) != -1:
#         #     raise TypeError('Your password should have some symbols')

        

#         else:
#             return 'Ваш пароль сохранен'

# parol1 = Password('Bebra1824')
# print(parol1.validate())
# parol2 = Password('Bebra13241@')
# print(parol2.validate())


#9
# from functools import reduce
# class Math:
#     def __init__(self, number):
#         self.num = number

#     def get_factorial(self):
#         def summa(x, y):
#             return x * y
            
#         return reduce(summa, [i for i in range(self.num + 1)])

# number = Math(11)
# print(number.get_factorial())












""" Наследование """
#3
# class MyString(str):
#     def __init__(self, first_string):
#         self.first_string = first_string
    
#     def __str__(self) -> str:
#         return self.first_string

#     def append(self, second_str):
#         self.first_string+=second_str

#     def pop(self):
#         res = self.first_string[-1]
#         self.first_string=self.first_string[:-1]
#         return res

        
    
# example = MyString('hello')
# example.append('world')
# a = example.pop()
# print(a)
# print(example)

""" Миксины """
#6



# class CreateMixin:

#     def create(self,key, todo):
#         if key in self.todos:
#             return 'Задача под таким ключом уже существует'
#         else:
#             # self.todos[key] = todo
#             self.todos.update({key:todo})
#             return self.todos

# class DeleteMixin:

#     def delete(self, key):
#         deleted = self.todos.pop(key)
#         return deleted

# class UpdateMixin:

#     def update(self, key, new_value):
#         self.todos.update({key:new_value})
#         # self.todos[key] = new_value
#         return self.todos

# class ReadMixin:

#     def read(self):
#         return sorted(self.todos.items())


# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     # def __init__(self):
#     todos = {}
#     "31/12/2021"
#     ['31','12','2021']
#     def set_deadline(self,deadline_date):
#         from datetime import date
#         # print(type(deadline_date))
#         deadline_date = deadline_date.split('/')
#         deadline = date(int(deadline_date[2]), int(deadline_date[1]), int(deadline_date[0]))
#         today = date.today()
#         res = deadline - today
#         return res.days
# todo = ToDo()
# todo.create('тренеровка', 'день ног')
# print(todo.read())
# todo.update('тренеровка', 'пресс')
# print(todo.read())
# todo.delete('тренеровка')
# print(todo.read())
# print(todo.set_deadline("31/12/2021"))

""" Полиморфизм """
#3
# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
    
#     def get_info():
#         pass

# class Employee(Person):
#     def __init__(self, name, last_name, work, status):
#         Person.__init__(self, name, last_name)
#         self.work = work
#         self.status = status
    

# class Student(Person):
#     def __init__(self, name, last_name, university, course):
#         Person.__init__(self, name, last_name)
#         self.university = university
#         self.course = course

