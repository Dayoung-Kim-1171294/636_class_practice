def display_formatted_row(row, format_str):

    if type(row) == tuple:
        row = list(row)

    for index, item in enumerate(row):
        if item is None:
            row[index] = ''     
        else:
            row[index] = str(item)

    print(format_str.format(*row))

shopping_list = [
    ('Apples', 5, 'items'),
    ('Bananas', 10, 'bunches'),
    ('Cherries', 20, 'puppets'),
    ('Dates', 15, 'pieces'),
    ('Elderberries', 7, 'jars')
]

format_string = "{: <15} | {: >5} | {: >7}"
display_formatted_row(("Item", "Qty", "Unit"), format_string)
display_formatted_row(('---', '---', '---'), format_string)

for entry in shopping_list:
    display_formatted_row(entry, format_string)

# for entry in shopping_list:
#     print(entry)



