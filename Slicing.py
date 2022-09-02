# 필요한 정보만 가공하여 사용하는것 = slicing

social_security = "990120-1234567" # 0번째 부터 시작

print("성별 : ", social_security[7])
print("연 : ", social_security[0:2]) # 0번째 부터 2번째 직전 자리까지
print("월 : ", social_security[2:4])
print("일 : ", social_security[4:6])
print("생년월일 : ", social_security[0:6]) # [:6] 처음부터 6직전까지

print("뒤 7자리 : ", social_security[7:14]) # [7:] 7부터 끝까지
print("뒤 7자리 (뒤에부터) : ", social_security[-7:]) # 맨뒤자리수는 -1이다.

