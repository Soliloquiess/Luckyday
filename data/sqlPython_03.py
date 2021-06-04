import pymysql as p
conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                 db='sqldb', charset='utf8')
cursor = conn.cursor()

# DB생성
cursor.execute('DROP DATABASE IF EXISTS sqldb2;')
cursor.execute('CREATE DATABASE sqldb2;')

# 테이블 생성
cursor.execute("USE sqldb2;")
cursor.execute("""
      create table movieTbl
                (
                    movieNum int PRIMARY KEY not null AUTO_INCREMENT, -- 번호(PK)
                    movieName varchar(30) not null, -- 무비명 
                    kind varchar(30), -- 장르명
                    price int not null, -- 대여 가격
                    period int not null -- 대여 기간
                );
""") # 워크벤치에서 생성됐는지 확인

conn.close()