# BUG NGHIÊM TRỌNG: Hai tham số có cùng tên
# Đây là một lỗi cú pháp và logic rõ ràng mà SonarCloud không thể bỏ qua.
def process_data(data, data):
    if data is not None:
        print("Processing data...")
        # Dòng code này sẽ không bao giờ được thực thi đúng cách
        # vì tham số 'data' thứ hai đã ghi đè lên cái thứ nhất.
        print(f"Received: {data}")

# Gọi hàm với một giá trị để kích hoạt phân tích
process_data("some_value_1", "some_value_2")
