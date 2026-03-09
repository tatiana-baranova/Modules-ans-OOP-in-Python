import math
import time
import platform

import my_module
# from my_module import printSome as ps, summa as s
# import my_module as m

# my_module.printSome(my_module.some)
my_module.printSome(my_module.summa(6, 5, 8, 2))


print(platform.platform())
print(platform.system())
print(platform.release())

time.sleep(3)

res = math.pow(math.pi, 5)
print(round(res))