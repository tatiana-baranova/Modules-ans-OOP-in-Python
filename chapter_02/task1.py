# # Магічні (dunder) методи Python

# __abs__() — повертає абсолютне значення числа (abs(obj))
# __add__() — операція додавання (+)
# __and__() — бітова операція AND (&)
# __bool__() — перетворення об'єкта у True або False
# __ceil__() — округлення числа вгору
# __class__ — повертає клас об'єкта
# __delattr__() — видалення атрибуту (del obj.attr)
# __dir__() — список атрибутів і методів об'єкта
# __divmod__() — результат функції divmod(a, b)
# __doc__ — документація об'єкта
# __eq__() — перевірка рівності (==)
# __float__() — перетворення об'єкта у float
# __floor__() — округлення вниз
# __floordiv__() — цілочисельне ділення (//)
# __format__() — форматування рядків format()
# __ge__() — більше або дорівнює (>=)
# __getattribute__() — доступ до атрибутів об'єкта
# __getnewargs__() — використовується при серіалізації (pickle)
# __getstate__() — отримання стану об'єкта
# __gt__() — більше ніж (>)
# __hash__() — хеш-значення об'єкта
# __index__() — дозволяє використовувати об'єкт як індекс
# __init__() — конструктор класу
# __init_subclass__() — викликається при створенні підкласу
# __int__() — перетворення об'єкта у int
# __invert__() — бітове NOT (~)
# __le__() — менше або дорівнює (<=)
# __lshift__() — зсув бітів вліво (<<)
# __lt__() — менше ніж (<)
# __mod__() — залишок від ділення (%)
# __mul__() — множення (*)
# __ne__() — не дорівнює (!=)
# __neg__() — унарний мінус (-obj)
# __new__() — створення нового об'єкта
# __or__() — бітова операція OR (|)
# __pos__() — унарний плюс (+obj)
# __pow__() — піднесення до степеня (**)
# __radd__() — додавання (коли об'єкт справа)
# __rand__() — бітове AND справа
# __rdivmod__() — divmod для правого операнда
# __reduce__() — використовується для pickle
# __reduce_ex__() — розширена версія reduce
# __repr__() — офіційне текстове представлення об'єкта
# __rfloordiv__() — цілочисельне ділення справа
# __rlshift__() — бітовий зсув вліво справа
# __rmod__() — залишок від ділення справа
# __rmul__() — множення справа
# __ror__() — бітове OR справа
# __round__() — округлення round()
# __rpow__() — піднесення до степеня справа
# __rrshift__() — бітовий зсув вправо справа
# __rshift__() — бітовий зсув вправо (>>)
# __rsub__() — віднімання справа
# __rtruediv__() — ділення справа
# __rxor__() — бітове XOR справа
# __setattr__() — встановлення значення атрибуту
# __sizeof__() — розмір об'єкта в пам'яті
# __str__() — читабельне текстове представлення об'єкта
# __sub__() — віднімання (-)
# __subclasshook__() — перевірка підкласів
# __truediv__() — звичайне ділення (/)
# __trunc__() — обрізання дробової частини
# __xor__() — бітове XOR (^)

# Методи чисел

# as_integer_ratio() — представляє число як дріб (чисельник/знаменник)
# bit_count() — кількість одиничних бітів у числі
# bit_length() — довжина числа в бітах
# conjugate() — спряжене число (для комплексних)
# denominator — знаменник дробу
# from_bytes() — створення числа з байтів
# imag — уявна частина комплексного числа
# numerator — чисельник дробу
# real — дійсна частина числа
# to_bytes() — перетворення числа у байти

# Найважливіші магічні методи Python

# __init__(self, ...) 
# Конструктор класу. Викликається при створенні об'єкта.

# __str__(self)
# Повертає "красивий" рядок для користувача. Викликається print(obj).

# __repr__(self)
# Технічне представлення об'єкта для розробника.

# __len__(self)
# Дозволяє використовувати len(obj).

# __eq__(self, other)
# Перевірка рівності об'єктів (==).

# __lt__(self, other)
# Менше (<).

# __le__(self, other)
# Менше або дорівнює (<=).

# __gt__(self, other)
# Більше (>).

# __ge__(self, other)
# Більше або дорівнює (>=).

# __add__(self, other)
# Додавання об'єктів (+).

# __sub__(self, other)
# Віднімання (-).

# __mul__(self, other)
# Множення (*).

# __truediv__(self, other)
# Ділення (/).

# __getitem__(self, key)
# Доступ до елементів obj[key].

# __setitem__(self, key, value)
# Встановлення значення obj[key] = value.

# __contains__(self, item)
# Оператор in (item in obj).

# __call__(self, ...)
# Дозволяє викликати об'єкт як функцію obj().

# __iter__(self)
# Робить об'єкт ітерабельним (для for).

# __next__(self)
# Повертає наступний елемент при ітерації.

# print(dir(int))

class Some:
    name = "John"
    number = 20
    def __add__(self, str):
        print('Some ' + str)
    # def __new__(self):
    #     self.__add__(self, 'new')
    #     self.__init__(self)
    def __init__(self):
        print('Init started')

    def __str__(self):
        return "Name: " + self.name
    def __ge__(self, x):
        if(self.number >= x):
            return True
        else:
            return False
        
    def __lt__(self, x):
        if(self.number < x):
            return True
        else:
            return False
    def __gt__(self, x):
        if(self.number > x):
            return True
        else:
            return False
        
    def __eq__(self, x):
        if(self.number == x):
            return True
        else:
            return False
    def __ne__(self, x):
        if(self.number != x):
            return True
        else:
            return False
        
    def __le__(self, x):
        if(self.number <= x):
            return True
        else:
            return False
        

    def __del__(self):
        print("Delete object")


# obj = Some()
# obj + "new"
# print(obj != 50)
# print(dir(obj))


# Самостійна робота

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, x):
        new_width = self.width + x.width
        new_height = self.height + x.height
        return Rectangle(new_width, new_height)
        
    def __str__(self):
        return f"{self.width} x {self.height}"

obj1 = Rectangle(8, 2)
obj2 = Rectangle(10, 6)

result_rect = obj1 + obj2 
print(f'Result: {result_rect}')