"""
add()-Adds an element to the set
update()-Update the set with another set, or any other iterable

copy()-Returns a copy of the set

clear()-Removes all the elements from the set
discard()-Remove the specified item
pop()-Removes an element from the set
remove()-Removes the specified element   remove() method will raise an error if the specified item does not exist, and the discard() method will not.

union()-Return a set containing the union of sets
intersection()-Returns a set, that is the intersection of two or more sets
intersection_update()-Removes the items in this set that are not present in other, specified set(s)
difference()-Returns a set containing the difference between two or more sets
difference_update()-Removes the items in this set that are also included in another, specified set
symmetric_differnce()-Returns a set with the symmetric differences of two sets
symmetric_differnce()_update()-inserts the symmetric differences from this set and another


isdisjoint()-Returns whether two sets have a intersection or not
issubset()-Returns whether another set contains this set or not
issuperset()-Returns whether this set contains another set or not


"""
s1 = {1, 2, 3, 6}
s1.add(19)
print(s1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y, (1, 2, (4, 6)))
print(x, y)

y = {"google", "microsoft", "apple"}
y.discard("a")         #no error
print(y) 

x = {'microsoft', 1, 'banana', 'cherry', 2, 'apple', (4, 6), 'google'} 
# x.remove("a")    #KeyError: 'a'
print(x)

x = {'microsoft', 1, 'banana', 'cherry', 2, 'apple', (4, 6), 'google'} 
p = x.pop()
print(p, x)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
u = x.union(y, {1, 2, 44})
print(u)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
i = x.intersection(y)
print(i)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
y.intersection_update(x)
print(y)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
d = x.difference(y)
print(d)
x.difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(x.symmetric_difference(y))
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft"}
print(x.isdisjoint(y))

x = {"apple", "banana", "cherry"}
y = {"apple"}
print(y.issubset(x))

x = {"apple", "banana", "cherry"}
y = {"apple"}
print(x.issuperset(y))
