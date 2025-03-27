#1bai code ve input va ham_ngay23thang3
# def my_list(age):
#     if age >= 18 and age <50:
#         print('da truong thanh')
#     elif age < 18 and age > 12:
#         print ('trung hoc co so')
#     elif age < 12 and age > 0:
#         print('tuoi tho')
#     else:
#         print('nghi huu')
# age =int(input("tran hien nay bao nhieu tuoi:"))
# my_list(age)

#2loop
# my_list=(1,2,3,4)
# for x in my_list:
#     print(x/3)

#3_btap kiem tra chang le
# #syntax: isinstance(n,int/float)
# def kiem_tra(n):
#     if n % 2 == 0:
#         return "Số chẵn"
#     else:
#         return "Số lẻ"

#4_Nhập từ người dùng
# so = int(input("Nhập số để kiểm tra: "))
# ket_qua = kiem_tra(so)
# print(ket_qua)

#5_baitapchanle
# so = float(input("Nhập số: "))
# if so.is_integer():  # Kiểm tra xem có phải số nguyên không
#     if int(so) % 2 == 0:
#         print("Số chẵn")
#     else:
#         print("Số lẻ")
# else:
#     print("Đây là số thực, không thể kiểm tra chẵn/lẻ!")
#6_baitapvesorted
# list = [34,90,21,4454,22,1443,433]
# list_sort = sorted(list)
# print(list_sort)
#7_baitapthemsorted
# danh_sach_hs_nu =['dao','thien','nhung','an','y']
# print(sorted(danh_sach_hs_nu,key=len))
#8_baikhac
# food =('ha', 'khoi bep','mien u dong dong','bun nam bo lau lau','pho ga ga','mien xao luon')
# sorted_food = sorted(food)
# print("Danh sach tang dan:",sorted_food) #tangdantheothutuAlphabe
# sorted_food_desc = sorted (food,reverse=True)
# print("Danh sach giam dan:",sorted_food_desc)#giamdantheothutuAlphabe
# sorted_by_length= sorted(food,key=len) #dodaicuatu
# print("Ds theo do dai ten mon:", sorted_by_length)
#9_baitapkhac
# magic = 'hocus,pocus'
# magic1 = magic.replace('cus', 'key')
# magic2 = magic.split(magic)
# print(type(magic))
# print(magic1)
# print(magic2)

#10_non_la = {'nhu xe','hoc hanh','linh li','nhu xe', 'linh li'}
# print(set(non_la))

#11_nummeric
# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

#12_convert from int to float:
# a = float(x)
# #convert from float to int:
# b = int(y)

#13_convert from int to complex:
# c = complex(x)
# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))

#14_phanrandom
# import random
# colors = ['red', 'blue', 'green']
# print(random.choice(colors))

#15_Array
# a = "Hello, World!"
# print(a[2],a[7]) #syntax luôn viết trong dấu ngoăc []


#16_baitap
# s = input("Nhập chuỗi:")
# if len(s) < 3:
#     print("Chuỗi quá ngắn!")
# else:
#     print("Ký tự đầu:", s[0]) #ký tư đầu tiên
#     print("Ký tự cuối:", s[-1]) #ký tự cuối cùng
#     print("Ký tự giữa:", s[len(s)//2]) #ký tự giữa
#     print("3 ký tự đầu:", s[:3]) # 3 ký tự đầu :3
#     print("3 ký tự cuối:", s[-3:])  # 3 ký tự cuối -3:
#     print("Đảo ngược:", s[::-1]) # đảo ngược chuỗi ::-1
     
#17_Check_String
# txt = "The best things in life are free!" baitapcheckstring
# print("free" in txt)
# txt = "The best things in life are free!"

#if "free" in txt:
#  print("Yes, 'free' is present.")

#18_Slicing_String
# b = "Hello, World!"
# print(b[2:]) #: từ 2 đến cuối

# b = "Hello, World!"
# print(b[-5:-2])

#19_Upper Case
# a = "Hello, World!"
# print(a.upper())

#20_Lower Casee
# a = "Hello, World!"
# print(a.lower())

#21_Remove Whitespace
# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"

#22_Replace String
# a = "Hello, World!"
# print(a.replace("H", "J"))

#23_Split String
# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']

# #24_String_Format/F-Strings
# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)

# #Placeholders and Modifiers
# #A placeholder can contain variables, operations, functions, and modifiers to format the value.
# price = 59
# txt = f"The price is {price} dollars"
# print(txt)

# #A placeholder can include a modifier to format the value.
# #A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
# price = 59
# txt = f"The price is {price:.2f} dollars" #Display the price with 2 decimals:
# print(txt)

# #A placeholder can contain Python code, like math operations:
# txt = f"The price is {20 * 59} dollars"
# print(txt)

#Escape Character
#The escape character allows you to use double quotes when you normally would not be allowed:
# txt = "We are the so-called \n Vikings from the north."
# print(txt) 

# text1 = "We1 are the so-called \'Vikings from the north."
# print(repr(text1))

# txt2 = "We2 are the so-called \\Vikings from the north."
# print(txt2) 

# txt3 = "We3 are the so-called \r Vikings from the north."
# print(txt3) 

# txt4 = "We4 are the so-called \t Vikings from the north."
# print(txt4) 

# txt5 = "We5 are the so-called \b Vikings from the north."
# print(txt5) 

# txt6 = "We6 are the so-called \f Vikings from the north."
# print(txt6) 

# txt7 = "We7 are the so-called \123 Vikings from the north."
# print(txt7) 

# txt8 = "We8 are the so-called \x53 Vikings from the north."  # \x53 = 'S'
# print(txt8)

#Boooleans
#bai1_booleans1
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

#bai2_booleans2
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

# x = 'Hello'
# y = 16
# print(bool(x))
# print(bool(y))

#baitap3_booleans
# print(bool('abc'))
# print(bool(123))
# print(bool(['apple','cherry','banana']))

#Boolean_Some Values are False
# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})

#Access Item
# thislist1 = ['apple','banana','cherry']
# print(thislist1[1])
# #Negative Index
# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1]) #-1 refers to the last item, -2 refers to the second last item
# #Range_Of_Index
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# #Remember that the first item is position 0,
# #and note that the item in position 5 is NOT included

# #This example returns the items from the beginning to, but NOT including, "kiwi":This example returns the items from the beginning to, but NOT including, "kiwi"
# thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist2[:4])

# #This example returns the items from "cherry" to the end
# thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist3[2:])

#CHANGE_ITEM_VALUE
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change a Range of Item Values
#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Insert Items
#Insert "watermelon" as the third item
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append() là một phương thức của list trong Python.Thêm 1 phần tử vào cuối danh sách (list)
#tên_list.append(giá_trị_mới)
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)
#Thêm nhiều phần tử_extend()	
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#Insert
mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1])
print(mylist)

#Remove_list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) #it will remove the 1st occurrence of item
#Remove_specific inndex
#Use_pop
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop() #if dont have specific index, will remove the last item
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0] #The [del] keyword also removes the specified index
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist #The del keyword can also delete the list completely

#Clear the List
#The clear() method empties the list.The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#PYTHON_LOOP LISTS
#Loop Through A List
thislist = ["apple", "banana", "cherry"]
for x in thislist: #loop through the list items by using a for loop
  print(x)