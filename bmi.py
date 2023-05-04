def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    print("bmi = " + str(bmi))

    if bmi < 18.5:
        print("user is under weight")
        return -1
    elif 18.5 <= bmi <= 25.0:
        print("user is normal weight")
        return 0
    else:
        print("user is over weight")
        return 1


X=calculate_bmi(weight=57, height=1.73)
print(X)
