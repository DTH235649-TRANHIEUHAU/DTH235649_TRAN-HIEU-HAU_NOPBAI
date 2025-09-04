'''
I. Các loại lỗi trong Python:
    1. Lỗi cú pháp (Syntax Errors):
        - Xảy ra khi mã nguồn không tuân thủ quy tắc cú pháp của Python.
        - Ví dụ: thiếu dấu hai chấm, dấu ngoặc không đóng, viết sai từ khóa.
        - Ví dụ mã:
            if True
                print("Hello, World!")
        - Cách xử lý: Sửa lỗi cú pháp theo thông báo lỗi của trình thông dịch.
    2. Lỗi thực thi (Runtime Errors):
        - Xảy ra khi mã nguồn có cú pháp đúng nhưng gặp sự cố trong quá trình thực thi.
        - Ví dụ: chia cho số không, truy cập vào chỉ mục ngoài phạm vi của danh sách.
        - Ví dụ mã:
            x = 10 / 0
        - Cách xử lý: Sử dụng khối try-except để bắt và xử lý lỗi. 
    3. Lỗi logic (Logical Errors):
        - Xảy ra khi mã nguồn chạy mà không báo lỗi, nhưng kết quả không như
II. Cách bắt  lỗi trong Python:
    1. Cú pháp cơ bản: 
        try , except , finally.
    2.Bắt lỗi cụ thể:
        - Sử dụng tên lỗi cụ thể trong khối except để xử lý các loại lỗi khác nhau. mong đợi.
        - Ví dụ: sử dụng sai toán tử, sai công thức tính toán
    3. Sử dụng khối else:
        - Khối else sẽ được thực thi nếu không có lỗi nào xảy ra trong khối try.   
            
'''