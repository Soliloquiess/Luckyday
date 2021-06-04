/* 11.25(WED) 수업*/

-- =======================================================
-- << INNER JOIN 뷰 등록 >>
SELECT B.*, name,addr FROM buyTbl B -- 테이블 B필드 전체와 U테이블의 이름,지역을 검색
INNER JOIN userTbl U ON B.userID = U.userID;

CREATE VIEW v_buyUser
AS 
SELECT B.*, name,addr FROM buyTbl B 
INNER JOIN userTbl U ON B.userID = U.userID;

SELECT * FROM v_buyUser;
SHOW FULL TABLES IN sqldb WHERE Table_Type="VIEW";


-- =======================================================
-- << SELF JOIN 뷰 등록 후 활용 >>
-- 셀프조인 결과확인
SELECT A.emp '사원명', A.empTel '사원구내번호', A.manager '직속상관', B.empTel '직속상관구내번호'
FROM empTbl A
INNER JOIN empTbl B ON A.manager = B.emp;

-- 뷰 생성
DROP VIEW v_empTbl;
CREATE VIEW v_empTbl
AS
SELECT A.emp '사원명', A.empTel '사원구내번호', A.manager '직속상관', B.empTel '직속상관구내번호'
FROM empTbl A
INNER JOIN empTbl B ON A.manager = B.emp;

SELECT * FROM v_empTbl;

-- 뷰 활용
SELECT 직속상관 '우대리의 상관', 직속상관구내번호
FROM v_empTbl WHERE 사원명 = '우대리';


-- =======================================================
-- << 데이타베이스 관련 명령어 >>
-- DROP DATABASE 데이타베이스명;
-- CREATE DATABASE 데이타베이스명;
-- SHOW DATABASES; 모든 데이타베이스 표시 
-- USE 데이타베이스명; 데이타베이스 변경 
DROP DATABASE tableDB; 
CREATE DATABASE tableDB;
SHOW DATABASES;
USE tableDB;

-- =======================================================
-- << 테이블 생성과 삭제 관련 명령어 >>
-- DROP/DELETE TABLE  <IF EXISTS> 테이블명; -- 테이블 삭제 

-- CREATE TABLE 테이블명 (필드명 자료형 옵션);
-- 옵션 : NULL/ NOT NULL / AUTO INCREMENT 
-- PRIMARY KEY / FOREIGN KEY(필드명) REFERENCES 테이블명(필드명)

-- SHOW TABLES; -- 테이블 목록 표시 
-- DESC 테이블명; -- 테이블 구조 표시 

-- << MYSQL 자료형 >>
-- 숫자형 (정수, 실수...) smallint, int, float, decimal ... 
-- 문자형 char(n), varchar(n), binary(n), text, longtext,  blob...
-- 날짜형 ????-??-?? ??:??:?? date, time, datetime ...
-- 기타  lob, json ... 


-- 회원가입테이블 userTbl
-- 이름 userName -- char(5) not  null 
-- 아이디 userId -- char(8) not   null      PRIMARY KEY 
-- 연락처 mobile -- varchar(16)   not null 
-- 이메일 email -- varchar(20)    null
-- 생년월일 birth -- date          null 
CREATE TABLE IF NOT EXISTS userTbl ( userName char(5) not null, 
									 userId char(8) not null PRIMARY KEY, 
									 mobile VARCHAR(16) not null, 
									 email VARCHAR(20) null, 
									 birth date);
DESC userTbl;

-- 레코드 삽입 테스트 
-- INSERT INTO 테이블명 VALUES (..,..,..,..);
-- INSERT INTO 테이블명 (필드명....)VALUES (..,..,..,..);
-- INSERT INTO 테이블명 VALUES (...), (...), (...), ....;

INSERT INTO userTbl 
   VALUES ('박지민','PJM','010-1234-5678','abc@naver.com','1995-08-31');
    
INSERT INTO userTbl 
   VALUES ('박지민','BJM','011-2345-5678',NULL, NULL);
   
INSERT INTO userTbl 
   VALUES 
      ('이지민','LJM','010-5678-7777','ccc@naver.com','1998-05-31'), 
        ('황지민','HJM','011-1567-7890','dddd@naver.com','1994-11-30'),
        ('최지민','CJM','없음',NULL, NULL);
   

SELECT * FROM userTbl;

-- =======================================================
-- << 테이블 구조 변경 ALTER TABLE >>
-- 컬럼 추가, 컬럼 수정, 컬럼 삭제 

-- 컬럼 추가
-- ALTER TABLE 테이블명
--    ADD 컬럼명 데이터형( CHAR(), INT, VARCHAR(), DATE, DATETIME ... )
--    [DEFAULT 디폴트값] -- 기본값 설정 
--    [NULL/NOT NULL]; -- Null 허용함

-- userTbl 테이블에서 homepage varchar(30) 컬럼 추가 
ALTER TABLE userTbl
ADD homepage VARCHAR(30) DEFAULT 'http://google.com' -- 디폴트값
NULL; -- Null 허용

-- userTbl 테이블에서 addr varchar(50) 컬럼 추가 
ALTER TABLE userTbl ADD addr VARCHAR(50); -- 디폴트값 미지정시 NULL값 들어감  

-- 테이블 구조 변경후에 레코드 삽입 테스트 
INSERT INTO userTbl 
VALUES ('김철수','KCS','019-2345-5678',NULL, NULL, NULL); -- NULL값 지정시 디폴트 값 들어가지 X
    
INSERT INTO userTbl (userName, userId, mobile)
VALUES ('윤철수','LCS','011-9999-5678'); -- 값 따로 안넣어주면 디폴트값 들어감

DESC userTbl;
SELECT * FROM userTbl;



-- 컬럼 삭제 : 외래키나 기본키가 설정되어 있지 않은 경우 
-- ALTER TABLE 테이블명 DROP COLUMN 컬럼명;
ALTER TABLE userTbl  DROP COLUMN addr;
DESC userTbl; SELECT * FROM userTbl;    

-- 데이타가 있는 컬럼 삭제 
ALTER TABLE userTbl DROP COLUMN email;
DESC userTbl; SELECT * FROM userTbl;   

--  NOT NULL 속성의 컬럼도 삭제 OK
ALTER TABLE userTbl DROP COLUMN mobile;
DESC userTbl; SELECT * FROM userTbl; 

--  기본키로 설정된 컬럼 삭제 OK
ALTER TABLE userTbl DROP COLUMN userId;
DESC userTbl; SELECT * FROM userTbl; 




-- 컬럼 수정 : 컬럼명1을 컬럼명2로 수정 
-- ALTER TABLE 테이블명 
-- CHANGE COLUMN 컬럼명1 컬럼명2 데이타형 [NULL 또는 NOT NULL] ;

-- homepage 컬럼을 url로 변경
ALTER TABLE userTbl CHANGE COLUMN homepage url VARCHAR(50) NULL;

-- birth 컬럼을 birth_date int형으로 변경
ALTER TABLE userTbl CHANGE COLUMN birth birth_date INT NULL;

DESC userTbl;

-- =======================================================
-- FOREIGN KEY (외래키) : 다른 테이블의 특정 필드값 참조
-- FOREIGN KEY (외래키설정 필드명) REFERENCES 참조테이블명(참조테이블의 외래키필드명);


-- 외래키 테스트 
-- demo_people (name, phone, pid(PK))
-- demo_property (spid(PK), pid(FK), selling)

use tableDB;
CREATE TABLE demo_people 
(
   pid int NOT NULL PRIMARY KEY AUTO_INCREMENT,
   name VARCHAR(10) NOT NULL,
    phone VARCHAR(16) NULL
);

DESC demo_people; -- 만들어진 테이블 확인

CREATE TABLE demo_property 
(
   spid int NOT NULL PRIMARY KEY AUTO_INCREMENT,
   pid int NOT NULL,
    selling VARCHAR(30) NOT NULL,
    FOREIGN KEY(pid) REFERENCES  demo_people(pid) -- demo_people 테이블의 pid컬럼을 외래키로 참조
);

DESC demo_property; -- 만들어진 테이블 확인(외래키 설정 포함)

SHOW TABLES;

-- 외래키가 있는 테이블에서 레코드 삽입 테스트 
-- demo_people , demo_property

INSERT INTO demo_people VALUES (NULL, '신짱구', '011-9090-9999');
SELECT * FROM demo_people;

INSERT INTO demo_property VALUES (NULL, 1, '야구공');
SELECT * FROM demo_property;

INSERT INTO demo_people VALUES 
      (NULL, '오짱구', '011-5555-1234'), (NULL, '박짱구', NULL);
SELECT * FROM demo_people;

-- 외래키가 설정된 테이블 
-- INSERT INTO demo_property VALUES (NULL, 5, '노트북');
INSERT INTO demo_property VALUES (NULL, 3, '노트북');
INSERT INTO demo_property VALUES (NULL, 2, '쇼파');
INSERT INTO demo_property VALUES (NULL, 2, '자동차');
SELECT * FROM demo_property;

-- 이너 조인 
SELECT * FROM demo_people D1
   INNER JOIN demo_property D2
    ON D1.pid = D2.pid;
    
    
-- =====================================================
--  퀴즈1 
--   다음과 같은 형태로  movieTbl 테이블을 생성하여라. 
--   movieNum int  -- 번호(기본키, 자동증감, 필수 속성) 
--   movieName varchar(30) -- 무비명(필수 속성) 
--   kind varchar(30) -- 장르명(필수 속성) 
--   price int, -- 대여 가격(필수 속성) 
--   period intl -- 대여 기간(필수 속성) 

CREATE TABLE movieTbl(
					  movieNum INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                      movieName VARCHAR(30) NOT NULL,
                      kind VARCHAR(30) NOT NULL,
                      price INT NOT NULL,
                      period INT NOT NULL
);

DESC movieTbl;

-- 퀴즈2. 퀴즈1의 movieTbl 테이블의 자료형에 맞추어 5개의 레코드를 삽입하여라. 
INSERT INTO movieTbl VALUES(movieNum,'삼익토익반','드라마',9000,15),(movieNum,'불초상', '로맨스', 10000, 30),
						   (movieNum, '먼훗날우리','드라마',5000,10),(movieNum, '오케이마담', '코미디',2000,5),
                           (movieNum, '원더','드라마',5000,1);
 INSERT INTO movieTbl VALUES (movieNum, '기생충','드라마',5000,1);

SELECT * FROM movieTbl;

--  퀴즈3 
--   다음과 같은 형태로  memberTbl 테이블을 생성하여라. 
--     userNum int  -- 번호(기본키, 자동증감, 필수 속성) 
--     name varchar(20)  -- 회원명
--     grade int  -- 회원 등급(필수 속성) 
--     tel varchar(15)  -- 연락처(필수 속성) 
--     address varchar(300) -- 주소(널 허용)
--     money int  -- 예치금(필수 속성) 
CREATE TABLE memberTbl(
					  userNum INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                      name VARCHAR(20),
                      grade INT NOT NULL,
                      tel VARCHAR(15) NOT NULL,
                      address VARCHAR(300),
                      money INT NOT NULL
);

-- 퀴즈4.  퀴즈3의 memberTbl 테이블의 자료형에 맞추어 7개 이상 레코드를 삽입하여라. 
INSERT INTO memberTbl VALUES (userNum, '서은기', 3, '010-1234-1111', '서울', 38000),
							 (userNum, '강마루', 2, '010-1234-2222', '서울', 18000 ),
                             (userNum, '한재희', 3, '010-1234-3333', '제주도', 27000),
                             (userNum, '이세령', 1, '010-1234-4444', '성남', 19800),
                             (userNum, '차윤서', 1, '010-1234-5555', '하남', 10000),
                             (userNum, '문채원', 4, '010-1234-6666', '서울', 90000),
                             (userNum, '차지원', 3, '010-1234-7777', '판교', 54000);

SELECT * FROM memberTbl;

--  퀴즈5 
--   다음과 같은 형태로  rentTbl 테이블을 생성하여라. 
/*
    rentNum int  -- 대여번호(PK)(기본키, 자동증감, 필수 속성) 
    userNum int -- 대여한 회원번호(FK) (필수 속성, memberTbl의 키 참조) 
    movieNum int  --대여한 비디오번호(FK) (필수 속성, movieTbl의 키 참조) 

*/
DROP TABLE rentTbl;
CREATE TABLE rentTbl(
					rentNum INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                    userNum INT NOT NULL,
                    movieNum INT NOT NULL,
                    FOREIGN KEY (userNum) REFERENCES memberTbl(userNum),
                    FOREIGN KEY (movieNum) REFERENCES movieTbl(movieNum)
); 
DESC rentTbl;

-- 퀴즈6.  퀴즈5의 rentTbl 테이블의 자료형에 맞추어 7개 이상 레코드를 삽입하여라. 
INSERT INTO rentTbl VALUES   (rentNum,2,2),(rentNum,3,4),(rentNum,5,2),(rentNum,7,1),
							 (rentNum,1,5),(rentNum,4,4),(rentNum,6,1);
INSERT INTO rentTbl VALUES (rentNum,1,2),(rentNum,4,4),(rentNum,7,2),(rentNum,5,1),
						   (rentNum,2,5),(rentNum,3,4),(rentNum,5,1);
							
SELECT * FROM rentTbl;

-- 퀴즈7.  3개의 테이블 (movietbl, rentTbl, memberTbl)을 이너조인하여라. 
SELECT * FROM rentTbl R
INNER JOIN movietbl MO ON R.movieNum = MO.movieNum
INNER JOIN memberTbl ME ON R.userNum = ME.userNum;


-- 퀴즈8.  퀴즈7의 이너조인 결과를 뷰 v_mrm 으로 생성하여라 
DROP VIEW v_mrm;
CREATE VIEW v_mrm
AS
SELECT R.rentNum, ME.userNum, MO.movieNum, movieName, kind, price, period, name, grade, tel, address, money  FROM rentTbl R
INNER JOIN movietbl MO ON R.movieNum = MO.movieNum
INNER JOIN memberTbl ME ON R.userNum = ME.userNum;

SELECT * FROM v_mrm;

-- 강사님 답
CREATE VIEW v_mrm
   AS
SELECT rentNum, M.*, MV.*  FROM renttbl R
INNER JOIN membertbl M ON R.userNum = M.userNum
INNER JOIN movietbl MV ON MV.movieNum = R.movieNum
ORDER BY rentNum;



-- 퀴즈9.  대여를 하지 않는 회원 목록을 출력하여라. 
SELECT * FROM v_mrm
WHERE rentNum IS NULL;

-- 강사님 답
SELECT name FROM membertbl M
LEFT OUTER JOIN renttbl R ON R.userNum = M.userNum
WHERE rentNum is NULL;


-- 퀴즈10.  대여가 한번도 되지않은 영화 목록을 출력하여라. 
SELECT movieNum, movieName
FROM movieTbl
WHERE movieNum NOT IN(SELECT R.movieNum FROM rentTbl R);

-- 강사님 답
SELECT movieName FROM movietbl MV
LEFT OUTER JOIN  renttbl R ON MV.movieNum = R.movieNum
WHERE rentNum is NULL;


--  퀴즈11.  회원별로 구매 횟수를 출력하여라. 
SELECT ME.name '회원명', COUNT(*) '대여횟수'
FROM rentTbl R
INNER JOIN memberTbl ME ON R.userNum = ME.userNum
GROUP BY R.userNum ORDER BY R.userNum;

-- 강사님 답
SELECT name, count(R.userNum) FROM renttbl R
INNER JOIN membertbl M ON R.userNum = M.userNum
INNER JOIN movietbl MV ON MV.movieNum = R.movieNum
GROUP BY R.userNum ORDER BY count(R.userNum) DESC, name;   


-- =====================================================
-- 기본키 추가와 삭제 
USE sqlDB;

-- userTbl(기본키 O) => userCopy(기본키 X), 즉, 카피해올 떈 KEY는 복사해오지 않음
CREATE TABLE userCopy 
(
   SELECT * FROM userTbl
);
SHOW TABLES;
DESC userTbl;
DESC userCopy;

-- 기본키 추가 
--  ALTER TABLE 테이블명
--    ADD CONSTRAINT PK_테이블명_기본키필드명
--  PRIMARY KEY (기본키필드명);

-- userCopy 테이블에서 userID 기본키 설정 
ALTER TABLE userCopy
   ADD CONSTRAINT PK_userCopy_userID
   PRIMARY KEY (userID);

DESC userCopy;

-- 기본키 삭제하기 => ALTER TABLE 테이블명 DROP PRIMARY KEY; 
ALTER TABLE userCopy DROP PRIMARY KEY; 
DESC userCopy;      

-- 외래키 추가 
-- ALTER TABLE 테이블명 ADD CONSTRAINT 테이블명_ibfk_1
-- FOREIGN KEY (외래키필드명) REFERENCES 참조테이블명(참조테이블의 외래키필드명);

ALTER TABLE buyCopy
   ADD CONSTRAINT buyCopy_ibfk_1
 FOREIGN KEY (userID)
 REFERENCES userTbl(userID);

DESC buyCopy;

-- 외래키 삭제하기 : 외래키명은 [Schemas]탭에서 해당 테이블의 정보 클릭후 FOREIGN_KEYS 에서 확인 
-- ALTER TABLE 테이블명  DROP FOREIGN KEY 외래키명;
DESC buyCopy;
ALTER TABLE buyCopy  DROP FOREIGN KEY buyCopy_ibfk_1;
