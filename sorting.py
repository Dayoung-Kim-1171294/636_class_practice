# list_of_students = ["Stuart", "Craig", "Troy", "Josh" ]
# print ("Original list:", list_of_students)
# sorted_students = sorted(list_of_students)
# print("Sorted list:", sorted_students)
# print ("Original list:", list_of_students)
# print("In-place sort:")
# list_of_students.sort()
# print ("Sorted list:", list_of_students)
# print("Original list:", list_of_students)

tuple_list = [
    ("COMP636", "Stuart", 1),
    ("COMP637", "Alice", 2),
    ("COMP638", "David", 3),
    ("COMP639", "Bob", 2),
]

sorted_tuple_list = sorted(tuple_list)
print("Sorted tuple list:", sorted_tuple_list)
# sorted(iterable, key=function, reverse=False)
def get_second_element(item):
    return item[2]

# sorted_by_element = sorted(tuple_list, key=get_second_element)
sorted_by_element = sorted(tuple_list, key=lambda x: x[2])
sorted_by_element = sorted(tuple_list, key=lambda x: (x[2], x[1]))
print("Sorted by second element:", sorted_by_element)