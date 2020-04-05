'''변수'''

'''quiz'''
# python=100
# age=27
# print('파이썬', python)
# print('나는', age)

# python=int(input("파이썬 점수:\n"))
# c=int(input("C언어 점수:\n"))
# java=int(input("Java 점수:\n"))

# sum=python + c + java
# ave=python + c + java/3
# print("3과목의 합계 : %d \n3과목의 평균 : %.2f" % (sum,ave))

'''예제'''
# flt= 123.567
# print("round(flt) : " , round(flt))
# print("round(flt,1)" , round(flt,1))
# print("round(flt,2) : " , round(flt,2))

'''quiz'''
# height=260
# floors=14
# first_height=500.23
# total_hegiht=first_height+((floors-1)*height)

# print("총 높이: %.3f" % (total_hegiht/100))
# print("총 높이:", round(total_hegiht/100,3))

'''비례식 퀴즈 quiz
-전동자전거로100m를가는데11.27초가걸린다면1시간후몇km를갈수있을까?(소수점2자리까지만표기하시오)'''
#비례식 같은 수학적 개념은 원리를 이해해야 코딩에 적용가능
#a:b=ma:mb=c:d(여기서 m은 증감시킬 값)

# km1=0.1
# second1=11.27
# second2=3600
# change_factor=second2/second1
# km2=change_factor*km1

# print("1시간 뒤에 이동한 거리:", round(km2,2))

'''예제'''
# str_1 = "python "; str_2 = "test"; #str_3 = str_1 + str_2
# print("%s + %s = %s" % (str_1,str_2,str_1+str_2))
# print(str_1,"+",str_2,"=",str_1+str_2)

'''Type
- 변수의 자료형 확인'''
# num1=100
# print("type : %s, \tid : %d" % (type(num1),id(num1)))
# num2="A"
# print("type : %s, \tid : %d" % (type(num2),id(num2)))
# num3=123.123
# print("type : %s, \tid : %d" % (type(num3),id(num3)))

'''예제'''
# st1 = "Python"
# st2 = "Test"
# su= 100
# flt= 1.11
# num= '100'
# print(flt+su)
# print(st1 + st2)
# #print(su+num), int와 str은 덧셈할수없다

'''quiz'''
# su=100
# num='100'
# flt="1.111"
# print(su+su)
# print(int(num)+float(flt))
# print(num+num)
