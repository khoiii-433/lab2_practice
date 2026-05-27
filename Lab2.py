print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67,32)") 
def get_user_input():
    print("get_user_input")
    inputstr = input()
    strlist = inputstr.split(",")
    print(strlist)
    floatlist = []
    for x in strlist:
        floatlist.append(float(x))
    print(floatlist)
    return floatlist
def calculate_average(floatlist):
    print("calculate_average")
    average = sum(floatlist) / len(floatlist)
    print("Average = " average)
    return average
def find_min_max(floatlist):
    print("find_min_max")
    temp_list= floatlist.copy()
    temp_list.sort()
    return [temp_list[0], temp_list[-1]]
def calc_med