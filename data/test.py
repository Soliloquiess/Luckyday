def testPrint():
    print("test.py 파일 출력")

def HelloMessage(m):
    print('test.py에 등록된 HellowMessage() 함수호출')
    print(f'Hello {m}')

# 다른 파일에서 임포트해 모듈로 사용될 경우를 대비
# 메인으로 실행될때만 특정 메세지 출력하기 (모듈로써 사용되는 경우가 아니라)
if __name__ == '__main__':
    print('메인으로 실행됨')

print()



'파이썬 문제풀이'

# 1부터 100까지 합을 구하여 다음과 같이 결과를 출력하도록 프로그래밍하세요. (10점)
sum=0
for i in range(101):
    sum+=i
print(f'1부터 100까지의 합은 {sum}입니다')

# 구구단을 다음과 같이 출력하도록 프로그래밍하세요. (10점)
for i in range(2,10):
    for j in range(1,10):
        print(f'{i} * {j} = {i*j}\t', end="")
    print()
# try..except..else 구문을 이용하여 2개의 입력값을 입력받은 후 입력값이 숫자가 아니라면 오류 메시지를 출력하고 숫자라면 두수의 합을 출력하도록 프로그래밍하세요.   (15점)
try:
    x,y = int(input('값을 입력하세요 =>')), int(input('값을 입력하세요 =>'))
except Exception as e:
    print('입력하신 값은 숫자가 아닙니다, 에러 상세확인 =>', e)
else:
    print(f'{x} + {y} = {x+y}')


#사용자가 종료할 때까지 입력받은 문자열을 "C:/새파일.txt" 파일에 계속 추가하는 코드를 작성하세요.
with open('/새파일.txt','w',encoding='utf-8') as f:
    f.write(input('파일에 저장할 내용을 입력하세요=>'))