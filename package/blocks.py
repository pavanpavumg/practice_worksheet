def age():
    age_enter = int(input("enter your age"))

    try:
        age = int(age_enter)
        if age < 0:
            print("age count be negative")
        elif age > 120:
            print("enter valid age")
        else:
            years_left = 100 - age
            if years_left <0:
                print(f"you have {years_left} years left to live")
            elif years_left == 0:
                print("you have reache d 100 years")
            else:
                print(f"you have {years_left} yrars lrft to live")


    except ValueError:
        print("invalid input, enter a number")

age()


