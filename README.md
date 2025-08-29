# Giới thiệu Python và các câu lệnh cơ bản

## 1. Giới thiệu Python
Python là một ngôn ngữ lập trình bậc cao, dễ học, cú pháp rõ ràng, thường được dùng trong:
- Phân tích dữ liệu
- Trí tuệ nhân tạo (AI, Machine Learning)
- Lập trình web
- Tự động hóa công việc

---

## 2. Các câu lệnh cơ bản trong Python

### In ra màn hình (`print`)

print("Hello, Python!")
print("Tổng của 2 + 3 =", 2 + 3)
##Gán biến

x = 10
y = 5
ten = "Hậu"
print(x, y, ten)
##Nhập dữ liệu từ bàn phím (input)

##Sao chép mã
name = input("Nhập tên của bạn: ")
print("Xin chào,", name)
##Câu điều kiện (if - elif - else)

##Sao chép mã
n = 10
if n > 0:
    print("Số dương")
elif n == 0:
    print("Số 0")
else:
    print("Số âm")
##Vòng lặp for

##Sao chép mã
for i in range(5):
    print("i =", i)
##Vòng lặp while

##Sao chép mã
n = 3
while n > 0:
    print("n =", n)
    n -= 1
##Hàm (def)

##Sao chép mã
def tong(a, b):
    return a + b

print("Tổng 5 + 7 =", tong(5, 7))
##Danh sách (List)

##Sao chép mã
ds = [1, 2, 3, "Python"]
print("Danh sách:", ds)
print("Phần tử đầu tiên:", ds[0])

ds.append(99)
print("Sau khi thêm:", ds)
##Vòng lặp qua danh sách

##Sao chép mã
ds = ["Táo", "Cam", "Xoài"]
for trai_cay in ds:
    print(trai_cay)
##Từ điển (Dictionary)

##Sao chép mã
sv = {"ten": "Hậu", "tuoi": 20, "lop": "CNTT"}
print("Tên:", sv["ten"])
print("Tuổi:", sv["tuoi"])
