# Báo Cáo Tuần 1
<i><b>Thời gian thực hiện:</b> Từ ngày 13/11/2023 đến 19/11/2023</i>

## Nội dung: Nhận diện bảng trong ảnh
  Xây dụng module identify_table Với 1 lớp 
  class Table_Img(path) - tham số path là đường dẫn ảnh
    preprocess() - Phương thức xử lý ảnh sang ảnh nhị phân.
    _lines() - phương thức xác định các vector đường thẳng.
    _group_lines() - nhóm các vector đường thẳng nhỏ thành 1 đường thẳng nối liền.
    find_horizontal_lines() - phương thức tìm các đường thẳng ngang bằng các sử dụng _lines() và _group_lines()
    find_vertical_lines() - phương thức tìm các đường thẳng doc bằng các sử dụng _lines() và _group_lines()
    <b>cut_cell()</b> - phương thức tìm ra giao điểm của horizontal_lines và vertical_lines để xác định ô và cắt thành từng ảnh riêng.
## Sử dụng module
    img = Table_Img(img_path)
    cells, list_img = img.cut_cell()
  
  cells nhận được 1 dang sách các ô, mõi ô có cấu trúc [[x1,y1], [x2, y2]]
  
  list_img là một danh sách 2 chiều, mõi phần tử là image (kiêu tuble) 
