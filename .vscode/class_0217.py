'''변수
- 데이터 사용을 위해 메모리에 공간 할당 받아 사용'''

'''Escape 문자
- 특수한 기능 수행
- \n, \t, \", \''''

'''예제'''
# print("저의 이름은 홍길동 입니다")
# print("저의 나이는 20 살 입니다")
# print("주소는 산골자기 입니다")

# print("Have\t"
#     "a\t"
#     "good\t"
#     "Time.")

# print("1234567t"
#     "1t"
#     "12345678t"
#     "123")

'''토끼 표현 quiz'''
# print('='*30)
# print("\t\t/)/)")
# print("\t       ( ..)")
# print("\t       ( >♥")
# print("  have a good time.")
# print('='*30)

'''회비 정보 quiz'''
# print('='*70)
# print("이름\t\t나이\t전화번호\t\t회비")
# print('='*70)
# print("홍길동\t\t" "\"15\"\t" "010-123-1234\t\t" "원20,000")
# print("임꺽정\t\t" "\"20\"\t" "010-234-2345\t\t" "원30,000")
# print("김말이\t\t" "\"28\"\t" "010-345-3456\t\t" "원50,000")
# print('-'*70)
# print("총합계\t\t\t\t\t\t" "원100,000")
# print('='*70)

'''예제'''
# print(123 + 123)
# print(542 - 242)
# print(2 * 123)
# print(120 / 3)

'''예제'''
# print("덧셈 결과 : ",123 + 123)
# print("뺄셈 결과 : ",542 - 242)
# print("곱셈 결과 : ",2 * 123)
# print("나눗셈 결과 : ",120 / 3)

'''quiz'''
# print("12 + 54 =", 12+54, "입니다")
# print("268 - 42 =", 268-42, "입니다")
# print("2 * 23 =", 2*23, "입니다")
# print("120 / 3 =", 120/3, "입니다")

'''진법
- 2진수 : 범위(0~1), 표현식(0b), ex)0b0100 0001, 함수 bin(진수값)
- 8진수 : 범위(0~7), 표현식(0o), ex)0o101, 함수 oct(진수값)
- 10진수 : 범위(0~9), 표현식(), ex)65, (진수값 그 자체로 10진수로 표기됨)
- 16진수 : 범위(0~9,A-F), 표현식(0x), ex)0x41, 함수 hex(진수값)'''

'''quiz'''
# # 0b01100111, 10진수와 16진수로
# print("10진수:", 0b01100111)
# print("16진수:", hex(0b01100111))
# # 0x7d, 10진수와 2진수로
# print("10진수:", 0x7d)
# print("2진수:", bin(0x7d))
# #123, 2진수 16진수로 변환
# print("2진수:", bin(123))
# print("16진수:", hex(123))

'''서식제어문자
- %d 10진 정수
- %o 8진 정수
- %x 16진 정수
- %f 실수
- %c 단일문자
- %s 문자열'''

'''예제'''
# print(" 정수 표현 : %d" % 123)
# print(" 정수 표현 : %d" % 123.123)
# print(" 정수 표현 : %d %d" % (123,456))

# print(" \n 실수 표현 : %f" % 456)
# print(" 실수 표현 : %f" % 456.456)
# print(" 실수 표현 : %f %f" % (456.456, 123.123))

'''서식 지정'''
# print("기본 값 :%d" % 123)
# print("설정 값 :%5d" % 123)
# print("설정 값 :%05d" % 123)
# print("설정 값 :%5d%5d" % (123,123))
# print("설정 값 :%-5d%-5d" % (123,123))
# print("설정 값 :%2.1f" % 123.45678)
# print("설정 값 :%10.3f" % 123.45678)
# print("설정 값 :%20s" % "python test")

'''quiz'''
# print('='*10, "출력결과", '='*10)
# print("\n이름 : %s" % "김은섭")
# print("나이 : %d" % 29)
# print("Tel : %03d-%d-%d" % (10, 1234, 1234))
# # ^ 0으로 시작하는 숫자를 int의 함수나 %d의 일반 정수 호출 명령어로 부를수 없다
# print("키 : %.1f" % 171.5)
# print("몸무게 : %d" % 78)
# print("혈액형 : %c" % "O")

