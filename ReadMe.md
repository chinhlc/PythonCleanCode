# Le Cong Chinh

## Khoá học Clean Code

## Phần 1: Clean Code căn bản

1. 5 mục tiêu chính của Clean Code là
   - Mục tiêu 1: tôi ưu code và khả năng viết code, cũng như đặt tên
   - Mục tiêu 2: các function rõ ràng chính xác dễ hiểu
   - Mục tiêu 3: dễ maintain, thêm sửa sau này
   - Mục tiêu 4: có thể tái sử dụng
   - Mục tiêu 5: chạy tốt trên tất cả các case
2. Đáp án của tôi là team A bởi vì:
   - Lý do 1: Trong làm dự án, quan trọng nhất vẫn là tiến độ để bàn giao cho khách hàng
   - Lý do 2: Sau khi giải quyết được vấn đề với khách hàng thì lúc đó ta mới tính đến chuyện cleancode

## Phần 2: OOP và SOLID

bỏ qua

## Phần 3: Thiết kế CSDL Quan hệ theo đặc tả

```
CREATE TABLE user (
   user_id INTEGER PRIMARY KEY,
   email VARCHAR(1000) NOT NULL,
   pasword INTEGER NOT NULL
);

CREATE TABLE teacher (
   user_id INTEGER PRIMARY KEY,
   phone INTEGER NOT NULL,
   experiences INTEGER NOT NULL,
);

CREATE TABLE student (
   user_id INTEGER PRIMARY KEY,
   year DATETIME
);

CREATE TABLE course (
   name VARCHAR(100) NOT NULL,
   description VARCHAR(1000) NOT NULL,
   location VARCHAR(200) NOT NULL,
   opened DATETIME
);

CREATE TABLE enroll (
   user_id INTEGER PRIMARY KEY,
   name VARCHAR(100) NOT NULL,
);

```

## Phần 4: Thiết kế RESTful API

Bỏ qua

## Phần 5: Lập trình Restful API

Bỏ qua

## Trắc nghiệm

         1.c
         2.B
         3.D
         4.C
            5.A
         6.A
            7.
         8.A
         9.B
         10.A
         11.D
         12.C
         13.B
            14.
         15.C
            16.
            17.
            18.A
         19.C
         20.B
            21.
            22.
            23.
            24.
         25.A
