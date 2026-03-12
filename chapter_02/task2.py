from enum import Enum


class Choices(Enum):
    Sweet = 1,
    Spice = 2,
    Ice = 3,
    Hot = 4

user_choice = Choices.Sweet
if(user_choice == Choices.Sweet):
    print('User selected sweets')

if(user_choice == Choices.Hot):
    print('User selected hot')
