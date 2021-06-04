'''
        2020.11.13(금) 수업
'''

# 고양이 클래스 (저번 수업 복습)
class Cat:
    def __init__(self, kind, gender, age,name):
        self.kind = kind
        self.gender = gender
        self.age = age
        self.name = name
        self.animalKind = '고양이'

    def sleep(self, where):
        print(f'{self.animalKind} {self.name}가 {where}에서 잠을 잔다')

    def eat(self, food):
        print(f'{self.animalKind} {self.name}가 {food}(을/를) 먹는다')

    def run(self):
        print(f'{self.animalKind} {self.name}가 달린다')

    def catprint(self):
        print(f'{self.age}살의 {self.animalKind} {self.name}(은/는) {self.kind} 종류이고 성별은 {self.gender} 입니다.')

    #정의된 메서드를 이용해 메서드 정의, 정의된 메서드 호출 가능 => self.메서드명(인자)
    def actionPrint(self):
        print(f'*** 우리 {self.animalKind} {self.name}는요 ***')
        self.catprint()
        self.sleep('서울숲 잔디밭 위')
        self.eat('츄르')
        self.run()

cat1 = Cat('삼색이', '여', 10, 'nabi')
cat2 = Cat('스콧', '남', 5, 'haha')
cat1.actionPrint()
cat2.actionPrint()


# 퀴즈 1
# 삼각형 클래스를 다음과 같은 속성과 메서드로 정의하여라
# 속성(이름, 밑변, 높이)
# 메서드1 - 속성 출력
# 메서드2 - 삼각형의 넓이 출력
# 삼각형의 면적 구하는 공식 = (밑변의길이 * 높이)/2

class Triangle:
    def __init__(self, name, under, height):
        self.name = name
        self.under = under
        self.height = height

    def triangle_print(self):
        print(f'이름 = {self.name}\n밑변 = {self.under}\n높이 = {self.height}')

    def triangle_area(self):
        print('*'*40)
        print(f'삼각형의 넓이 = {(self.under * self.height)/2}')
        print('*' * 40)

    def total(self):
        self.triangle_print()
        self.triangle_area()
        print()

# 퀴즈 2
# 퀴즈1의 삼각형 클래스를 이용하여 인스턴스 객체를 생성하고 메서드를 호출하여라
triangle1 = Triangle('triangle1', 10, 5 )
triangle2 = Triangle('triangle2',35,27)
triangle1.total()
triangle2.total()

'''
    * 클래스 변수 : 클래스 정의시 지정된 공용 변수로 생성자 함수 위에 정의, 동일한 주소값 가짐
   
    id(객체이름) : 주소 표시
    인스턴스 생성후 접근
    - 인스턴스명.클래스변수명
    - 클래스명.클래스변수명

'''

class Test:
    #클래스 변수 = 공용변수 (생성자 함수 안에 정의 X, 클래스 안에 별도로 정의)
    msg = 'Hello World'
    
    #생성자 함수 = 속성 정의
    def __init__(self, color):
        self.name = 'test class'
        self.color = color

    def print_info(self):
        print(f'{self.name}, {self.color}, {self.msg}')

#객체 인스턴스화
test1 = Test('파랑')
test1.print_info()  #인스턴스명.클래스변수명
print(test1.msg)    #클래스명.클래스변수명

#클래스 변수와 인스턴스 변수 msg는 같은 주소인가? => YES



print()
'''
    * 상속 : 부모클래스의 속성이랑 메소드를 그대로 가짐, 다중상속 가능, 코드 재사용의 장점
    class 클래스이름(부모클래스1,부모클래스2...)
    
    부모클래스1 - 아파트, 차
    부모클래스2 - 오피스텔, 전동스쿠터
    자식클래스 - 아파트, 차 , 오피스텔, 전동스쿠터
    
    부모클래스를 상속해서 자식 클래스 만들기
    class 자식클래스명(부모클래스명1, 부모클래스명2....):
      명령문
'''


# 부모 클래스1 생성
class Papa:
    def __init__(self):
        self.firstName1 = '홍'

    def info1(self):
        print('Papa - 아파트, 차')
    def test1(self, msg):
        print(f'Papa test1 method call => {msg}')


# 부모 클래스2 생성
class Mama:
    def __init__(self, firstname2):
        self.firstName2 = firstname2

    def info2(self):
        print('Mama - 오피스텔, 전동스쿠터')


# 2개의 클래스를 상속받은 자식 클래스 생성
class Child(Papa, Mama):

    #생성자 함수 정의
    def __init__(self):

        #부모클래스 속성 사용할 수 있게 생성자 함수 정의 => 부모클래스명.__init__(self)
        Papa.__init__(self)
        Mama.__init__(self,firstname2='')

        #부모클래스와 상관없는 새로운 속성 정의
        self.myname='진'

    def info3(self ):
        print('Child - 자전거, 노트북')


# 부모 클래스 객체 인스턴스화
papa1 = Papa()
print(papa1.firstName1)
papa1.info1()
print('-'*30)

mama1 = Mama('서')
print(mama1.firstName2)
mama1.info2()
print('-'*30)

# 자식클래스 객체 인스턴스화
child1 = Child()
papa1 = Papa()

# 자식클래스가 부모 클래스의 메서드와 속성을 호출할 수 있다.
child1.info1()
child1.info2()
child1.info3()


# papa1.test1('상위 클래스 메소드 입니당')
# child1.test1('하위 클래스로 상위 클래스의 메소드 출력합니당')
# #print(child1.firstName1, child1.firstName2(), child1.myname)
# print('-'*30)


print()


# 클래스 Animal과  Animal 클래스를 상속받는 Dog 클래스를 정의해라
# 위에서 정의한 클래스를 이용하여 다음과 같이 출력되도록 객체 인스턴스화하고 메서드를 호출하여라.
'''
종류 : 동물
다리수 : 4
동물 이(가) 달린다. 
동물 이(가) 물을(를) 먹는다.
==============================
종류 : 강아지
다리수 : 4
강아지 이(가) 달린다. 
강아지 이(가) 뼈다귀을(를) 먹는다.
강아지의 이름은 행운이이다.
강아지 이(가) 멍멍 짖는다.(소리를 낸다) 
'''

class Animal:
    def __init__(self, objName, leg):
        self.objName = objName
        self.leg = leg

    def info(self):
        print(f'종류 : {self.objName}\n다리수 : {self.leg}')

    def run(self):
        print(f'{self.objName} 이(가) 달린다')

    def eat(self, food):
        print(f'{self.objName} 이(가) {food}(을/를) 먹는다')

    def total_print(self,food):
        self.info()
        self.run()
        self.eat(food)



class Dog(Animal):
    def __init__(self, objName, leg):
        Animal.__init__(self, objName, leg)

    def printName(self, name):
       print(f'{self.objName} 이름은 {name}이다')

    def shout(self, sound):
        print(f'{self.objName}이(가) {sound} 짖는다/소리를 낸다')

    def total_print2(self, food, name, sound):
        self.total_print(food)
        self.printName(name)
        self.shout(sound)

animal1 = Animal('동물', 4)
animal1.total_print('물')
print("="*30)

dog1 = Dog('강아지', 4)
dog1.total_print2('뼈다귀', '행운이', '멍멍')