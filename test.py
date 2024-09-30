def divide(num):
    try:
        10/num
    except ZeroDivisionError:
        print("hahahaa")
    else:
        print("GOOD")
    finally:
        print("finally")

num = 0
divide(num)
