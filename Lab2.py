def main():
    print ("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list=get_user_input()

def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5, 67, 32)")

def get_user_input():
    floatlist=[]
    x=input()
    print(x)
    x .split(", ")
    floatlist= [float(value) for value in x]
    return floatlist


def calc_average():
    x=get_user_input()
    avg=sum(x)/len(x)
    print("the average temperature is " , avg)

def find_min_max():
    x=get_user_input()
    maxi=max(x)
    mini=min(x)
    print("the maximum temperature is " , maxi)
    print("the minimum temperature is " , mini)
