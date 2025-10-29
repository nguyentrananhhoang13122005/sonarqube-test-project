import os # LỖI: Module được import nhưng không bao giờ sử dụng

# VULNERABILITY (LỖ HỔNG BẢO MẬT): Thông tin nhạy cảm không bao giờ nên được viết thẳng vào code.
# SonarQube sẽ phát hiện ra điều này ngay lập tức.
DATABASE_PASSWORD = "super_secret_password_123"

# BUG (LỖI NGHIÊM TRỌNG): Sử dụng một đối tượng có thể thay đổi (mutable) làm giá trị mặc định.
# Đây là một lỗi logic phổ biến trong Python, gây ra hành vi không mong muốn.
def add_user(username, user_list=[]):
    user_list.append(username)
    return user_list

# CODE SMELL (MÃ CÓ MÙI): Hàm này quá phức tạp và khó bảo trì.
# SonarQube sẽ tính toán "Độ phức tạp nhận thức" và cảnh báo bạn.
def check_permissions(user_role, action, environment):
    if user_role == "admin":
        return True
    else:
        if user_role == "editor":
            if action in ["create", "edit"]:
                if environment != "production":
                    return True
    return False

# CODE SMELL (MÃ CÓ MÙI): So sánh với None nên dùng 'is' thay vì '=='
def get_user_profile(user):
    if user == None:
        return "User not found"
    return f"Profile for {user}"

# Chạy chương trình
print("Running application...")

# Lần gọi đầu tiên, kết quả đúng như mong đợi: ['user_a']
users1 = add_user("user_a")
print(f"Users 1: {users1}")

# Lần gọi thứ hai, kết quả sẽ sai: ['user_a', 'user_b'] thay vì chỉ ['user_b']
# vì list mặc định đã bị thay đổi ở lần gọi trước.
users2 = add_user("user_b")
print(f"Users 2: {users2}") # Đây là hậu quả của BUG ở trên!
