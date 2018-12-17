# -*- coding: utf-8 -*-
import logging
from pprint import pprint
from sys import stdout as STDOUT
# 6. 한 슬라이스에 start, end, stride 함께 쓰지 말자
#  - 한 슬라이스에 start, end, stride 사용하지 말자
#  - 음수 stride 가급적 사용하지 말자
#  - 한 슬라이스에 start, end, stride 모두 사용해야한다면, 2번 슬라이스 하거나 내장모듈 itertolls의 islice 사용
# Example 1
a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print(odds)  # ['red', 'yellow', 'blue']
print(evens) # ['orange', 'green', 'purple']


# Example 2
x = b'mongoose'
y = x[::-1]
print(y)  # esoognom


# Example 3
try:
    w = '謝謝'
    x = w.encode('utf-8')
    y = x[::-1]
    z = y.decode('utf-8')
except:
    logging.exception('Expected')
else:
    assert False


# Example 4
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[::2]   # ['a', 'c', 'e', 'g']
a[::-2]  # ['h', 'f', 'd', 'b']


# Example 5
a[2::2]     # ['c', 'e', 'g']
a[-2::-2]   # ['g', 'e', 'c', 'a']
a[-2:2:-2]  # ['g', 'e']
a[2:2:-2]   # []


# Example 6
b = a[::2]   # ['a', 'c', 'e', 'g']
c = b[1:-1]  # ['c', 'e']
print(a)
print(b)
print(c)