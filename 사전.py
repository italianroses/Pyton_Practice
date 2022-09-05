# 키는 3번 value는 유재석
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# print(cabinet[5]) # 해당되는 값이 없으면 error

print(cabinet.get(5))
print("hi")

print(cabinet.get(5, "사용가능"))
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-100" : " 유재석", "B-100" : "박명수"}
print(cabinet["A-100"])
print(cabinet)

# 새 손님

cabinet["A-100"] = "김종국" # 기존 유재석 제거
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-100"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# Value 들만 출력
print(cabinet.values())

# Key 와 Value 모두 출력
print(cabinet.items())

# 폐점
cabinet.clear()
print(cabinet)