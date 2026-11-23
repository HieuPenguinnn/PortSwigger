# Lab: JWT authentication bypass via weak signing key

## Mô tả lab

Ứng dụng dùng JWT (thuật toán HS256) làm session cookie. Khóa bí mật ký token quá yếu và nằm trong danh sách các secret phổ biến, nên ta có thể brute-force (crack) khóa đó rồi tự tạo token administrator. 

## Các bước thực hiện

### Phân tích

![alt text](image.png)

Thử bỏ chữ ký hoặc đổi thuật toán thành `none` như 2 lab trước nhưng không được.

Lưu JWT lấy từ response vào một file:

![alt text](image-1.png)

JWT dùng thuật toán `HS256`, nên ta chỉ cần khóa bí mật là có thể tự ký token tùy ý. Chạy hashcat:

```
hashcat -a 0 -m 16500 jwt.txt /usr/share/wordlists/rockyou.txt
```

Sau một lúc, hashcat tìm ra khóa đúng:

![alt text](image-2.png)

### Khai thác

Có khóa ký rồi, ta có thể tạo token tùy ý. Lưu khóa vào key store của `JWT Editor`:

![alt text](image-3.png)

Gửi request `/admin` sang Burp Repeater, đổi `sub` thành `administrator` rồi re-sign token bằng khóa vừa lưu:

![alt text](image-4.png)

Xóa user `carlos`:

![alt text](image-5.png)

![alt text](image-6.png)

Lab solved.
