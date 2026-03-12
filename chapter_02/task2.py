from enum import Enum


# class Choices(Enum):
#     Sweet = 1,
#     Spice = 2,
#     Ice = 3,
#     Hot = 4

# user_choice = Choices.Sweet
# if(user_choice == Choices.Sweet):
#     print('User selected sweets')

# if(user_choice == Choices.Hot):
#     print('User selected hot')


class DayOfWeek(Enum):
    Monday = 1,
    Tuesday = 2,
    Wednesday = 3,
    Thursday = 4,
    Friday = 5,
    Saturday = 6,
    Sunday = 7

for day in DayOfWeek:
    print(day)
