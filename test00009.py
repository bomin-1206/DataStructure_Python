# [문제] 리스트에 주어진 알파벳을 오름차순 정렬하라.
arr =['b','c','a','f','t','e']
arr.sort()
print(arr)
print(arr[2])
print(len(arr)) #배열, 리스트의 길이

# [문제] 리스트 요소 중 아스키 코드값이 가장 큰 알파벳을 출력하시오.
arr=['b','c','a','f','t','e']
arr.sort()
print(arr[-1])

# arr.sort(reverse=True) # 내림차순으로 정렬
# print(arr[0])

# print(arr[len(arr)-1])

# [문제] 주어진 점수 리스트에서 최고점과 최저점을 출력하시오.
score = [55, 78, 99, 34, 87]
score.sort()
print(score[-1], score[0]) #최고점, 최저점

# print(score[-1]) #최고점
# print(score[0]) #최저점

print(max(score)) #최고점
print(min(score)) #최저점