def calculate_bmi(height, weight):
    print("height="+ str(height))
    print("Weight="+ str(weight))
    bmi=weight/(height*height)
    print("bmi="+ str(bmi))
    if (bmi<18.5):
        print("Unnder Weight")
    elif (18.5<=bmi<=25.0):
        print("Normal weight")
    elif (bmi>25.0):
        print("Over Weight")
calculate_bmi(weight=57, height=1.73)