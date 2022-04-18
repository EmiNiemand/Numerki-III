import draw_func as df
import newton_and_knots as nk
from menu import menu

def main():
    #function, lower_range, upper_range, knots_number
    options = menu()
    x = nk.knots_x(options[3], options[1], options[2])
    y = nk.knots_y(x, options[0])
    a = nk.coefficients(x, y, options[3])
    df.draw_functions(options[1], options[2], options[0], a, x, y)


if __name__ == '__main__':
    main()

