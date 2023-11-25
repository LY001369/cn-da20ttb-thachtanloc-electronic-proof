# Sử dụng image Python chính thức làm base image
FROM python:3.10

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Sao chép các file requirements.txt (nếu có) vào container và cài đặt dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Command để chạy ứng dụng khi container được khởi chạy
CMD ["python", "app.py"]
