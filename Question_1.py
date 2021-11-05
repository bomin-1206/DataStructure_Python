#[문제]
#숫자 1개를 입력받아 1부터 그 수까지 짝수의 곱을 구해보자.

n=int(input())
s=1
for i in range(1,n+1) :
    if i%2==0:
        s*=i

print(s)