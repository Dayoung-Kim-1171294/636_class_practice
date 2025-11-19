shopping_list = []

def get_qty(list_item: str) -> int:
    qty = input(f"Enter the quantity for {list_item}: ").strip()
    if not qty.isdigit():
        print("Please enter a valid number for quantity.")
        return get_qty(list_item)
    return int(qty)


list_item = input("Enter an item for your shopping list: ").strip()
# shopping_list.append('banana')

while list_item.lower() != 'done':
    units = input(f"Enter the units for {list_item} (e.g., kg, litres, packs): ").strip()

    # qty = input(f"Enter the quantity for {list_item}: ").strip()
    shopping_list.append((list_item, get_qty(list_item), units))
    list_item = input("Enter an item for your shopping list: ").strip()

print("\nYour Shopping List:")
for item in shopping_list:
    # print(item)
    print(f"You need to buy {item[1]} {item[2]} of {item[0].capitalize()}.")

