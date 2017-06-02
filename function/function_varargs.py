def total(a=5, *numbers, **phonebook):
    print("a", a)

    for number in numbers:
        print("number", number)

    for key, value in phonebook.items():
        print(key, value)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
