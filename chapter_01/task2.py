# admin = {"name": "Alex", "age": 23, "allows": [2,4], "bio": "Some info"}

# def printAllows(user):
#     print(user["allows"])

# printAllows(admin)

# class User:
#     name = None
#     email = None
#     login = None
#     age = None

#     def __init__(self, name, email, login='None', age=20):
#         self.set_info(name, email, login, age)
#         self.get_info()

#     def set_info(self, name, email, login, age):
#         self.name = name
#         self.email = email
#         self.login = login
#         self.age = age

#     def get_info(self):
#         print(f'User: {self.name}, login: {self.login}, email: {self.email} age: {self.age}')

# admin = User("Admin", "admin@gmail.com", "Admins", 35)
# bob = User("Bob", "bob@gmail.com")
# alex = User("Alex", "alex@gmail.com", "Alexa", 32)

# bob.set_info("Bob", "bob@gmail.com", "Modest", 26)
# alex.set_info("Alex", "alex@gmail.com", "Alexa", 32)
# admin.set_info("Admin", "admin@gmail.com", "Admins", 35)

# admin.get_info()
# bob.get_info()
# alex.get_info()

class Book:
    
    def __init__(self,title, author, is_available):
        self.set_info(title, author, is_available)

    def check_out(self, is_available=False):
        self.is_available = is_available
    
    def check_in(self, is_available=True):
        self.is_available = is_available

    def set_info(self,title, author, is_available):
        self.title = title
        self.author = author
        self.is_available = is_available

    def __str__(self):
        return f"Book: {self.title}, author: {self.author}, is_available: {self.is_available}"

book = Book('The Great Gatsby', "F.Scott Fitzgerald", is_available=True)

print(book)
book.check_out()
print(book)
book.check_in()
print(book)