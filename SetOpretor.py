#  creating sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("set A:", set_a)
print("set B:", set_b)
# adding and removing
set_a.add(6)
set_a.remove(1)
print("set a after adding 6 and removing 1:", set_a)
print("set A:", set_a)
print("srt B:", set_b)
# union of set
union_set = set_a.union(set_b)
print("union of a and set b:", union_set)
# Intersection of set
intersection_set =set_a.intersection(set_b)
print("Inteersection of set a and b:", intersection_set)
# difference of set
difference_set = set_a.difference(set_b)
print("difference of  set a and b (a - b):", difference_set)
# symmetric diffrence of sets
sym_diff_set = set_a.symmetric_difference(set_b)
print("symmetric difference of set a and set b:", sym_diff_set)
# subset and superset testing
set_c = {4, 5}
is_subset = set_c.issubset(set_a)
is_superset = set_a.issuperset(set_c)
print(f"Is set C a subset of set A?{is_subset}")
print(f"Is set A a superset of C?{is_superset}")
# membership testing
is_member = 3 in set_a
print("Is 3 in set A?", is_member)
# removing duplicates sets
number_list = [1, 2, 3, 4, 5, 6, 6, 7]
unique_numbers = set(number_list)
print("list of numbers after removing duplicates:", unique_numbers)
# set comprehention 
squares_set = {x **2 for x in range(1, 11)}
print("set of squares of numbers from 1 o 10:", squares_set)
# clearing a set 
set_a.clear()
print("set a after clearing:", set_a)
