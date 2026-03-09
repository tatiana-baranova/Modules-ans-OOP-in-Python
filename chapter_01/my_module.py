if __name__ == 'main.py':
    print("Hello my friend, how are you?")

some = 15

def printSome(word):
    print(f'Результат: {word}')

def summa(*args):
    sum = 0
    for i in args:
        sum += i

    return sum