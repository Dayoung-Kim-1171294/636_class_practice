fruit_list = ['apple', 'banana', 'cherry']

def add_fruit(fruit: str):
    fruit_list.append(fruit)



print('Fruits in the list:')
print(fruit_list)

fruit_to_add = input('Enter a fruit to add to the list: ').strip()
fruit_list.append(fruit_to_add)
print('fruits after adding one directly:')
fruit_to_add = input('Enter another fruit to add to the list: ').strip()
add_fruit(fruit_to_add)
print('fruits after adding one via function:')
for fruit in fruit_list:
    print(fruit)

print('finished for loop')
print(fruit)
