def my_list(age):
    if age >= 18 and age <50:
        print('da truong thanh')
    elif age < 18 and age > 12:
        print ('trung hoc co so')
    elif age < 12 and age > 0:
        print('tuoi tho')
    else:
        print('nghi huu')
age =int(input("tran hien nay bao nhieu tuoi:"))
my_list(age)
 