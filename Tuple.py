#  creating tuples
tuple1 = (1, 2, 3)
tuple2 = 'a','b','c'
tuple3 = tuple([4, 5, 6])
print(tuple1,tuple2,tuple3)

# implementation of accessing element in a tuple
my_tuple = (10, 20, 30, 40)
print(my_tuple[0])
print(my_tuple[2])
# slicing a tuple
my_tuple = (1, 2, 3, 4, 5, 6)
print(my_tuple[1:4])
print(my_tuple[::2])
# immutability in tuple
my_tuple = (1, 2, 3)
print("tuplea are immutable")
# concatenating tuples 
tuple1 = (3,5)
tuple2 = (4,6)
result = tuple1 + tuple2
print(result)
# repeating a tuple
my_tuple = (1, 2)
repeated = my_tuple * 3
print(repeated)
# length of a tuple
my_tuple = (10, 20, 30)
print(len(my_tuple))
# checking membership in a tuples
my_tuple = (2,3, 6)
print(2 in my_tuple)
print(5 in my_tuple)
# iterating over a tuple
my_tuple = (8, 9, 10)
for item in my_tuple:
    print(item)
# index of a element
my_tuple = (10, 20, 30)
print(my_tuple.index(20))
# counting element
my_tuple = (1, 4, 6, 3, 3, 5)
print(my_tuple.count(3))
# nested_tuple
nested_tuple = (1, (2, 3), (4, (5, 6)))
print(nested_tuple[1])
print(nested_tuple[2][1])
# unpacking tuple
my_tuple = (1, 2, 3)
a, b, c=my_tuple
print(a, b, c)
# dictionary kays
coordinates = {(1, 2): "point A",(3, 4): "point B"}
print(coordinates[(1, 2)])
# tuple with list
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]
my_list [0] = 10
print(my_list)
# returning multiple values from a funtion
def  get_coordination ():
    return (10, 20)
x, y =get_coordination()
print(x, y)
# sorting a list tuple
tuple_list = [(3, 'C') ,(1, 'A'),(2, 'B')]
sorted_list = sorted(tuple_list)
print(sorted_list)
# hashability in tuple
my_tuple = (1, 2, 3)
print(hash(my_tuple))
# packing  and unpacking funtion
def pack (* arg):
    return arg
packed = pack(1, 2, 3)
print(packed)
# conversion between lists and tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
converted_list = list(my_tuple)
print(my_tuple, converted_list)
