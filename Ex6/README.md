# Exercise 6

## Assignee

Lê Tuấn Anh - 17020572

## Problem

> Hãy viết chương trình thực hiện các việc sau:
>
> - Tính linear convolution của hai vector cho trước. So sánh kết quả với việc gọi hàm có sẵn của scipy/python.
> - Tính cyclic convolution của hai vector cho trước. So sánh kết quả với việc gọi hàm có sẵn của scipy/python (nếu có).
> - Tính cyclic convolution từ linear convolution theo hướng dẫn trong slide bài giảng và so sánh kết quả với cách tính cyclic convolution ở trên.

## Solution

Giải pháp thi công

- Sử dụng numpy.convole để tính linear convolution
- Tự tính linear convolution:
  - Xây dựng 1 hàm convert từ vector sang ma trận cần để tính linear
  - Nhân ma trận với vector dài hơn để trả về 1 vector kết quả
- Tự tính cyclic convolution:
  - Xây dựng 1 hàm convert từ vector ngắn hơn sang ma trận cần để tính cyclic
  - Nhân ma trận với vector dài hơn để trả về 1 vector kết quả
- Tính cyclic từ linear
  - Tính cyclic trả về 1 vector (Tận dụng hàm tự tính hoặc dùng hàm `convole`)
  - Giả sử chiều dài vector ngắn hơn là x thì ta cộng x-1 phần tử cuối trong mảng vừa tính linear được lên vị trí đầu và loại bỏ các phần tử vừa được lấy để cộng, ta sẽ được cyclic convolution

create by Lê Tuấn Anh 24/11/2019
