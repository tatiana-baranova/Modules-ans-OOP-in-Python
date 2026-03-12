import pickle

# user = {'name':'John', 'age': 34, 'weight': 87}
# file = open('user.pickle', "wb")
# pickle.dump(user, file)
# file.close()
file_in = open('user.pickle', "rb")
user_new = pickle.load(file_in)
file_in.close()

print(user_new)
print(user_new['age'])