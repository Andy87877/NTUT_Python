def my_divide(x, y):
    try:
        c = x / y
    except ZeroDivisionError:
        print("divide by zero", end="")
        return
    else:
        print(int(c), end="")
        return
    finally:
        print("END")


my_divide(10, 2)
my_divide(10, 0)
