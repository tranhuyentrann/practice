#💼 MINI PROJECT: HỒ SƠ NGƯỜI DÙNG – USER PROFILE MANAGER
#🎯 Mục tiêu:
#Tạo một chương trình cho phép người dùng:
#Nhập thông tin cá nhân
#Phân loại theo độ tuổi
#Kiểm tra sở thích liên quan đến học Python
#Hiển thị lại toàn bộ thông tin dưới dạng đẹp và rõ ràng
user_name=input("Hãy nhập tên của bạn: ")
user_birth=int(input("Hãy nhập năm sinh của bạn: "))
user_year=int(input("Nhập năm hiện tại: "))
user_py=str(input("Bạn có thích học Python không? Nhập Y là Có, N là Không: ")) 
user_age=int (user_year - user_birth)
print(f"Bạn {user_name}, năm nay {user_age} tuổi ") 
y = user_age
if y >= 60:
    print(f"{user_name} đã già")
elif 12 <= y <=18:
    print(f"{user_name} đang là tuổi teen")
elif 19<= y <=30:
    print(f"{user_name} đang là tuổi thanh xuân rực rỡ")
elif 31<= y <=40:
    print(f"{user_name} đang tuổi trưởng thành")
elif 41<= y<=59:
    print(f"{user_name} gần về hưu và là bậc tiền bối trong xã hội")    
else:
    print(f"{user_name} đang là trẻ em")
x = user_py
if x.lower() == "y":
    print(f"{user_name} ✅ Có thích học Python")
else:
    print(f"{user_name} ❌ Không thích học Python")
