import logging
from pprint import pprint
from sys import stdout as STDOUT

# 4. 복잡한 표현식 대신 헬퍼함수를 만들자

# Example 1
from urlparse import parse_qs
my_values = parse_qs('red=5&blue=0&green=',
                     keep_blank_values=True)
print(repr(my_values))


# Example 2
print('Red:     ', my_values.get('red'))
print('Green:   ', my_values.get('green'))
print('Opacity: ', my_values.get('opacity'))


# Example 3
# For query string 'red=5&blue=0&green='
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0
print('Red:     %r' % red)
print('Green:   %r' % green)
print('Opacity: %r' % opacity)


# Example 4
red = int(my_values.get('red', [''])[0] or 0)
green = int(my_values.get('green', [''])[0] or 0)
opacity = int(my_values.get('opacity', [''])[0] or 0)
print('Red:     %r' % red)
print('Green:   %r' % green)
print('Opacity: %r' % opacity)


# Example 5
red = my_values.get('red', [''])
red = int(red[0]) if red[0] else 0
green = my_values.get('green', [''])
green = int(green[0]) if green[0] else 0
opacity = my_values.get('opacity', [''])
opacity = int(opacity[0]) if opacity[0] else 0
print('Red:     %r' % red)
print('Green:   %r' % green)
print('Opacity: %r' % opacity)


# Example 6
green = my_values.get('green', [''])
if green[0]:
    green = int(green[0])
else:
    green = 0
print('Green:   %r' % green)


# Example 7. 복잡한 표현식은 헬퍼함수로 옮기고, 같은 로직을 반복해서 사용해야 한다면 헬퍼 함수를 사용하자.
# if/else 표현식을 이용하면 or나 and 같은 불 연산자를 사용할 때보다 수월
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


# Example 8
green = get_first_int(my_values, 'green')
print('Green:   %r' % green)