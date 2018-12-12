import logging
from pprint import pprint
from sys import stdout as STDOUT
# 5. 시퀀스를 슬라이스하는 방법을 알자.

# Example 1. 너무 장황하지 않게 하자. start에 0를 설정하거나 end 에 길이 설정하지 말자.
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First four:', a[:4])
print('Last four: ', a[-4:])
print('Middle two:', a[3:-3])


# Example 2
assert a[:5] == a[0:5]


# Example 3
assert a[5:] == a[5:len(a)]


# Example 4
print(a[:5])
print(a[:-1])
print(a[4:])
print(a[-3:])
print(a[2:5])
print(a[2:-1])
print(a[-3:-1])


# Example 5
# a[:]      # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# a[:5]     # ['a', 'b', 'c', 'd', 'e']
# a[:-1]    # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# a[4:]     #                     ['e', 'f', 'g', 'h']
# a[-3:]    #                          ['f', 'g', 'h']
# a[2:5]    #           ['c', 'd', 'e']
# a[2:-1]   #           ['c', 'd', 'e', 'f', 'g']
# a[-3:-1]  #                          ['f', 'g']


# Example 6. 슬라이싱은 범위를 벗어난 인덱스 허용
first_twenty_items = a[:20]
last_twenty_items = a[-20:]


# Example 7.하지만 직접 접근은 안됨
try:
    a[20]
except:
    logging.exception('Expected')
else:
    assert False


# Example 8
b = a[4:]
print('Before:   ', b)
b[1] = 99
print('After:    ', b)
print('No change:', a)


# Example 9. 지정한 범위에 대체하고 남은 자리는 줄임 , 자리가 없으면 늘림
print('Before ', a)
a[2:7] = [99, 22, 14]
print('After  ', a)


# Example 10
b = a[:]
assert b == a and b is not a


# Example 11
b = a
print('Before', a)
a[:] = [101, 102, 103]
assert a is b           # Still the same list object
print('After ', a)      # Now has different contents