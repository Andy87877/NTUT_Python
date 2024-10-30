temp_list = [False]*4

def myTestCase(a, b):
    counter = 0
    sum = 0
    while a != 1:
        print(a, counter)
        if counter == 3:
            temp_list[0] = True
            print("A")
            counter = 0
        if b % 3 == 0 and a < 100:
            temp_list[1] = True
            print("B")
            sum = b - 1
            b = b + 1
        if a % 2 == 0 and b < 100:
            temp_list[2] = True
            print("C")
            sum += a
            counter += 1
            a /= 2
            continue
        a -= 1
        temp_list[3] = True
        print("D")

    print("sum is", sum) 

myTestCase(10000,9)

print(temp_list)