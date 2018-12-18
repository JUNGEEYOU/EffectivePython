# -*- coding: utf-8 -*-
# 11. 이터레이터를 병렬로 처리하려면 zip 사용하자.
#  - 내장 함수 zip은 여러 이터레이터를 병렬로 순회할 때 사용
#  - 파이썬 3 zip은 튜플을 생성하는 지연 제너레이터, 2는 zip 전체 결과를 튜플 리스트로 반환
#  - 길이가 다른 이터레이터를 사용 시, zip은 알아서 잘라냄
#  - 길이 상관없이 순회하기 위해선 itertools, zip_longest 사용

import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]
print(letters)


# Example 2
longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

print(longest_name)


# Example 3
longest_name = None
max_letters = 0
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)


# Example 4
longest_name = None
max_letters = 0
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)


# Example 5. 알아서 잘라냄
names.append('Rosalind')
for name, count in zip(names, letters):
    print(name)