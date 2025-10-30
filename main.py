# VULNERABILITY (LỖ HỔNG BẢO MẬT): Hard-coded password
# Đây là một lỗi bảo mật nghiêm trọng mà SonarCloud chắc chắn sẽ phát hiện
# và Quality Gate của bạn sẽ không thể bỏ qua.

SECRET_KEY = "my-super-secret-password-that-should-not-be-in-code"

def check_access(key_provided):
    """
    Một hàm đơn giản để kiểm tra khóa bí mật.
    Hàm này có lỗ hổng bảo mật nghiêm trọng.
    """
    if key_provided == SECRET_KEY:
        return "Access Granted"
    else:
        return "Access Denied"

# In ra để SonarCloud biết code này đang được sử dụng
print(check_access("some-key"))
