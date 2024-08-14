"""class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1=Person('Abuzar',20)

print(p1.name)
print(p1.age)"""

"""class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print('Hi',self.name,'how are you doing?')
p1=Person('Abuzar',20)
p1.greet()"""
"""class Car:
    def __init__(self,made,model,year):
        self.made = made
        self.model = model
        self.year = year

    def detail(self):
        print("made in", self.made,
            "\nmodel:",self.model,
                       '\nyear:',self.year) 

car1=Car('china','crolla',2010)  
car1.detail()"""
"""class Circle:
    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        result = self.radius * 3.14
        print(result)

answer=Circle(7)
answer.Area()"""
"""class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def compute_Area(self):
        result = self.length * self.width
        print("The area of rectangle is",result)
    
    def compute_perimeter(self):
        perimeter_result = 2 * (self.length + self.width)
        print("The perimeter of rectangle is",perimeter_result)
R1 = Rectangle(4,2)
R1.compute_Area()
R1.compute_perimeter()"""
"""class Animal:
    def speak(self):
        print("Animals speak")

class Dog(Animal):
    def speak(self):
        print("Dogs bark")

class Cat(Animal):
    def speak(self):
        print("cats meow")
A1 = Animal()
A1.speak()
A2 = Dog()
A3 = Cat()
A3.speak()
A2.speak()"""
"""class Shape:
    def area(self):
        print("The area of the shape")

class Square(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        result = 3.14 * self.radius
        print("The area of the square",result)

class Triangle(Shape):
    def __init__(self,length,base):
        self.length = length
        self.base = base
    def area(self):
        s = 0.5 * self.length * self.base
        print("The area of the triangle",s)
A1 = Square(4)
A1.area()
A2 = Triangle(2,3)
A2.area()"""
"""class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department

employee1 = Manager('Abuzar',"1000$","IT")
print(employee1.department)
print(employee1.salary)"""
"""class Vehicle:
    def drive(self):
        print('Drive carefully')
class Bike(Vehicle):
    def drive(self):
        print('Drive fast')

class Truck(Vehicle):
    def drive(self):
        print("Drive slowly")

c1 = Bike()
c1.drive()
c2 = Truck()
c2.drive()"""
"""class Bird:
    def fly(self):
        print("birds fly")

class Eagle(Bird):
    def fly(self):
        print("eagles fly")

class Penguin(Bird):
    def fly(self):
        print("penguin can not fly")

b1 = Bird()
b1.fly()
b2 = Penguin()
b2.fly()"""
"""class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self,deposit_money):
        self.__balance += deposit_money 
        return self.__balance
    
    def withdraw(self,withdraw_money):
        if self.__balance >= withdraw_money:
            self.__balance -= withdraw_money
        else:
            print("You can not withdraw such an amount.Your balance is inadequate")
    def check_balance(self):
        return self.__balance 
                
A1 = Account()
A1.deposit(1000)
A1.withdraw(600)
print(A1.check_balance())"""
"""class Book:
    def __init__(self,title,author,pages):
        self.__title = title
        self.__author = author
        self.__pages = pages

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_pages(self):
        return self.__pages
    
    def set_title(self,title):
        self.__title = title
    
    def set_author(self,author):
        self.__author = author
    
    def set_pages(self,pages):
        self.__pages = pages

b1 = Book('humanity','Abuzar',1200)
print(b1.get_author())
b1.set_title("computer science in Quran")
b1.set_author("Ali")
print(b1.get_author())"""
"""class Laptop:
    def __init__(self,brand,model,price):
        self.__brand = brand
        self.__model = model
        self.__price = price
    def details(self):
        print("The brand is",self.__brand)
        print("The model is",self.__model)
        print("The price is",self.__price)
    
    def discount(self,percentage):
        if 0<= percentage <= 100:
            self.__price = self.__price - (percentage * self.__price / 100)
        return f"The price after discount is {self.__price}"
    
L1 = Laptop('Dell',"Acer swift X 14",500)
L1.details()
print(L1.discount(10))"""

"""class Bank_Account:
    def __init__(self,account_number):
        self.__account_number = account_number
        self.__balance = 0

    def deposit(self,deposit_money):
        self.__balance += deposit_money
    
    def withdraw(self,withdrawal):
        if withdrawal <= self.__balance:
            self.__balance -= withdrawal
        else:
            print("Your balance is not enough to withdraw such amount of money")
    
    def check_balance(self):
        return self.__balance


B_A = Bank_Account (12345)
B_A.deposit(10000)
print("Before withdrawl your balance is",B_A.check_balance())
B_A.withdraw(500)
print("After withdrawl your balance is",B_A.check_balance())"""
"""class Student:
    def __init__(self,name,grade,age):
        self.__name = name
        self.__grade = grade
        self.__age = age
    
    def get_name(self):
        return self.__name
        
    def get_grade(self):
        return self.__grade
    
    def get_age(self):
        return self.__age

    def set_name(self,name):
        self.__name = name
        
    def set_grade(self,grade):
        self.__grade = grade
    
    def set_age(self,age):
        self.__age = age

    def display_detail(self):
        print("Name:",self.__name)
        print("Grade:",self.__grade)
        print("Age:",self.__age)

s1 = Student('Abuzar', 1,20)
print(s1.get_name())
s1.set_name("Ali")        
s1.display_detail()"""

"""class Library:
    def __init__(self,name):
        self.name = name
        self.list_of_books = []

    def Add_books(self):
        while True:
            a = input("Enter a name of book to add(or press enter to finish):")
            if a == "":
                break
            self.list_of_books.append(a)
            print("The book is added")
            
    def Remove_books(self):
        try:
            while True:
                r = input("enter a name of book to remove(or press to enter finish):")
                if r == "":
                    break
                self.list_of_books.remove(r)
                print("The book is removed")
        except:
            print(f"The book {r} is not in the list")

    def show_list():
        return f"Library{self.name}, Books {self.list_of_books}"
            

L = Library("Mother")
L.Add_books()
print(L.list_of_books)
L.Remove_books()
print(L.list_of_books)"""

"""class School:
    def __init__(self,name):
        self.name = name
        self.list_of_students = []
    
    def Add_student(self):
        while True:
            i = input("Enter a name of student to add(or press enter to finish):")
            if i == '':
                break
            self.list_of_students.append(i)
            print("The student is added")
    
    def Remove_student(self):
        try:
            while True:
                j = input("Enter a name of student to remove(or press enter to finish):")
                if j == '':
                    break
                self.list_of_students.remove(j)
                print("The student is removed")
        except:
            print(f"The student {j} is not in the list")

s1 = School("Yektaparastan")
s1.Add_student()
print(s1.list_of_students)
s1.Remove_student()
print(s1.list_of_students)"""

"""class Team:
    def __init__(self,name):
        self.name = name
        self.list_of_members = []

    def Add_member(self):
        while True:
            t = input("Enter a name of person to add(or press enter to finish):")
            if t == '':
                break
            self.list_of_members.append(t)
            print("The person is added")
        
    def Remove_member(self):
        try:
            while True:
                r = input("Enter name of person to remove(or press enter to finish):")
                if r == '':
                    break
                self.list_of_members.remove(r)
                print("The person is removed")
        except:
            print(f"The person {r} is not in the list")
T = Team("Real Madrid")
T.Add_member()
print(T.list_of_members)
T.Remove_member()
print(T.list_of_members)"""

"""class Company:
    def __init__(self,name):
        self.name = name
        self.list_of_employees = []
    
    def Add_employee(self):
        while True:
            e = input("Enter name of employee to add(or press enter to finish):")
            if e == '':
                break
            self.list_of_employees.append(e)
            print("The employee is added" )
    
    def Remove_employee(self):
        try:
            while True:
                r = input("Enter name of employee to remove(or press enter to finish):")
                if r == '':
                    break
                self.list_of_employees.remove(r)
                print("The employee is removed ")
        except:
            print(f"The employee {r} is not in list")

C = Company("Yektaparast")
C.Add_employee()
print(C.list_of_employees)
C.Remove_employee()
print(C.list_of_employees)"""
"""class Zoo:
    def __init__(self,name):
        self.name = name 
        self.Animals_of_zoo = []
    
    def Add_animal(self):
        while True:
            z = input("Enter name of animal to add(press enter to finish):")
            if z == '':
                break
            self.Animals_of_zoo.append(z)
            print("The animal is added")
    
    def Remove_animal(self):
        try:
            while True:
                r = input("Enter name of animal to remove(or press enter to finish):")
                if r == '':
                    break
                self.Animals_of_zoo.remove(r)
                print("The animal is removed")
        except:
            print(f"The animal {r} is not in the list")
Z = Zoo("Zoo of Kabul")
Z.Add_animal()
print(Z.Animals_of_zoo)
Z.Remove_animal()
print(Z.Animals_of_zoo)"""
"""class FileManager:
    def __init__(self):
        self.my_file = open("my_file1.txt",'r+')

    def write_file(self,write):  
        i = input("write something here: ")
        self.my_file.write(i +'\n')

    def read_file(self):
        self.my_file.seek(0)
        r = self.my_file.read()
        return  r
   
i = FileManager()
print(i.read_file())
i.write_file(i)"""


"""from datetime import datetime
class Log:
    def __init__(self, filename='error1_log.txt'):       
        self.filename = filename

    def write_error(self, message):
        #Write an error message to the log file with a timestamp.#In the context of the log class
                                                                      #example, a timestamp is included to 
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')      #indicate exactly when each error
        with open(self.filename, 'a') as f:                           #message was logged
            f.write(f"{timestamp} - ERROR: {message}\n")


logger = Log()
logger.write_error("This is an error message.")
logger.write_error("Another error occurred.")"""

"""________W________import json
class Config:
    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.settings = json.load(file)

    def get(self, key, default=None):
        #Get a setting by key, or return default if not found.
        return self.settings.get(key, default)


config = Config('config.json')
some_value = config.get('some_key', 'default_value')
print(f"Value for 'some_key': {some_value}")"""

"""import sqlite3
class SimpleDatabase:
    def __init__(self, db_name):
        #Initialize the database connection.
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def execute(self, query, params=None):
        #Execute a query (INSERT, UPDATE, DELETE).
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()

    def fetch_all(self, query, params=None):
        #Fetch all results from a SELECT query.
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        #Close the database connection.
        self.connection.close()

# Example usage
if __name__ == "__main__":
    db = SimpleDatabase('example.db')
    
    # Create a table
    db.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')

    # Insert a user
    db.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))

    # Fetch all users
    users = db.fetch_all('SELECT * FROM users')
    print(users)

    # Close the connection
    db.close()"""
"""class Report:
    def __init__(self, file_path):
        #Initialize the Report with the file path.
        self.file_path = file_path

    def read_file(self):
    #Read data from the file and return it.
        try:
            with open(self.file_path, 'r+') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' does not exist.")
            return []
        except IOError:
            print("Error: Could not read the file.")
            return []

    def generate_report(self):
        #Generate and print a report from the data.
        data = self.read_file()
        if data:
            print("Report Generated:")
            print("".join(data))
        else:
            print("No data available to generate the report.")

# Example usage
if __name__ == "__main__":
    report = Report('data.txt')
    report.generate_report()"""
    


"""class Ticket:
    def __init__(self,movie_name,seat_number,price):
        self.movie_name = movie_name
        self.seat_number = seat_number
        self.price = price
    
    def display_detail(self):
        print("The name of movie:",self.movie_name)
        print("seat_number:",self.seat_number)
        print("The price of ticket:",self.price,'$')
    
    def apply_discount(self,percentage_of_discount):
        self.price -= (self.price * percentage_of_discount / 100)
        return f"price of ticket after discount {self.price} $"

T1 = Ticket('on the way of love',120,15.0)
T1.display_detail()
print(T1.apply_discount(10))"""
"""class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
class ShoppingCart:
    def __init__(self):
        self.lst_of_item = []
    def add_item(self,item):
        if isinstance(item,Item):
            self.lst_of_item.append(item)
        else:
            print("Invalid item.please provide an instance of the item class")
        
    def remove_item(self,item_name):
        for i in self.lst_of_item:
            if i.name == item_name:
                self.lst_of_item.remove(i)
                print(f"Removed {item_name} from the cart")
                return
        print(f"{item_name} not found in the cart")
    
    def display_item(self):
        for item in self.lst_of_item:
            print(f"{item.name} : {item.price} $")


cart = ShoppingCart()
cart.add_item(Item("salt",25))
cart.add_item(Item('meat',500))
cart.display_item()
cart.remove_item('meat')
cart.display_item()"""

"""class Restaurant:
    def __init__(self,name):
        self.name = name
        self.menu = []

    def add_to_menu(self):
        while True:
            a = input("Name of food or drink to add to the menu(or press enter to finish):")
            if a == '':
                break
            self.menu.append(a)
            print("item is added")
    
    def remove_from_menu(self):
        try:
            while True:
                r = input("name of food or drink to remove from menu(or press enter to finish):")
                if r == '':
                    break
                self.menu.remove(r)
                print("item is removed")
        except:
            print(f"{r} is not in the menu")
R1 = Restaurant("Mother's Restaurant")
R1.add_to_menu()
print(R1.menu)
R1.remove_from_menu()
print(R1.menu)"""
"""class Flight:
    def __init__(self,flight_number,destination):
        self.flight_number = flight_number
        self.destination = destination
        self.passengers = []

    def add_passenger(self):
        while True:
            p = input("Enter name of a passenger here to add:")
            if p == '':
                break
            self.passengers.append(p)
            print(f"Passenger {p} has been added")
    def remove_passenger(self):
        try:
            while True:
                r = input("Enter a name of passenger here to remove :")
                if r == '':
                    break
                self.passengers.remove(r)
                print("The passenger is removed")
        except:
            print(f"{r} is not in the list")
F1 = Flight('Ariana',"London")
F1.add_passenger()
print(F1.passengers)
F1.remove_passenger()
print(F1.passengers)"""
"""class Room:
    def __init__(self,room_number,is_occupied = False):
        self.room_number = room_number
        self.is_occupied = is_occupied
    
    def __str__(self):
        status = "Occupied"  if self.is_occupied else "Available"
        return f"Room{self.room_number}:{status}"
        
class Hotel:
    def __init__(self,name):
        self.name = name
        self.lst_of_rooms = []
        
    def add_room(self,room):
        if isinstance(room,Room):
            self.lst_of_rooms.append(room)
            print(f"Room {room.room_number} added to Hotel")
    def book_room(self,room_number):
        for room in self.lst_of_rooms:
            if room.room_number == room_number:
                print(f"Room {room_number} has been booked")

    def checkout_room(self,room_number):
        for room in self.lst_of_rooms:
            if room.room_number == room_number:
                print(f"Room {room_number} has been checked out")
        
    def display_rooms(self):
        print(f"Rooms in {self.name} :")
        for room in self.lst_of_rooms:
            print(room)
hotel = Hotel("Abuzar Plaza")
hotel.add_room(Room(202))
hotel.add_room(Room(301))
hotel.add_room(Room(107))

hotel.display_rooms()
hotel.book_room(301)
hotel.book_room(107)
hotel.checkout_room(107)"""
# _________GUI application__________________________________________________________________________
"""import tkinter as tk

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Counter")

        self.counter = 0
        self.label = tk.Label(root, text=str(self.counter), fg="dark green") 
        self.label.pack()

        self.create_buttons()

    def create_buttons(self):
        increment_button = tk.Button(self.root, text="Increment", command=self.increment)
        decrement_button = tk.Button(self.root, text="Decrement", command=self.decrement)

        increment_button.pack()
        decrement_button.pack()

    def increment(self):
        self.counter += 1
        self.update_label()

    def decrement(self):
        self.counter -= 1
        self.update_label()

    def update_label(self):
        self.label.config(text=str(self.counter))

root = tk.Tk()
app = CounterApp(root)
root.mainloop()"""

"""import tkinter as tk

class CounterApp:
    def __init__(self, root):  # Corrected constructor name
        self.root = root
        self.root.title("Counter")

        self.counter = 0
        self.label = tk.Label(root, text=str(self.counter), fg="dark green")  # Initialize with counter value
        self.label.pack()

        self.create_buttons()

    def create_buttons(self):
        increment_button = tk.Button(self.root, text="Increment", command=self.increment)
        decrement_button = tk.Button(self.root, text="Decrement", command=self.decrement)

        increment_button.pack()
        decrement_button.pack()

    def increment(self):
        self.counter += 1
        self.update_label()

    def decrement(self):
        self.counter -= 1
        self.update_label()

    def update_label(self):
        self.label.config(text=str(self.counter))

if __name__ == "__main__":  # Corrected name check
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()"""
    
    
    
    
    
    
"""import tkinter as tk

class ToDoApp:
    def __init__(self, root):  # Corrected constructor name
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []  # List to store tasks

        # Create widgets
        self.task_entry = tk.Entry(root)
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.task_listbox = tk.Listbox(root)
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)

        # Pack widgets
        self.task_entry.pack()
        self.add_button.pack()
        self.task_listbox.pack()
        self.remove_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)  # Clear the entry after adding

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":  # Corrected name check
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()"""
    
    
    
    
    
    
    
    
    
"""import tkinter as tk

class CalculatorApp:
    def __init__(self, root):  # Corrected constructor name
        self.root = root
        self.root.title("Calculator")

        self.expression = ""  # Stores the user input expression

        # Create widgets
        self.entry_field = tk.Entry(root)
        self.entry_field.grid(row=0, column=0, columnspan=4)

        # Create buttons for digits and operators
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        for i, button_text in enumerate(buttons):
            row, col = divmod(i, 4)
            button = tk.Button(root, text=button_text, command=lambda text=button_text: self.on_button_click(text))
            button.grid(row=row + 1, column=col)

    def on_button_click(self, text):
        if text == '=':
            try:
                result = str(eval(self.expression))
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(0, result)
                self.expression = result  # Update expression with result
            except Exception as e:
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(0, "Error")
                self.expression = ""  # Clear expression on error
        else:
            self.expression += text
            self.entry_field.insert(tk.END, text)

if __name__ == "__main__":  # Corrected name check
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()"""
    
    
    
    
    
    
    
    
    
    
    
    
"""import tkinter as tk

class LoginApp:
    def __init__(self, root):
        self\.root = root
        self\.root\.title("Login Form")

        # Create widgets
        self\.username_label = tk\.Label(root, text="Username")
        self\.username_entry = tk\.Entry(root)

        self\.password_label = tk\.Label(root, text="Password")
        self\.password_entry = tk\.Entry(root, show="*")  # Hide password characters

        self\.login_button = tk\.Button(root, text="Login", command=self\.validate_credentials)

        # Grid layout
        self\.username_label\.grid(row=0, column=0)
        self\.username_entry\.grid(row=0, column=1)

        self\.password_label\.grid(row=1, column=0)
        self\.password_entry\.grid(row=1, column=1)

        self\.login_button\.grid(row=2, columnspan=2)

    def validate_credentials(self):
        username = self\.username_entry\.get()
        password = self\.password_entry\.get()

        # Add your validation logic here (e\.g\., check against a database)
        if username == "admin" and password == "secret":
            print("Login successful\!")
        else:
            print("Invalid credentials\. Please try again\.")

if __name__ == "__main__":
    root = tk\.Tk()
    app = LoginApp(root)
    root\.mainloop()
    
    
    
    
    
    
    
    
    
    
import tkinter as tk
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        # Create widgets
        self.city_label = tk.Label(root, text="Enter City:")
        self.city_entry = tk.Entry(root)

        self.weather_label = tk.Label(root, text="")
        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.show_weather)

        # Grid layout
        self.city_label.grid(row=0, column=0)
        self.city_entry.grid(row=0, column=1)
        self.get_weather_button.grid(row=1, columnspan=2)
        self.weather_label.grid(row=2, columnspan=2)

    def show_weather(self):
        city_name = self.city_entry.get()
        api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

        try:
            response = requests.get(weather_url)
            weather_data = response.json()

            if weather_data.get("cod") == 200:
                temperature = weather_data["main"]["temp"]
                description = weather_data["weather"][0]["description"]
                self.weather_label.config(text=f"Temperature: {temperature:.1f}°C\nDescription: {description}")
            else:
                self.weather_label.config(text="City not found. Please check the spelling.")

        except Exception as e:
            self.weather_label.config(text="An error occurred while fetching the weather data.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()"""


