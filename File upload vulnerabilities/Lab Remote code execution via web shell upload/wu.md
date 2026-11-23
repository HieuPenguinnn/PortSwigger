# Lab: Remote code execution via web shell upload

## Mô tả lab

Ứng dụng có chức năng upload avatar và kiểm tra để xác minh file được upload đúng là ảnh. Mục tiêu là tạo một file polyglot vừa là ảnh hợp lệ vừa chứa code PHP, upload làm web shell và đọc `/home/carlos/secret`.

## Các bước thực hiện

Ứng dụng là trang blog. Đăng nhập bằng `wiener`, thử upload avatar với một ảnh hợp lệ:

![alt text](image.png)

![alt text](image-1.png)

Khi trang hiển thị avatar, trình duyệt gửi một request `GET /files/avatars/<tên-file>.jpg` và server trả về đúng nội dung ảnh:

![alt text](image-2.png)

Thử thay phần nội dung file bằng code PHP web shell với một payload đọc `/etc/passwd` để kiểm chứng khả năng thực thi:

```php
<?php readfile('/etc/passwd'); ?>
```

Gửi request, server trả về thông báo upload thành công cho `avatars/payload.php`:

![alt text](image-3.png)

Bây giờ truy cập file web shell vừa upload tại `GET /files/avatars/payload.php`:

![alt text](image-4.png)

Response trả về toàn bộ nội dung `/etc/passwd`, chứng tỏ web shell đã được thực thi chứ không chỉ lưu trữ

Đọc file secret `/home/carlos/secret` mà lab yêu cầu:

![alt text](image-5.png)

Upload lại rồi truy cập `GET /files/avatars/payload.php` một lần nữa. Response trả về chuỗi secret của user `carlos`:

![alt text](image-6.png)

Submit secret:

![alt text](image-7.png)

Lab solved.
