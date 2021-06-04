# 파이참에서 FILE/SETTINGS 클릭 후  Project에서 pymysql 설치 됐는지 목록확인 필요
# 레퍼런스 사이트 https://github.com/PyMySQL/PyMySQL/


# Step1/ 모듈 임포트
import pymysql

# Step2/ mysql의 계정의 특정 데이타베이스에 접속해서 객체 생성
conn = pymysql.connect(
                        host = 'localhost', port=3306,
                        user='root', password='1234',
                        db='world', charset='utf8')
print(conn, type(conn))

# Step3/ 커서(Cursor) 객체 생성 => 객체명 = 연결객체(conn).cursor()
cursor = conn.cursor()

# Step4/ sql명령을 실행 => 커서객체.execute(sql 명령문)
# 테이블조회
cursor.execute('SELECT Name, Population FROM city LIMIT 10;')

# Step5/ sql 실행 결과 저장 => 변수명=커서객체
# .fetchall() 모두를 2차원 튜플구조로, .fetchmany(size) size 행만큼 2차원 튜플로 갖고옴, .fetchone() 하나의 행만
#result_list = cursor.fetchall()
result_list = cursor.fetchmany(5)
for item in result_list:
    print(item)

# DB close
conn.close()

