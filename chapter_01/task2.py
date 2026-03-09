# admin = {"name": "Alex", "age": 23, "allows": [2,4], "bio": "Some info"}

# def printAllows(user):
#     print(user["allows"])

# printAllows(admin)

class User:
    name = None
    email = None
    login = None
    age = None

    def __init__(self, name, email, login='None', age=20):
        self.set_info(name, email, login, age)
        self.get_info()

    def set_info(self, name, email, login, age):
        self.name = name
        self.email = email
        self.login = login
        self.age = age

    def get_info(self):
        print(f'User: {self.name}, login: {self.login}, email: {self.email} age: {self.age}')

admin = User("Admin", "admin@gmail.com", "Admins", 35)
bob = User("Bob", "bob@gmail.com")
alex = User("Alex", "alex@gmail.com", "Alexa", 32)

# bob.set_info("Bob", "bob@gmail.com", "Modest", 26)
# alex.set_info("Alex", "alex@gmail.com", "Alexa", 32)
# admin.set_info("Admin", "admin@gmail.com", "Admins", 35)

# admin.get_info()
# bob.get_info()
# alex.get_info()