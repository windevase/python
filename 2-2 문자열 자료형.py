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