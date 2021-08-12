# Sử dụng Python thao tác với biến môi trường (Environment Variables)

- **Thực hiện:** Thi Minh Nhựt - **Email:** <thiminhnhut@gmail.com>

- **Thời gian:** Ngày 12 tháng 08 năm 2021

## Thư viện hỗ trợ

```bash
pip install python-decouple
```

## Nội dung

- Thư viện `decouple` hỗ trợ các file `*.ini` và `.env`.

- Ví dụ cơ bản: [simple.py](https://github.com/thiminhnhut/python/tree/master/environment-variables/simple.py)

- Lưu ý:

  - Các giá trị được đọc ra từ file `.env` và `*.ini` đều ở kiểu `string`, nên cần cast về kiểu dữ liệu mong muốn trong python (sử dụng option `cast=[data_type]`).

  - Khi đọc ra giá trị của một `key` nếu `key` này không tồn tại, chúng ta có thể sử dụng giá trị `default` với option `default=[Default Value]`.
