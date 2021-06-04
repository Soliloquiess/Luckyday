
# 퀴즈5 클래스를 이용한 자판기 메뉴를 표시하는 프로그램을 프로그래밍 하려고 한다.
# 다음과 같이 속성과 메서드를 정의하여라.
# 속성
# :  지역, 메뉴(튜플형태), 가격(튜플형태)
# 메소드
# : 메뉴 표시
# : 머신 실행



'''
# vm1 = Vending_machine('강남점',('아메리카노', '라떼'), (1200, 2000))
# vm1.start()

       강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원
'''


'''
# vm2 = Vending_machine('분당점',('아메리카노', '핫초코', '버블티'), (800, 1000, 2500))
# vm2.start()
       분당점 
메뉴1 : 아메리카노 /  가격 800 원
메뉴2 : 핫초코 /  가격 1000 원
메뉴3 : 버블티 /  가격 2500 원

'''


'''
# vm3 = Vending_machine('부산역점',('수박쥬스','아이스아메리카노', '카푸치노', '탄산수'), (2000, 700, 1500, 1300))
# vm3.start()

       부산역점 
메뉴1 : 수박쥬스 /  가격 2000 원
메뉴2 : 아이스아메리카노 /  가격 700 원
메뉴3 : 카푸치노 /  가격 1500 원
메뉴4 : 탄산수 /  가격 1300 원

'''


# 퀴즈 6 :
# 퀴즈 5의 자판기 머신 클래스에 금액을 투입하여
# 투입한 금액에 따라 메세지를 출력하는
# 메서드를 추가하고 실행되도록 프로그램하여라.

'''
       강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원
주문하실 메뉴의 금액을 삽입구에 넣어주세요
투입 => Yes
투입한 금액이 올바르지 않습니다. 주문이 불가능합니다.
투입 => 

'''

'''
# 예시 

       강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원
주문하실 메뉴의 금액을 삽입구에 넣어주세요
투입 => 2000
주문이 가능합니다.

'''

'''
       강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원
주문하실 메뉴의 금액을 삽입구에 넣어주세요
투입 => 500
투입 금액이 부족하여 주문이 불가능합니다.
투입구를 확인하여 주세요(환불) => 500원

'''


# 퀴즈 7 :
# 퀴즈 6의 자판기 머신 클래스에서 아래 출력 화면을
# 참조하여 메서드를 추가하고 실행되도록 하여라.
# - 투입금액에 따른 메뉴 선택
# - 메뉴 선택에 따른 메시지 출력
# - 잔돈 메시지

'''


       강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원
주문하실 메뉴의 금액을 삽입구에 넣어주세요
투입 => 1500
주문이 가능합니다.

========== 메뉴를 선택하세요 ==========
1.아메리카노   2.라떼    (환불 및 다시 시작 q)
======================================
선택 => 2
투입 금액이 부족하여 주문이 불가능합니다.


========== 메뉴를 선택하세요 ==========
1.아메리카노   2.라떼    (환불 및 다시 시작 q)
======================================
선택 => 567
선택 번호의 메뉴가 없습니다.

========== 메뉴를 선택하세요 ==========
1.아메리카노   2.라떼    (환불 및 다시 시작 q)
======================================
선택 => hhh
잘못된 입력입니다.

========== 메뉴를 선택하세요 ==========
1.아메리카노   2.라떼    (환불 및 다시 시작 q)
======================================
선택 => q
투입구를 확인하여 주세요(금액 환불) => 1500원


       강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원
주문하실 메뉴의 금액을 삽입구에 넣어주세요
투입 => 900
투입 금액이 부족하여 주문이 불가능합니다.
투입구를 확인하여 주세요(환불) => 900원


       강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원
주문하실 메뉴의 금액을 삽입구에 넣어주세요
투입 => 2000
주문이 가능합니다.

========== 메뉴를 선택하세요 ==========
1.아메리카노   2.라떼    (환불 및 다시 시작 q)
======================================
선택 => 1

=====================================
주문하신 아메리카노가 나왔습니다.
잔돈은 800원 입니다.


'''

# 자판기 클래스 완성 - 추가 기능
#  - 금액이 맞지는 않는데 음료 주문이 된다?
#  - 투입 금액에 맞는 음료만 나오게 수정
#  - 잔돈
#  - 자판기 프로그램은 무한루프로 진행
'''
#자판기 클래스 정의
class Vending_machine:
    def __init__(self,local,product,price):
        self.local = local
        self.product = product
        self.price = price

    #메뉴, 가격표시 메서드
    def show_menu(self):
        print('='*10, self.local,'메뉴를 선택하세요 ', '='*10)
        for i in range(len(self.product)):
            print(f'메뉴{i+1} : {self.product[i]} / {self.price[i]} 원')

    #투입 금액에 따른 메시지 출력 메서드
    def input_money(self):
        print('주문하실 메뉴의 금액을 입력하세요 ')
        while True:
            self.in_money = input('투입 => ').strip()
            #숫자 판별
            if self.in_money.isdigit():
                self.in_money = int(self.in_money)

                #투입금액이 메뉴의 최소금액보다 큰지 작은지
                if self.in_money >= min(self.price):
                    print('주문가능')
                    self.get_drink()
                else:
                    print('※ 주문불가 ※\t\t투입금액 환불 => ',self.in_money,'원')
            else:
                print('주문불가, 다시 투입해주세요')

    def get_drink(self):
        #메뉴출력
        print('='*40)
        for i in range(len(self.product)):
            print(str(i + 1) + '.' + self.product[i], end='    ')

        print('(환불 및 다시시작 q)\n', '='*40)
        sel = input('선택 => ').strip()

        if(sel == 'q'):
            print(f'투입금액 환불 => {self.input_money()}원')
            self.start()

        #숫자 입력 : 1~ 메뉴길이
        elif sel.isdigit():
            #올바른 메뉴선택
            if 0 < int(sel) <= len(self.product):
                print(f'주문하신 {self.product[int(sel)-1]}가 나왔습니다')
            else:
                print('선택 번호의 메뉴가 없습니다')
                self.get_drink() #재귀메서드 (자기자신 호출)
        # q, 숫자 입력도 아닌 경우
        else:
            print('잘못된 입력입니다')
            self.get_drink()

    def start(self):
            self.show_menu()
            self.input_money()


#객체 인스턴스
# vm1 = Vending_machine('강남점', ('아메리카노', '라떼'), (4300, 4600))
# vm1.start()
vm2 = Vending_machine('부산역점',('수박쥬스','아이스아메리카노', '카푸치노', '탄산수'), (2000, 700, 1500, 1300))
vm2.start()


'''
# ============================================================================
'''
    * 자료선언
    변수 < 콜렉션 (리스트, 튜플, 집합, 딕셔너리) < 함수 < 클래스 < 모듈(파일단위) < 패키지(폴더 단위)
    
    * 함수의 종류
    - 사용자정의 함수
    - 내장함수 (import 명령 X)
    - 외장함수 (import 명령 O) : random, os....

    
    * 모듈(Module)이란? 
    함수, 클래스의 집합 => 별도의 파일(*.py)로 생성
    
    * 모듈의 종류
    - 내부모듈
    : 파이썬에서 기본적으로 제공
    : datetime, time, math, random ....
    
    - 외부(외장) 모듈
    : pip/pip3(파이썬), conda(아나콘다)를 이용해서 별도 설치
    : 파이참에서는 [File]-[Settings]
          [Project Interpreter]에서 확인
    : pandas, numpy, mathplotlib, seaborn, flask ...
    
    다른 파이썬 파일에 있는 함수나 클래스 사용하고 싶다면? ▼
    - 사용자정의 모듈 : 필요에 의해서 직접 모듈로 등록한 후 사용
    
    - 설치형(빌트인) 모듈 : python, 아나콘다 설치하면 미설치 모듈
    1) 설치확인 ex:request - 웹상의 페이지를 파이썬과 연동하는 모듈(스크래핑)
        - 파이참 : [FILE] - [Setting] - Project-interpreter 항목에서 모듈 확인
        - 터미널 모드에서 명령으로 확인 : pip list
    2) 모듈 설치하기
    - 파이참 
        > [FILE] - [Setting] - Project-interpreter 에서 설치
    - 터미널 모드 
        > pip install 모듈명
        > conda install 모듈명 
    3) 설치 모듈 확인
    - flask, pymysql
    - beautifulsoup4.requests
  
'''

# 모듈의 호출방법 1
# import 모듈이름
# 모듈이름.함수(인자)
import math
print(math.sin(10))

# 모듈의 호출방법 2
# import 모듈이름 as 별칭
# 별칭.함수(인자)
import math as m
print(f'p1 = {m.pi}')
print(f'sin(10) = {m.sin(10)}')

# 모듈의 호출방법 3
# from 모듈이름 import 모듈함수
# 모듈함수(인자)
from math import sin,cos,tan
print(f'sin, cos, tan 10의 값 -> {sin(10)}, {cos(10)}, {tan(10)}')



# requests 모듈 테스트
# 방법1 -> 모듈명으로 접근 - 모듈명.함수명(인자)
# requests.get(url) => 온라인상의 웹페이지 연동
# import requests
# respons = requests.get('http://naver.com')
# print(respons.content)

# 방법2 -> 모듈명을 별칭으로 접근 - 별칭.함수명(인자)
# requests.get(url) => 온라인상의 웹페이지 연동
# import requests as r
# respons = r.get('http://naver.com')
# print(respons.content)

# 방법3
# 모듈명안의 특정함수 사용  - 함수명(인자)
# requests.get(url) => 온라인상의 웹페이지 연동
from requests import get
respons = get('http://naver.com')
print(respons.content)

# 사용자 정의 모듈 (파이썬 파일의 함수, 클래스 사용)
import test, triangle
test.testPrint()
test.HelloMessage("python")

t1 = triangle.Triangle('세모',5,10)
t1.total()

'''
    * 패키지(Package)
    모듈파일을 별도의 폴더에 저장하여 쓰는 기능
    폴더는 패키지명으로 이용
    
    패키지 생성후 함수 호출은?
    1.
    import 패키지명.모듈명
    패키명.모듈명.함수(인자)
    2.
    import 패키지명.모듈명 as 별칭
    별칭.함수(인자)
    3.
    from 패키지명.모듈명 import 함수
    함수(인자)
    
    >> 파이참에서 패키지용도의 폴더만들기
    [Project] 창에서 폴더 마우스우측버튼 -> 
    [New]-[python package] -> 
    패키지폴더가 생성되고 자동으로 __init__.py 파일(패키지폴더임을 알려주는 파일) 생성
    
    별도패키지폴더명 - AAA
    패키지안의 모듈 파일 - AAA/a.py
    모듈파일안에 함수 정의 - testPrint()
    
'''
# import AAA.a
# AAA.a.testPrint()

import AAA.a as A
A.testPrint()

from AAA.a import testPrint
testPrint()

#패키지 안에 패키지의 모듈
import BBB.BB.b
BBB.BB.b.testPrint2()


# 퀴즈 : 로또번호 생성하기
# Lotto.lotto()로 호출
# 조건 :
# 1~45 의 숫자중에서 6개로 구성
# 숫자는 중복되면 안된다.
# 로또리스트는 빈 리스트 생성
# 반복문에서
#   : 번호의 갯수가 6개라면 반복문 탈출
#   : 1~45까지 번호중에서 1개 생성
#   : 리스트안에 이미 번호가 있다면 다시 번호 생성
#   : 중복번호가 아니라면 리스트에 추가
# 로또 리스트를 출력한다.
# random.randint(star,end) : 0~숫자까지 정수난수 발생

import Custom.lotto as l
l.lottoNumber()


'''
    교재 p222
    * 오류/에러 코드
    - NameError: 함수이름, 변수, 리스트 이름등이 잘못된 경우 (변수가 없다던지 등등)
    - IndexError :  튜플,리스트의 잘못된 인덱스 접근
    - ZeroDivisionError : 0으로 나눈 경우
    - FileNotFoundError : 잘못된 파일 경로
    - ValueError : 데이터형 오류
    - TypeError : 인자로 전달되는 데이터의 타입형이 맞지 않을 떄?
    - SyntaxError(문법오류)=> 예외처리 try: ~ Except 구문에서 제외됨
    
    (튜플, 리스트 인덱스 접근시 발생되는 오류)
    - IndexError: list index out of range
    - IndexError: tuple index out of range
    
    
    * 예외처리(Exception) : 오류가 발생 시 메세지를 출력 or 오류 무시하는 기능
    - try..except 명령
    - try..except..else 명령
    - try..except..else..finally 명령
    - raise Exception : 사용자정의 에러  ex) 금칙어, 특별한 값 지정. 데이타 유효성
'''

# 0으로 나눌 시 발생되는 에러 (제로 디비전 에러)
num = int(input("숫자를 입력하세요 => "))
try:
    print(10/num) #에러 발생 대상
#제로 디비전 에러 발생 시 어떻게 처리할래? (e는 에러메시지)
except ZeroDivisionError as e:
    print('에러 발생 !!!!!!!!!', e)
    print('0으로는 나눌 수 없어요')

print('-' * 40)

# ValueError: invalid literal
try:
    ans = int(input('숫자를 입력하세요'))
    print(ans)
except ValueError as e:
    print(f'에러메세지 => {e}')
    print('입력된 값이 숫자가 아닙니다.')
