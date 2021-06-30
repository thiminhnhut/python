"""
Author: Thi Minh Nhut <thiminhnhut@gmail.com>
Date: 2021-06-30 09:56:12
Title: get_class_name.py
"""


class Student:
    """
    Class Student
    """

    def __init__(self, name):
        self.name = name


def main():
    """
    Main function
    """
    student = Student("Thi Minh Nhut")
    print(student.__class__.__name__)


if __name__ == "__main__":
    main()
