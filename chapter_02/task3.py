import time
import threading

# def sleepTime(wait, name):
#     print("Enter text: {}".format(name))
#     time.sleep(wait)
#     print("Enter text repeatedly: {}".format(name))

# start = time.time()
# t_list = []
# for i in range(5):
#     name = 'SleepTime ' + str(i + 1)
#     print('{} start'.format(name) )
#     td = threading.Thread(target=sleepTime, name=name, args=(3, name))
#     td.start()
#     t_list.append(td)

# for t in t_list:
#     t.join()

# end = time.time()

# print("Time: ", end - start)

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)
    


thread = threading.Thread(target=print_numbers)

thread.start()
thread.join()

print('Головний потік завершив роботу')