# -*- coding: utf-8 -*-
# 9. 컴프리헨션이 클때는 제너레이터 표현식을 고려하자
#  - 리스트 컴프리헨션은 큰 입력을 처리할 때 너무 많은 메모리를 소모해서 문제를 일으킬수 있음
#  - 제너레이터 표현식은 이터레이터로 한 번에 한 출력만 만드므로 메모리 문제 피할 수 있음
#  - 한 제너레이터 표현식에서 나온 이터레이터를 또 다른 제너레이터 표혁식의 for 서브 표현식으로
#    넘기는 방식으로 제너레이터 표현식을 조합 가능
#  - 제너레이터 표현식은 서로 연결되어 있을 때 매우 빠르게 실행
import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
import random
with open('my_file.txt', 'w') as f:
    for _ in range(10):
        f.write('a' * random.randint(0, 100))
        f.write('\n')

value = [len(x) for x in open('my_file.txt')]
print(value)


# Example 2
it = (len(x) for x in open('my_file.txt'))
print(it)


# Example 3
print(next(it))
print(next(it))


# Example 4
roots = ((x, x**0.5) for x in it)


# Example 5
print(next(roots))
