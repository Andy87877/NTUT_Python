def round_test(BMI):
    # print(BMI)

    BMI *= 1000
    BMI //= 1

    number = BMI % 10

    if number == 5:
        fo_number = (BMI % 100 - BMI % 10) // 10
        if fo_number % 2 == 1:
            BMI += 5
        else:
            BMI -= 5

    BMI //= 10
    BMI /= 100

    return BMI


meter = float(input())
kg = float(input())

BMI = kg / (meter * meter)

BMI = round_test(BMI)

print(format(BMI, ".2f"))
