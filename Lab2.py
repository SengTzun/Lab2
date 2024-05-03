def main():
    print ("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    z=get_user_input()
    calc_average(z)
    find_min_max(z)
    w=sort_temperature(z)
    calc_median_temperature(w)

def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5, 67, 32)")

def get_user_input():
    floatlist=[]
    x=input()
    print(x)
    y=x.split(", ")
    floatlist= [float(value) for value in y]
    return floatlist


def calc_average(x):
    avg=sum(x)/len(x)
    print("the average temperature is " , avg)
    return avg

def find_min_max(x):
    maxi=max(x)
    mini=min(x)
    print("the maximum temperature is " , maxi)
    print("the minimum temperature is " , mini)
    ans=[maxi, mini]
    return ans

def sort_temperature(x):
    sortednumbers = sorted(x)
    print(sortednumbers)
    return sortednumbers
def calc_median_temperature(w):
    n = len(w)
    if n % 2 == 0:
        median = (w[n//2 - 1] + w[n//2]) / 2
    else:
        median = w[n//2]
    print("median temperature is " , median)
    return median
    
if __name__=="__main__":
    main()