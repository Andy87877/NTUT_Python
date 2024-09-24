height = float(input())
weight = int(input())

bmi = float(weight) / float(height**2)
bmi = round(bmi, 3)

bmi *= 10**3

if (bmi%10 == 5):
    tmp = (bmi%100 - 5)/10
    if (tmp%2 == 1):
        bmi += 5
    else:
        bmi -= 5

bmi /= 10**3
bmi = round(bmi, 2)

print(format(bmi, '.2f'))