
personName = input("Please enter your name: ")
personAge = int(input("Please enter your age: "))


if personAge >= 18:
    print(f'{personName} is an adult.')
else:
    print(f'{personName} is a minor.')