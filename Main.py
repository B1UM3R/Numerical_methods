import math


def eps():
    return 0.5 * math.pow(10, -5)


def f(x):
    return x - 3*math.cos(x*x)


def f_1(x):
    return 1 + 6*x*math.sin(x*x)


def f_2(x):
    return 12*x*x*math.cos(x*x) + 6*math.sin(x*x)


def fi(x):
    return math.sqrt(math.acos(x/3))


def root_check(number):
    result = f(number[0]) * f(number[1])
    print("Произведение f(a)f(b) = " + str(result) + " < 0")
    print("Значит наш корень лежит на отрезке [" + str(number[0]) + ", " + str(number[1]) + "]")


def x0_check(x0):
    result = f(x0) * f_2(x0)
    print("За х0 возьмем конец отрезка, тогда х0 = " + str(x0))
    print("f(x0) * f''(x0) = " + str(result) + " > 0")


def first_method(number):
    left, right = number
    epsilon = eps()
    count = 0
    number_of_steps = math.ceil(math.log((number[1] - number[0]) / epsilon, 2))
    while math.fabs(f((left + right) / 2)) >= epsilon and number_of_steps >= count:
        count += 1
        middle = (left + right)/2
        if f(left)*f(middle) < 0:
            right = middle
        elif f(middle)*f(right) < 0:
            left = middle
    result = (right + left)/2
    print("Метод половинного деления: ")
    print(" Результат: " + str(result))
    print(" Количество итераций: " + str(count))


def second_method(x0):
    epsilon = eps()
    xn = x0
    count = 0
    while True:
        count += 1
        new = xn - f(xn) / f_1(xn)
        if math.fabs(new - xn) < epsilon:
            print("Метод Ньютона: ")
            print(" Результат: " + str(new))
            print(" Количество итераций: " + str(count))
            break
        xn = new


def third_method(x0):
    epsilon = eps()
    xn = x0
    count = 0
    while True:
        count += 1
        new = xn - f(xn) / f_1(x0)
        if math.fabs(new - xn) < epsilon:
            print("Модифицированный метод Ньютона: ")
            print(" Результат: " + str(new))
            print(" Количество итераций: " + str(count))
            break
        xn = new


def fourth_method(number, x0):
    epsilon = eps()
    if x0 == number[0]:
        xn = number[1]
    elif x0 == number[1]:
        xn = number[0]
    count = 0
    while True:
        count += 1
        new = xn - f(xn) * (xn - x0) / (f(xn) - f(x0))
        if math.fabs(new - xn) < epsilon:
            print("Метод хорд: ")
            print(" Результат: " + str(new))
            print(" Количество итераций: " + str(count))
            break
        xn = new


def fifth_method(number, x0):
    prev = x0
    epsilon = eps()
    if x0 == number[0]:
        xn = number[1]
    elif x0 == number[1]:
        xn = number[0]
    count = 0
    while True:
        count += 1
        new = xn - f(xn) * (xn - prev) / (f(xn) - f(prev))
        if math.fabs(new - xn) < epsilon:
            print("Метод подвижных хорд: ")
            print(" Результат: " + str(new))
            print(" Количество итераций: " + str(count))
            break
        prev = xn
        xn = new


def sixth_method(x0):
    epsilon = eps()
    xn = x0
    count = 0
    while True:
        count += 1
        new = fi(xn)
        if math.fabs(new - xn) < epsilon:
            print("Метод простой итерации: ")
            print(" Результат: " + str(new))
            print(" Количество итераций: " + str(count))
            break
        xn = new


def main():
    number = (1, 1.25)
    x0 = 1.25
    root_check(number)
    x0_check(x0)
    first_method(number)
    second_method(x0)
    third_method(x0)
    fourth_method(number, x0)
    fifth_method(number, x0)
    sixth_method(x0)


if __name__ == '__main__':
    main()