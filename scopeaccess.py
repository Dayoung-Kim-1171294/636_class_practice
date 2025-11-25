



this_is_a_variable = "Hello from Global scope"
def display_variable():
    print(this_is_a_variable)
    this_is_a_variable = "Hello from Local scope"
    print(this_is_a_variable)


display_variable()