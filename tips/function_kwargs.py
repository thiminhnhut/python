"""
Author: Thi Minh Nhut <thiminhnhut@gmail.com>
Date: 2021-06-30 10:23:08
Title: function_kwargs.py
"""
# python -m tips.function_kwargs


def my_sum(*kwargs):
    """
    Test python function multiple arguments
    """
    s = 0
    for value in kwargs:
        s += value
    return s


if __name__ == "__main__":
    print(my_sum(1, 2, 3))
