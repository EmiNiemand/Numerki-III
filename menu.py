import functions as func


def menu():
    function = choose_func()
    lower_range, upper_range = choose_range()
    knots_number = number_of_knots()
    return function, lower_range, upper_range, knots_number

def choose_func():
    while True:
        print("Choose function: "
              "\n1. 4x+3"
              "\n2. |x|"
              "\n3. 2x^3 + 2x^2 + 4x - 1"
              "\n4. sin(x)"
              "\n5. 4x * |x|"
              "\n6. sin(x) + 2x^3 + 2x^2 + 4x - 1")
        choice = int(input("funkcja: "))
        if choice == 1:
            return func.linear
        elif choice == 2:
            return func.absolute_x
        elif choice == 3:
            return func.polynomial
        elif choice == 4:
            return func.trigonometric
        elif choice == 5:
            return func.composite_1
        elif choice == 6:
            return func.composite_2
        print("Wybierz prawidłową liczbę (od 1 do 6)")


def choose_range():
    print("Choose range: ")
    lower_range = float(input("Lower range: "))
    upper_range = float(input("Upper range: "))
    if lower_range > upper_range:
        return upper_range, lower_range
    return lower_range, upper_range


def number_of_knots():
    return int(input("Number of Czebyszew knots: "))

