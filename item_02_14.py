# -*- coding: utf-8 -*-
# 14. None을 반환하기 보다는 예외를 일으키자.
#  - 특별한 상황을 알릴때 none이 아닌 예외 일으키자, None은 flase로 평가되어 문제가 될 수 있다.

import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# assert divide(4, 2) == 2
# assert divide(0, 1) == 0
# assert divide(3, 6) == 0.5
# assert divide(1, 0) == None


# Example 2
x, y = 1, 0
result = divide(x, y)
if result is None:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)


# Example 3
x, y = 0, 5
result = divide(x, y)
if not result:
    print('Invalid inputs')  # This is wrong!
else:
    assert False


# Example 4
def divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


# Example 5
x, y = 5, 0
success, result = divide(x, y)
if not success:
    print('Invalid inputs')


# Example 6
x, y = 5, 0
_, result = divide(x, y)
if not result:
    print('Invalid inputs')  # This is right

x, y = 0, 5
_, result = divide(x, y)
if not result:
    print('Invalid inputs')  # This is wrong


# Example 7
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs')


# Example 8
x, y = 5, 2
try:
    result = divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)