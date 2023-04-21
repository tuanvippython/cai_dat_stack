#tạo lớp Stack gồm các thuộc tính là : giới hạn số phần tử trong Stack và tạo Stack rỗng
class Stack:
    def __init__(self,gioi_han):
        self.danh_sach_gioi_han = gioi_han
        self.danh_sach = []

    # Hàm kiểm tra Stack có rỗng hay không
    # Nếu rỗng trả về số phần tử trong Stack là 0
    def is_empty(self):
        return len(self.danh_sach) == 0
    
    # Hàm kiểm tra Stack đã đủ phần tử hay chưa
    # Nếu đủ thì trả về số phần 
    def is_full(self):
        return len(self.danh_sach) == self.danh_sach_gioi_han
    
    # Hàm thêm phần tử vào đỉnh Stack
    def push_stack(self,value):
        # Kiểm tra nếu số phần tử trong Stack bé hơn số phần tử giới hạn trong Stack thì thêm phần tử mới vào Stack
        if len(self.danh_sach) < self.danh_sach_gioi_han:
            self.danh_sach.append(value)
            print(f"Đã thêm phần tử {value} vào Stack")
        # Ngược lại nếu số phần tử trong Stack bằng với số phần tử đã giới hạn trong Stack thì in ra Stack đã đầy
        else:
            print("Stack đã đầy")
    # Hàm xóa phần tử trong Stack
    def remove_stack(self, value):
        # Thực thi xóa phần tử khỏi Stack nếu có lỗi sẽ in ra kết quả không tìm thấy giá trị trong Stack
        try:
            self.danh_sach.remove(value)
            print(f"Đã xóa phần tử {value} khỏi Stack")
        except ValueError:
            print(f"Không tìm thấy phần tử {value} trong Stack")

    # Hàm in các phần tử trong Stack
    def print_stack(self):
        print("Các phần tử trong Stack: ")
        # Sử dụng vòng lặp để in ra từng giá trị trong Stack
        for values in self.danh_sach:
            print(values)


# Tạo đối tượng Stack với giới hạn là 5 phần tử
thuc_thi = Stack(int(input("Nhập số phần tử giới hạn trong Stack: ")))

# Thực thi thêm phần tử vào Stack
while True:
    values = input("Nhập các giá trị cần thêm, cách nhau bởi dấu cách, hoặc gõ End để kết thúc: ")
    if values == "End":
        break
    for value in values.split():
        thuc_thi.push_stack(int(value))
# in Stack sau khi thêm các giá trị
print("****Sau khi thêm các phần tử vào Stack****")
thuc_thi.print_stack()

# xóa phần tử ra khỏi Stack
while True:
    values = input("Nhập các giá trị cần xóa, cách nhau bởi dấu cách, hoặc gõ End để kết thúc: ")
    if values == "End":
        break
    for value in values.split():
        thuc_thi.remove_stack(int(value))
# In các phần tử còn lại trong Stack
print("****Sau khi xóa các phần tử vào Stack****")
thuc_thi.print_stack()

# kiểm tra xem Stack đầy hay chưa (Nếu đầy trả về True và ngược lại trả về False)
print("Kiểm tra Stack đầy hay chưa: ",thuc_thi.is_full()) 
# Kiểm tra xem Stack có rỗng hay không (Nếu rỗng trả về True và ngược lại trả về False)
print("Kiểm tra Stack rỗng hay không: " ,thuc_thi.is_empty()) 








        