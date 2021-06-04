import random

def lottoNumber():
    resultList =[]
    for i in range(6):
        num = random.randint(1, 46)
        if num not in resultList:
            resultList.append(num)
    print(resultList)
    
    
#강사님 답
def lottoNumber() :
    lottoList = []
    while True:
        if len(lottoList)>= 6:
            break
        else:
            data = random.randint(1,45)
            if data not in lottoList:
                lottoList.append(data)
    print(lottoList)

lottoNumber()

if __name__ =="__main__":
    print('Main 으로  실행되었음')