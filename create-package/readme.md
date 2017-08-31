# Hướng dẫn cách tạo một Package trong ngôn ngữ lập trình Python

* **Thực hiện:** Thi Minh Nhựt - **Email:** thiminhnhut@gmail.com

* **Thời gian:** Ngày 31 tháng 08 năm 2017

## Nguồn tham khảo

* [How to Create a Python Package](http://pythoncentral.io/how-to-create-a-python-package/)

## Nội dung

### Giới thiệu

Khi có một số lượng lớn các lớp (class) hoặc các module trong Python, chúng ta cần sắp xếp chúng thành một gói (package). Khi có số lượng các module (đơn giản mỗi file chứa một class) trong khi phát triển bất kỳ một dự án đáng kể, công việc cần thiết là tổ chức chúng thành các package - đặt các module/class có chức năng tương tự nhau trong cùng một thư mục.

### Các bước tạo một Package trong Python

Gồm các bước sau đây:

1. Tạo thư mục và đặt tên thư mục là tên của package.

2. Đặt các class đã tạo vào trong thư mục này.

3. Tạo thêm một file `__init__.py` trong thư mục này.

File `__init__.py` thực sự cần thiết vì Python sẽ biết thư mục chứa file `__init__.py` là một package.

### Ví dụ về cách tạo một Package trong Python

* Yêu cầu: Tạo một package có tên là `Animals`: gồm 2 module `Mammals` và `Birds` với 2 class tương ứng là `Mammals` và `Birds`.

* Các bước thực hiện:

    + **Bước 1:** Tạo thư mục package với tên là `Animals`.
    
    + **Bước 2:** Lần lượt tạo 2 file `Mammals` và `Birds` chứa các lớp `Mammals` và `Birds` có nội dung tương ứng như sau:
        
        - Nội dung của file `Mammals.py`: [Mammals.py](https://github.com/thiminhnhut/python/blob/master/create-package/Animals/Mammals.py)
        
        ```python
         class Mammals:
            def __init__(self):
                ''' Constructor for this class. '''
                # Create some member animals
                self.members = ['Tiger', 'Elephant', 'Wild Cat']
                
            def printMembers(self):
                print('Printing members of the Mammals class')
                for member in self.members:
                    print('\t%s ' % member)
        ```
        
         - Nội dung của file `Birds.py`: [Birds.py](https://github.com/thiminhnhut/python/blob/master/create-package/Animals/Birds.py)
        
        ```python
         class Birds:
            def __init__(self):
                ''' Constructor for this class. '''
                # Create some member animals
                self.members = ['Sparrow', 'Robin', 'Duck']
                
            def printMembers(self):
                print('Printing members of the Birds class')
                for member in self.members:
                   print('\t%s ' % member)
        ```
    + **Bước 3:** Thêm vào file `__init__.py` với nội dung như sau:
    
        ```python
        from Mammals import Mammals
        from Birds import Birds
        ```
    + Sau 3 bước thực hiện đã tạo thành công package với tên `Animals`, tiến hành kiểm tra package vừa tạo ra:
        
        - Tạo một file `test.py` và đặt cùng cấp với thư mục `Animals`.
        
        - Nội dung của file `test.py`: [test.py](https://github.com/thiminhnhut/python/blob/master/create-package/test.py)
        
        ```python
        # Import classes from your brand new package
        from Animals import Mammals
        from Animals import Birds
        
        # Create an object of Mammals class & call a method of it
        myMammal = Mammals()
        myMammal.printMembers()
        
        # Create an object of Birds class & call a method of it
        myBird = Birds()
        myBird.printMembers()
        ```
        
        - Khi thực thi tự động tạo ra các file `.pyc` và kết quả là:
        
        ```bash
        $ ls
        Animals                test.py
        
        $ python test.py
        Printing members of the Mammals class
	        Tiger 
	        Elephant 
	        Wild Cat 
        Printing members of the Birds class
	        Sparrow 
	        Robin 
	        Duck
        ```
