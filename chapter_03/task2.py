import json

data = {
    'name': 'John',
    'age': 25,
    'city': 'New York',
    'hobby': ['football']
}

result1 = json.dumps(data)

result2 = json.loads(result1)

print(type(result2))
print(result2['hobby'])