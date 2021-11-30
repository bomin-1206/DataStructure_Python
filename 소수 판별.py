# 소수 판별하기

num = int(input())

if num<=1:
    print('Fasle')
else:
    for i in range(2,int(num**0.5)+1):  #루트 num을 의미한다
        if not num % i: # 나누어지면 수가 아니므로
            print('False')
            exit(0) # 종료

    print('True')

# def is_prime_number(x) :
# 	# 2부터 (x-1)까지의 모든 수를 확인하며
# 	for i in range(2,x) :
# 		# x가 해당 수로 나누어떨어진다면
# 		if x % i == 0 :
# 			return False # 소수가 아님
# 	return True # 소수임
#
# print(is_prime_number(4)) # 4는 소수가 아님
# print(is_prime_number(7)) # 7은 소수임