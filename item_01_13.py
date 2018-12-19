# -*- coding: utf-8 -*-
# 13. try/except/else/finally 에서 각 블록의 장점을 이용하자.
#  - try/finally 복합문을 이용하면, try 블록에서 예외 발생 여부와 상관없이 정리 코드를 실행할 수 있다.
#  - else 블록: try 블록에 있는 코드의 양을 최소로 불이는 데 도움을 주며 try/except 블록과
#              성공한 경우 실행할 코드를 시각적으로 구분 가능
#  - else 블록: try 블록의 코드가 성공적으로 실행된 후, finally 블록에서 공통 정리 코드를 실행하기 전에 추가 작업을 하는 데 사용

import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
handle = open('random_data.txt', 'w')
handle.write('success\nand\nnew\nlines')
handle.close()

handle = open('random_data.txt')  # May raise IOError
try:
    data = handle.read()  # May raise UnicodeDecodeError
finally:
    handle.close()        # Always runs after try:


# Example 2
import json

def load_json_key(data, key):
    try:
        result_dict = json.loads(data)  # May raise ValueError
    except ValueError as e:
        raise KeyError
    else:
        return result_dict[key]         # May raise KeyError

# JSON decode successful
assert load_json_key('{"foo": "bar"}', 'foo') == 'bar'
try:
    load_json_key('{"foo": "bar"}', 'does not exist')
    assert False
except KeyError:
    pass  # Expected

# JSON decode fails
try:
    load_json_key('{"foo": bad payload', 'foo')
    assert False
except KeyError:
    pass  # Expected


# Example 3
import json
UNDEFINED = object()

def divide_json(path):
    handle = open(path, 'r+')   # May raise IOError
    try:
        data = handle.read()    # May raise UnicodeDecodeError
        op = json.loads(data)   # May raise ValueError
        value = (
            op['numerator'] /
            op['denominator'])  # May raise ZeroDivisionError
    except ZeroDivisionError as e:
        return UNDEFINED
    else:                       # 성공한 경우 실행
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)    # May raise IOError
        return value
    finally:
        handle.close()          # Always runs

# Everything works
temp_path = 'random_data.json'
handle = open(temp_path, 'w')
handle.write('{"numerator": 1, "denominator": 10}')
handle.close()
assert divide_json(temp_path) == 0.1

# Divide by Zero error
handle = open(temp_path, 'w')
handle.write('{"numerator": 1, "denominator": 0}')
handle.close()
assert divide_json(temp_path) is UNDEFINED

# JSON decode error
handle = open(temp_path, 'w')
handle.write('{"numerator": 1 bad data')
handle.close()
try:
    divide_json(temp_path)
    assert False
except ValueError:
    pass  # Expected