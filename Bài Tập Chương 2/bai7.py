'''
Một số cách nhập dữ liệu từ bàn phím trong Python
1. Hàm input():
    - Hàm input() được sử dụng để nhận dữ liệu từ người dùng dưới dạng chuỗi (string).
    - Cú pháp: input(prompt)
    - Ví dụ:
      name = input("Nhập tên của bạn: ")
      print("Chào mừng, " + name + "!")
2. Chuỗi kiểu dữ liệu khi nhập:
    - Dữ liệu nhập từ bàn phím qua hàm input() luôn được coi là chuỗi (string).
    - Nếu cần dữ liệu kiểu số (int, float), bạn phải chuyển đổi kiểu dữ liệu.
    - Ví dụ:
      age = int(input("Nhập tuổi của bạn: "))  # Chuyển đổi sang int
      height = float(input("Nhập chiều cao của bạn (m): "))  # Chuyển đổi sang float
3. Nhập nhiều giá tri trên 1 dòng:
    - Bạn có thể nhập nhiều giá trị trên một dòng và tách chúng bằng dấu cách.
    - Sử dụng phương thức split() để tách chuỗi thành danh sách các chuỗi con.
    - Ví dụ:
      data = input("Nhập các số cách nhau bằng dấu cách: ")
      numbers = data.split()  # Tách chuỗi thành danh sách
      numbers = [int(num) for num in numbers]  # Chuyển đổi từng phần tử sang int
4. Nhập danh sách số:
    - Bạn có thể nhập một danh sách số từ bàn phím và chuyển đổi chúng thành danh sách các số nguyên hoặc số thực.
    - Ví dụ:
      nums = list(map(int, input("Nhập các số cách nhau bằng dấu cách: ").split()))
      print("Danh sách số:", nums)
'''