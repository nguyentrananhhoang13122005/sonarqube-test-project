# BUG (LỖI NGHIÊM TRỌNG): Sử dụng một đối tượng có thể thay đổi (mutable) làm giá trị mặc định.
# Chúng ta biết chắc rằng SonarQube xếp lỗi này vào mức độ 'High'.
def add_user(username, user_list=[]):
    user_list.append(username)
    return user_list

print("Running simple test...")

# Lần gọi đầu tiên, kết quả đúng: ['user_a']
users1 = add_user("user_a")
print(f"Users 1: {users1}")

# Lần gọi thứ hai, kết quả sẽ sai: ['user_a', 'user_b']
# Đây là hậu quả trực tiếp của lỗi ở trên.
users2 = add_user("user_b")
print(f"Users 2: {users2}")
