
result = 0

def add_to_result(value: int, result: int) -> None:
    result += value
    return result

def reset_result() -> None:
    global result
    result = 0

print(f"Initial result: {result}")
input_value = int(input("Enter a number to add to the result: "))
result = add_to_result(input_value, result)
print(f"Updated result: {result}")
reset_result()
input_value = int(input("Enter another number to add to the result: "))
result = add_to_result(input_value, result)
print("updated result:", result)

