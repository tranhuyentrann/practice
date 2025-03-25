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

#btap kiem tra chang le
#syntax: isinstance(n,int/float)
def kiem_tra(n):
    if n % 2 == 0:
        return "Số chẵn"
    else:
        return "Số lẻ"

# Nhập từ người dùng
so = int(input("Nhập số để kiểm tra: "))
ket_qua = kiem_tra(so)
print(ket_qua)
