def calculate_bmi(height, weight):
    print("height="+ str(height))
    print("Weight="+ str(weight))
    bmi=weight/(height*height)
    print("bmi="+ str(bmi))
    return checkbmi(bmi)



def checkbmi(bmi):
     if (bmi<18.5):
         print("Under Weight")
         return -1
     elif (18.5<=bmi<=25.0):
         print("Normal weight")
         return 0
     elif (bmi>25.0):
         print("Over Weight")
         return 1


returnvalue = calculate_bmi(weight=57, height=1.73)
print(returnvalue)