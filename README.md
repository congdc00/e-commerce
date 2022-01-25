# Dự án drone delivery
## Giới thiệu
Đây là dự án về bài toán giao hàng bằng drone với các chức năng được xây dựng từ giao diện cho đến phần giao hàng tới tay người dùng, bao gồm các thành phần
* Các chức năng AI phục vụ mục đích vận chuyển hàng
* Website bán hàng 
## Tài liệu
Các tài liệu đi kèm được lưu trữ tại [Drive](https://drive.google.com/drive/folders/1TVq7Tfm4zC5uZw7qKQdM0sZjZI-KzRoR?usp=sharing)
## Các công cụ cần thiết
1. Pycharm
2. DataSpell
3. DataGrip
4. Webstorm
## Hướng dẫn chạy
* Phần UI  
Bước 1: vào terminal và gõ `pip install library` để cài đặt các thư viện cần thiết  
Bước 2: mở terminal tại địa chỉ ui/e-commerce gõ python manage.py runserver  
* Phần AI  
Khi đã có 50 thu thập được như trong tài liệu đính kèm có hướng dẫn thì tiến hành  
Bước 1: Mở thư mục ai\client_recoginition và chạy file extract_face.ipynb để trích xuất embedding   
Bước 2: Tại cùng thư mục đó chạy file live_recoginittion.ipynb để hiển thị ra các chức năng về human pose và face recognition   
