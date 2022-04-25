# calculate years for people


year_start = int(input("Enter year born: " ))


year_current = 2022

age = year_current - year_start
if year_start < 1900:
    print ("Error")
elif age >= 1 and age <= 3:
    print (age, "Years, Baby!!!")
elif age >= 4 and age <= 9:
    print(age, "Years, Kid!!!")
elif age >= 10 and age <= 15:
    print(age, "Years, Teen!!!")
elif age >= 16 and age <= 18:
    print (age, "Years, Young!!!")
elif age >= 19 and age <= 50:
    print (age, "Years, Adult!!!")
elif age >=51:
    print (age, "Years, Old!!!")


