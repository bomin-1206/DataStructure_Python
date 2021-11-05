import random #랜덤 모듈
arr=list()
#arr을 리스트로 선언
print(arr) # []가 출력, 리스트 의미

for i in range(1,10): # 10회 반복
    arr.append(random.randint(1,100))
    #arr리스트에 랜덤한 값을 넣는다.

print('*'* 40)
print(arr)
print('*'* 40)

# [문제] arr에 있는 데이터 중 가장 큰 값을 출력하시오.
arr.sort()
print(arr[-1])
# print(max(arr))

#리스트 정렬
arr.sort()
print(arr)

# [문제] 정렬된 리스트 두 번쨰 값을 출력하시오.
print(f'리스트 두 번쨰 값 :  {arr[1]}')