# Lab: Password reset broken logic

## Mô tả lab

Bài lab này sai trong chức năng đặt lại mật khẩu. Mục tiêu của bài lab là chiếm quyền truy cập tài khoản `carlos` bằng cách lợi dụng lỗi trong cơ chế reset password.

## Các bước thực hiện

### Phân tích chức năng reset mật khẩu

Đầu tiên, truy cập chức năng Forgot password và thực hiện reset mật khẩu cho tài khoản `wiener`.

![alt text](image.png)

![alt text](image-1.png)

Đặt new password là `abc`

### Request đổi mật khẩu

Khi nhập mật khẩu mới cho `wiener`, Burp bắt được request `POST` dùng để đổi mật khẩu.

Request này có chứa tham số `username`. Đây là dấu hiệu nguy hiểm, vì tên tài khoản cần đổi mật khẩu lẽ ra không nên được tin tưởng từ dữ liệu do client gửi lên.

![alt text](image-2.png)

Tiếp theo, thay:

```text
username=wiener
```

thành:

```text
username=carlos
```
![alt text](image-3.png)

Log in.

![alt text](image-4.png)

Lav solved.