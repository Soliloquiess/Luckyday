'''
        2020.11.12 수업
'''

'''
    절차지향 - c
    객체지향 - java, javascript, c++, c#, python(어정쩡한 객체지향)

    * 클래스 (설계도/틀) => 붕어빵틀
    - 기본자료형(숫자, 문자열, 불른)
    - 콜렉션형 (리스트, 집합, 튜플, 딕셔너리)
    - 클래스 ( 속성, 함수 ...) => 틀
    
    * 인스턴스=객체=Object (객체) => 붕어빵
    - 클래스에 의해서 만들어진 산출물
    
    클래스 생성 문법 (클래스이름은 첫글자는 대문자로 지정) ▼
    class 클래스명:
      명령문
      
    클래스 메소드란? => 동작/ 기능
    def 메소드이름(self,인자):
       명령어
       return 값
    메소드 호출은 인스턴스명.메소드이름(인자)
'''

# 자동차 클래스
class Car:
    pass

# 버스 클래스
class Bus:
    pass

# 인스턴스 생성
car1 = Car()
bus1 = Bus()
print(car1, type(car1))
print(bus1, type(bus1))

# 인스턴스가 클래스에 의해 생성 됐니? True, False 반환
# isinstance(인스턴스 변수, 클래스 명)
print(isinstance(car1,Car))
print(isinstance(bus1, Car))
print(isinstance(bus1, Bus))


'''
    * 생성자 함수 (Constructor)

    생성자함수 문법 ▼
    class 클래스명:
      def __init__(self, 인자):
          self.인자 = 인자값
          self.인자 = (인자값1, 인자값2,...) # 튜플형태 
'''
# 사각형 클래스 정의 // 속성- 가로,세로, 색상, 스타일
class Square:
    #생성자 함수 선언
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.style = '줄무늬'
        self.maker = ('영희','철수','미미')

    # 속성 출력 클래스 메서드(함수 개념) 정의
    def printInfo(self):
        print(f' square1 color = {self.color} ')
        print(f' square1 width = {self.width} ')
        print(f' square1 height = {self.height} ')
        print(f' square1 style = {self.style} ')
        print(f' square1 maker = {self.maker} ')
        print('*'*40)

    # 사각형 넓이 반환 클래스 메서드 정의
    def area(self):
        return self.width * self.height


square1 = Square(50, 100, 'Red')
square2 = Square(30, 30, 'Yellow')

# 인스턴스 각 속성 출력
print(f'스퀘어1의 가로: {square1.width} == 스타일: {square1.style} == 일꾼: {square1.maker[-1]}')

# 속성 출력하는 클래스 메서드 호출
square1.printInfo()
square2.printInfo()

# 넓이 구하는 클래스 메서드 호출
print(f' square1 넓이 : {square1.area()}')
print(f' square2 넓이 : {square2.area()}')



#Bread 클래스 생성
class Bread:
    def __init__(self,kind, price, kcal, src, brand):
        self.kind = kind
        self.price = price
        self.kcal = kcal
        self.src = src
        self.brand = brand

    # 속성 출력 메서드
    def breadprint(self):
        print(f'Bread 클래스 속성 => 종류({self.kind}), 가격({self.price}), '
              f'\n칼로리({self.kcal}), 재료({self.src}), 브랜드({self.brand}) ')

    # 계산 메서드
    def culculate(self, count):
        print('*'*10 , ' 주문내역 ','*'*10  )
        print(f'{self.kind}(을/를) {count}개 주문하셨습니다')
        print(f'주문가격 => {self.price * count}')

bread = Bread('식빵',4500,'1080',('밀가루','버터','설탕'),'뚜레쥬르')
bread.breadprint()
print()
bread.culculate(5)
