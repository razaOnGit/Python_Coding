#sets repeated value ko ignore kr deta hai
#set is a collection of unordered and unindexed elements
#set is mutable
#set is represented by {}
#set is not ordered
#set is not indexed
#set is not duplicate

s = {2, 4, 2, 6}
print(s)

info = {"Carla", 19, False, 5.9, 19}
print(info)

harry = set()
print(type(harry))

for value in info:
  print(value)

#set is mutable
      # I. union() and update():
      # The union() and update() methods prints all items that are present in the two sets. 
      # The union() method returns a new set whereas update() method adds item into the existing set from another set.

     # Example:
      # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
      # cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
     # cities3 = cities.union(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.update(cities2)
# # print(cities)

#          II. intersection and intersection_update():
#          The intersection() and intersection_update() methods prints only items that are similar to both the sets.
#         The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set. 
#         Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.intersection(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.intersection_update(cities2)
# print(cities)
#          III. difference and difference_update():
#          The difference() and difference_update() methods prints only items that are not similar to both the sets.
#         The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.
#         Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.difference(cities2)
# print(cities3)
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.difference_update(cities2)
# print(cities)
#          IV. symmetric_difference and symmetric_difference_update():
#          The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets.
#         The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.
#         Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.symmetric_difference_update(cities2)
# print(cities)
#          V. issubset():
#          The issubset() method returns True if all items in the set are present in the specified set, otherwise it returns False.
#         Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.issubset(cities2))
#          VI. issuperset():
#          The issuperset() method returns True if all items in the specified set are present in the original set, otherwise it returns False.
#         Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.issuperset(cities2))
#          VII. isdisjoint():
#          The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
#         Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.isdisjoint(cities2))
#          VIII. add():
#          The add() method adds an item to the set.
#         Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.add("London")
# print(cities)
#          IX. remove():
#          The remove() method removes the specified item from the set.
#         Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Madrid")
# print(cities)
#          X. discard():
#          The discard() method removes the specified item from the set.
#         Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.discard("Madrid")
# print(cities)


info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")