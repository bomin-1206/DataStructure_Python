def is_prime_number(x) :
	# 2부터 (x-1)까지의 모든 수를 확인하며
	for I in range(2,x) :
		# x가 해당 수로 나누어떨어진다면
		if x % I == 0 :
			return False # 소수가 아님
	return True # 소수임

print(is_prime_number(4)) # 4는 소수가 아님
print(is_prime_number(7)) # 7은 소수임