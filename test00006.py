#매개변수 한 개인 함수 만들어보자.

# def Hello(name):
#     print('Hi', name)
#
# Hello('bomin')
#
# def Hello1(name):
#     print(f'Hello, {name}') #f-strubg 방식으로 출력, f 접두사
#     # python 3.6 version 이상
#
# def Hello2(name, hobby):
#     print(f'Hi My name is {name}, My hobby is {hobby}')
#     # print(f'Hi, My name is {name}'\ # 여러줄 연결
#     #       f' My hobby is {hobby}')
#
# Hello1('bomin')
# Hello2('bomin', 'listen to music')

#[문제] 매개변수로 넘긴 문자열 3개를 출력하는 프로그램을 만들어보시오.

def info(name, address, phone): #이름 주소 전화번호
    print(f'제 이름은 {name}이고, 주소는 {address}입니다.'\
          f'제 전화번호는 {phone}에요')

info('강보민', '대구시 달성군', '010-1234-5678') # 실행해 보기

# [기초 문제] Hello() 함수에 'bomin'과 17 숫자를 매개변수 값으로 넘겨줄 때
# 'Hi, bomin, You are 17 years old.'이 출력되도록 하시오.
# Hello('bomin', 17)

def Hello(name, age):
    print(f'Hi, {name} You are {age} years old')

Hello('bomin',17)

# [문제] 자신이 좋아하는 가수 이름을 3개 입력(input())받고, 출력하는 함수 만들기
# 함수이름 : singer(a,b,c)
def singer(a,b,c):
    print(f'내가 좋아하는 가수 {a},{b},{c}입니다.')
    # print('내가 좋아하는 가수', a,b,c, '입니다.')


a = input('첫 번째 좋아하는 가수 : ')
b = input('두 번째 좋아하는 가수 : ')
c = input('세 번째 좋아하는 가수 : ')

singer(a, b, c)