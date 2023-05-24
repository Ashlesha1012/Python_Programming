"""
index()-Returns the index of the first element with the specified value
count()-Returns the number of elements with the specified value

append()-Adds an element at the end of the list
insert()-Adds an element at the specified position
extend()-Add the elements of a list (or any iterable), to the end of the current list

clear()-Removes all the elements from the list
remove()-Removes the first item with the specified value
pop()-Removes the element at the specified position

copy()-Returns a copy of the list
reverse()-Reverses the order of the list
sort()-Sorts the list

"""

makeup = [1, 2, 4, (1, 2), 7, 7]
x = makeup.index(7)
print(x)

students = ["a", "b", "c", "d", "a"]
print(students.count("a"))

animals = ["cat", 'dog']
animals.append(("cow", "hen"))
print(animals)

country = ["India", "Australia"]
country.insert(0, "USA")
print(country)

vegetables = ["onion", "chillies"]
vegetables.extend((1, 2, 3))
print(vegetables)

city = ["mumbai", "nagpur"]
city.clear()
print(city)

city = ["mumbai", "nagpur"]
city.remove("nagpur")
print(city)

city = ["mumbai", "nagpur"]
x = city.pop()
print(x, city)

vegetables = ["onion", "chillies"]
x = vegetables.copy()
print(x, id(vegetables), id(x))

vegetables = ["onion", "chillies"]
vegetables.reverse()
print(vegetables)

makeup = [1, 10, 55, 2, 4, 7, 7]
makeup.sort(reverse=True)
print(makeup)