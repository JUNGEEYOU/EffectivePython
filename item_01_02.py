# 2. PEP 8 스타일 가이드를 따르자.

# 1. 화이트 스페이스 :
# - 스페이스 4개  들여 쓰기 , tab x
# - 함수와 클래스는 빈줄 2개로 구분
# - 클래스에서 매서드는 빈 줄 1개
# - 리스트 인덱스, 함수 호출, 키워드 인수 할당에는 스페이스 사용 안함
# - 변수 할달 앞뒤에는 스페이스 한번
# - 한줄의 문자 길이는 79 이내, 만약 길어져 다음줄로 가야하면 들여쓰기 4개 사용


# 2. 명명
# - 함수, 변수, 속성은 lowrcase_underscore
# - 보호 : _leading_underscore
# - 비공개: __double_leading_underscore
# 클래스&예외: CapitalizedWord
# 모듈 수준 상수: ALL_CAPS
# 클래스의 인스턴스 메서드: 첫 번째 파라미터의 이름을 self
# 클래스의 메서드: 첫 번째 파라미터의 이름을 cls로 지정


# 3. 표현식과 문장
# - if not a is b  > if a is not b
# - 길이 확인(if len(some) == 0)이나 빈값 확인 하지 않고 > if not somelist or if somelist
# - 한 줄로 된 if문, for, while, except 복합문 사용 하지 말고 여러 줄로 나눠서 사용
# - 항상 파일의 맨 위는 import
# - import foo 아닌 > from bar import foo
# - 임포트 순서: 표준 라이브러리 > 서드파티 모듈 > 자신이 만든 모듈 순