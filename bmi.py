def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    print("bmi = " + str(bmi))

    if bmi < 18.5:
        print("user is under weight")
    elif 18.5 <= bmi <= 25.0:
        print("user is normal weight")
    else:
        print("user is over weight")


calculate_bmi(weight=57, height=1.73)
