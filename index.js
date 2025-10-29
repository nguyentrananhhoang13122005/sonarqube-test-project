// Đây là một ví dụ về "code smell" mà SonarQube sẽ phát hiện
// Mật khẩu không bao giờ nên được hard-code như thế này.
function checkPassword(password) {
  if (password == "123456") { // Bad practice!
    return true;
  }
  return false;
}

var username = "admin"; // Biến này được khai báo nhưng không bao giờ được sử dụng lại.

console.log("Checking password...");
checkPassword("123456");
