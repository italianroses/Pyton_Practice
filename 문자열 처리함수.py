

python = "Python is Amazing"

print(python.lower()) # lower()는 앞을 소문자로
print(python.upper()) # upper()는 앞을 대문자로
print(python[0].isupper()) #.isupper 는 []자리수의 문자가 대문자인지 확인시켜줌
print(len(python)) # len()의 문자길이를 판별시켜준다.
print(python.replace("Python", "Java")) # 함수.replace("문구1","문구2") 문구1과 문구2를 바꿔서 출력해준다.


index = python.index("n")
print(index) # python 속 n이 몇번째 존재하는가

index = python.index("n", index +1) # 두번째 n의 위치찾기
print(index)


print(python.find("n")) # n찾는 문자열

print(python.find("Java")) # 만약 찾는 문자열이 없다면 -1 을 반환한다.
# print(python.index("Java")) index는 오류발생

# error 발생 뒤에는 처리 진행 X

print(python.count("n")) # n의 등장수를 계산

