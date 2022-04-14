import math


def knots_x(knots_number: int, lower_range: float, upper_range: float):
    x = []
    for i in range(knots_number):
        x.append((math.cos(math.pi * (2 * i + 1) / (2 * knots_number + 1)) *
                  (upper_range - lower_range) + (lower_range + upper_range)) * 0.5)

    return x


def knots_y(x: [], function):
    y = []
    for knot in x:
        y.append(function(knot))

    return y


def coefficients(x: [], y: [], knots_number: int):
    a = y[::]
    for i in range(knots_number - 1):
        for j in range(knots_number - 1, i, -1):
            a[j] = (a[j] - a[j-1]) / (x[j] - x[j-i-1])

    return a


def newton(a: [], x: [], point: float):
    result = 0
    for i in range(len(x)):
        if a[i] != 0:
            multiplier = a[i]
            for j in range(i):
                multiplier = multiplier * (point - x[j])
            result += multiplier

    return result

