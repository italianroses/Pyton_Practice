# 집합(set)
# 중복 안됨 , 순어 없음

my_set = {1,2,3,3,3}

print(my_set) # 중복 무시 따라서 3 중복 무시

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 출력

print(java&python)
print(java.intersection(python))

# 합집합 (java and pyhton 모두 할수있는 사람)

print(java | python)
print(java.union(python)) # 순서 없음

# 차집합(java 는 가능 python 불가능 출력)

print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java 를 잊어먹음

java.remove("김태호")
print(java)