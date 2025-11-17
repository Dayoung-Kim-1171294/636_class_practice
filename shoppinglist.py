shopping_list = []

list_item = input("Enter an item for your shopping list: ").strip()
# shopping_list.append('banana')

while list_item.lower() != 'done':
    qty = input(f"Enter the quantity for {list_item}: ").strip()
    shopping_list.append((list_item, qty))
    list_item = input("Enter an item for your shopping list: ").strip()

print("\nYour Shopping List:")
for item in shopping_list:
    # print(item)
    print(f"You need to buy {item[1]} of {item[0]}.")