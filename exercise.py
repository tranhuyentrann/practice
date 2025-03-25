# #bai code ve input va ham_ngay23thang3
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

# #loop
# my_list=(1,2,3,4)
# for x in my_list:
#     print(x/3)

# #btap kiem tra chang le
# #syntax: isinstance(n,int/float)
# def kiem_tra(n):
#     if n % 2 == 0:
#         return "Số chẵn"
#     else:
#         return "Số lẻ"

# # Nhập từ người dùng
# so = int(input("Nhập số để kiểm tra: "))
# ket_qua = kiem_tra(so)
# print(ket_qua)

# #baitapchanle_2
# so = float(input("Nhập số: "))
# if so.is_integer():  # Kiểm tra xem có phải số nguyên không
#     if int(so) % 2 == 0:
#         print("Số chẵn")
#     else:
#         print("Số lẻ")
# else:
#     print("Đây là số thực, không thể kiểm tra chẵn/lẻ!")
# #baitapvesorted
# list = [34,90,21,4454,22,1443,433]
# list_sort = sorted(list)
# print(list_sort)
# #baitapthemsorted
# danh_sach_hs_nu =['dao','thien','nhung','an','y']
# print(sorted(danh_sach_hs_nu,key=len))
# #baikhac
# food =('ha', 'khoi bep','mien u dong dong','bun nam bo lau lau','pho ga ga','mien xao luon')
# sorted_food = sorted(food)
# print("Danh sach tang dan:",sorted_food) #tangdantheothutuAlphabe
# sorted_food_desc = sorted (food,reverse=True)
# print("Danh sach giam dan:",sorted_food_desc)#giamdantheothutuAlphabe
# sorted_by_length= sorted(food,key=len) #dodaicuatu
# print("Ds theo do dai ten mon:", sorted_by_length)
#baitapkhac
# magic = 'hocus,pocus'
# magic1 = magic.replace('cus', 'key')
# magic2 = magic.split(magic)
# print(type(magic))
# print(magic1)
# # print(magic2)
# non_la = {'nhu xe','hoc hanh','linh li','nhu xe', 'linh li'}
# print(set(non_la))

# #nummeric
# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# #convert from int to float:
# a = float(x)
# #convert from float to int:
# b = int(y)
# #convert from int to complex:
# c = complex(x)
# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))
# #phanrandom
# import random
# colors = ['red', 'blue', 'green']
# print(random.choice(colors))

#Array
# a = "Hello, World!"
# print(a[2],a[7]) #syntax luôn viết trong dấu ngoăc []


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

