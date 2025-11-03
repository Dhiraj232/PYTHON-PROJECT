# set is a unorder item and unique and mutable but set element is immutable.
# set not a count in a duplicate value
# unhausable= mutable
# hausable= immutable

collection = {1,2,2,3,3,4,"hello","world"}
print(collection)
print(len(collection))
print(collection.pop())

# {} is a empty dictionary
# () is a empty set

collection=set()
print(type(collection))
collection.add(2)
collection.add("hello")
collection.remove(2)
print(collection)


set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1)
