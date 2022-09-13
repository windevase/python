# 문자열에 ' 포함
a = "Python's favorite food is perl"
print(a)

# 문자열에 " 포함
b = '"Python is very easy." he says.'
print(b)

# 백슬래시\를 사용하여 문자열에 '와 " 포함
food = 'Python\'s favorite food is perl'
print(food)

say = "\"Python is very easy.\" he says."
print(say)

#줄을 바꾸는 이스케이프 코드 /n 삽입
multiline = "Life is too short\nYou need python"
print(multiline)

#연속된 ''' 또는 """ 사용하기
multiline = '''
Life is too short
You need python
'''
print(multiline)

multiline = """
Life is too short
You need python
"""
print(multiline)


#문자열 연산하기

#1. 문자열 더해서 연결하기(Concatenation)
head="Python"
tail=" is fun!"
print(head+tail)

#2. 문자열 곱하기
a="python"
print(a*2)

#3. 문자열 곱하기 응용
print("="*50)
print("My Program")
print("="*50)

#4. 문자열 길이 구하기
a = "Life is too short"
print(len(a))

#응용 문제
a="You need Python"
print(len(a))


#문자열 인덱싱과 슬라이싱

#문자열 인덱싱이란?
# Life is too short, You need Python
# 0123456789012345678901234567890123
a = "Life is too short, You need Python"
print(a[3])

#파이썬은 0부터 숫자를 센다

print(a[0])
print(a[12])
print(a[-1])
print(a[-0])

print(a[-2])
print(a[-5])


#문자열 슬라이싱
a = "Life is too short, You need Python"
b = a[0]+a[1]+a[2]+a[3]
print(b)

print(a[0:4])
#슬라이싱 기법은 끝번호에 해당하는 것은 포함하지 않는다.
print(a[0:3])

#문자열을 슬라이싱하는 방법
print(a[0:5]) #공백이 포함되면 다른 문자열이다

#시작 번호가 0일 필요는 없다
print(a[0:2])
print(a[5:7])
print(a[12:17])

#시작 번호에서 끝 번호 부분을 생략하면 시작 번호부터 끝까지 출력
print(a[19:])

#시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 뽑아낸다
print(a[:17])

#시작 번호, 끝 번호를 생략하면 문자열의 처음부터 끝까지 출력
print(a[:])

# Life is too short, You need Python
# 0123456789012345678901234567890123

#슬라이싱에서도 인덱싱과 마찬가지로 - 기호를 사용할 수 있다.
print(a[19:-7])
#위 소소코드에서 a[19]에서부터 a[-8]까지를 말한다.


#슬라이싱으로 문자열 나누기
# 20010331Rainy
# 0123456789012
a="20010331Rainy"
date=a[:8]
weather=a[8:]
print(date)
print(weather)

a="20010331Rainy"
year=a[:4]
day=a[4:8]
weather=a[8:]
print(year)
print(day)
print(weather)


# Pithon이라는 문자열을 Python으로 바꾸려면?
# 문자열의 요솟값은 바꿀 수 없다. immutable
a="Pithon"
print(a[:1])
print(a[2:])
print(a[:1]+'y'+a[2:])


#문자열 포매팅
number=3
a="I eat %d apples." % number
print(a)

string='five'
a="I eat %s apples." % string
print(a)

number=10
day="three"
a="I eat %d apples. so I was sick for %s days" % (number, day)
print(a)

# %s  문자열 string
# %c  문자 1개 character
# %d  정수 Integer 
# %f  부동 소수 Floatingpoint 
# %o  8진수
# %x  16진수
## %% Liberal 문자 '%'자체

# %s 포맷은 어떤 형태의 값이든 변환해 넣을수 있다. 문자열로 변환
a="I have %s apples" % 3
print(a)

a="rate is %s" % 3.234
print(a)

#포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
a="Error is %d%%" % 98
print(a)


#포맷 코드와 숫자 함께 사용하기
#1. 정렬과 공백
a="%10s" % "hi"
print(a)
#         hi
# 0123456789
# 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고
# 그 앞의 나머지는 공백으로 남겨두라는 의미이다.

a="%-10sjane" % "hi"
print(a)
# hi        jane
# 0123456789
# hi를 왼쪽으로 정렬하고 나머지는 공백으로 채움


#2. 소수점 표현하기
a="%0.4f" % 3.42134234
print(a)
#소수점 네 번째 자리까지만 나타냄

a="%10.4f" % 3.42134234
print(a)
# 소수점 네 번째 자리까지만 표시하고 
# 전체 길이가 10개인 문자열 공간에서 오른쪽으로 정렬
#     3.4213
# 0123456789


#format 함수를 사용한 포매팅
#숫자 바로 대입하기
a="I eat {0} apples".format(3)
print(a)

#문자열 바로 대입하기
a="I eat {0} apples".format("five")
print(a)

#숫자 값을 가진 변수로 대입하기
number=3
a="I eat {0} apples".format(number)
print(a)