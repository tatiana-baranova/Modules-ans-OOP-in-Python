import time
import threading

def sleepTime(wait, name):
    print("Enter text: {}".format(name))
    time.sleep(wait)
    print("Enter text repeatedly: {}".format(name))


# td.start()
# td.join()
start = time.time()
t_list = []
for i in range(5):
    name = 'SleepTime ' + str(i + 1)
    print('{} start'.format(name) )
    td = threading.Thread(target=sleepTime, name=name, args=(3, name))
    td.start()
    t_list.append(td)

for t in t_list:
    t.join()

# for e in range(5):
#     sleepTime(3, e)

end = time.time()

print("Time: ", end - start)