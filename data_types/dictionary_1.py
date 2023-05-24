"""
keys()-Returns a list containing the dictionary's keys
items()-Returns a list containing a tuple for each key value pair
values()-Returns a list of all the values in the dictionary
fromkeys()-Returns a dictionary with the specified keys and value

clear()-Removes all the elements from the dictionary
pop()-Removes the element with the specified key
popitem()-Removes the last inserted key-value pair

copy()-Returns a copy of the dictionary

update()-Updates the dictionary with the specified key-value pairs
get()-Returns the value of the specified key
setdefault()-Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
"""

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.keys()
y = car.values()
z = car.items()
a = dict.fromkeys(x,1)
car["color"] = "pink"
# print(x)
# print(y)
# print(z)
print(a)

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(car.pop("model"))
print(car)
print(car.popitem())
print(car)

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.update({"color": "White"})
print(car)

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.get("model","ash")
print(x)

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.setdefault("del","ash")
print(car)