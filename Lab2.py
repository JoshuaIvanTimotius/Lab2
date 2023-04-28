def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    floatlist = get_user_input()
    average = calc_average(floatlist)
    minmax = calc_min_max_temperature(floatlist)
    print(minmax)
    sortedlist = sort_temperature(floatlist)
    print("sorted list is " + str(sortedlist))
    median = calc_median_temperature(floatlist)
    print("median is " + str(median))


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def calc_average(floatlist):
    y = 0
    for i in floatlist:
        y += 1
    total_sum = 0
    for x in floatlist:
        total_sum += x
    avg = total_sum / y
    print('Average of ', y, ' numbers is :', avg)
    return avg


def get_user_input():
    input1 = input()
    stringlist = input1.split(",")
    print(stringlist)
    floatlist = [float(x) for x in stringlist]
    print(floatlist)
    return floatlist


def calc_min_max_temperature(floatlist):
    print("The max temperature is ", max(floatlist))
    print("The min temperature is ", min(floatlist))
    minmax = [min(floatlist), max(floatlist)]
    return minmax


def sort_temperature(floatlist):
    floatlist.sort()
    return floatlist


def calc_median_temperature(floatlist):
    import statistics
    median = statistics.median(floatlist)
    return median


if __name__ == "__main__":
    main()
