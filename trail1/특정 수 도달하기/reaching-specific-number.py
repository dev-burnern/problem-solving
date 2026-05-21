# 1. 10개의 정수 입력 받기 (변수명 numbers 확인!)
numbers = list(map(int, input().split()))

total_sum = 0
count = 0

# 2. 조건에 따라 합계와 개수 구하기
for num in numbers:
    if num >= 250:
        break
    total_sum += num
    count += 1

# 3. 안전하게 평균 계산하기 (ZeroDivisionError 방지)
if count > 0:
    average = total_sum / count
else:
    average = 0.0

# 4. 결과 출력
print(f"{total_sum} {average:.1f}")
