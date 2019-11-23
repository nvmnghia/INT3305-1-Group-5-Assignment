# Exercise 5

## Assignee

Nguyễn Việt Minh Nghĩa - 15021358

## Problem

> Hãy viết các chương trình sinh ra các ảnh sau:
>
> - Bàn cờ vua gồm các ô đen trắng đan xen.
> - Dải màu biến đổi tuần tự theo chiều ngang từ đỏ đến tím (gợi ý, có thể sử dụng hệ màu khác RGB, ví dụ HSL).
> - Dải màu biến đổi tuần tự theo chiều dọc từ đỏ đến tím.
> - Dải màu biến đổi tuần tự theo chiều chéo từ đỏ đến tím.

## Solution

### 1. Checkerboard generator

#### 1. Run

```bash
$ pip install -r requirements.txt
...

$ python checkerboard.py -h
usage: checkerboard.py [-h] [-c C] [-r R] [-s S] [O]

Generate checkerboard pattern.

positional arguments:
  O                 Output filename (default output.png)

optional arguments:
  -h, --help        show this help message and exit
  -c C, --column C  Number of column (default 8)
  -r R, --row R     Number of row (default 8)
  -s S, --ssize S   Size of each square (default 50 px)

$ python checkerboard.py
...
```

#### 2. Preview

![checkerboard.png](../Ex5/checkerboard.png)
