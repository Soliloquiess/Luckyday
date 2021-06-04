/* 11.20(FRI) 수업*/

USE sqldb;
SHOW TABLES;
DESC buyTbl;

-- GROUP BY (그룹을 묶어주는 역할. 집계함수와 함께 사용) => SELECT .. FROM 테이블명 GROUP BY 컬럼명;
-- 합계 구하기 SUM(컬럼명)  /  평균 구하기 AVG(컬럼명)
-- 각 종목의 가격 합계, 평균를 groupName을 기준으로 정렬하여 표시하기 
SELECT groupName, SUM(price), AVG(price)  FROM buyTbl
GROUP BY groupName ORDER BY groupName;

-- AS 별칭이름; 컬럼명을 대신하는 별칭 이름 표시 => SELECT 컬럼명 AS 별칭명 FROM 테이블명;    
-- 함수 결과 필드명에 별칭 주기
SELECT userID AS '아이디', prodName AS '상품명', price AS '가격'
FROM buyTbl LIMIT 5;

-- 집계함수 결과 필드 이름 정의해 출력
SELECT groupName '', SUM(price), AVG(price)  FROM buyTbl
GROUP BY groupName ORDER BY groupName;

-- 퀴즈 : buytbl 테이블에서 사용자별로 구매합계 구하기 
/*사용자아이디별 총구매액 표시 - GROUP BY, SUM(), AS ==== 총구매액은? SUM(price*amount)*/
SELECT * FROM buyTbl;
SELECT userId '사용자아이디' , SUM(price*amount) '총구매액' 
FROM buyTbl GROUP BY userId; 



-- 집계함수
-- MAX(필드명이나 수식)
-- MIN(필드명이나 수식)
-- COUNT(필드명이나 수식) : 레코드 갯수 
SELECT    MAX(price) AS '최대값', 
		  MIN(price) AS '최소값',
		  COUNT(price) AS '갯수'
FROM buytbl;
   
-- buytbl 테이블에서 각 사용자별로 물건을 몇개 사는지 평균 구하기 
SELECT userId AS '회원 아이디', AVG(amount) '평균구매횟수' 
FROM buyTbl GROUP BY userId ORDER BY AVG(amount) DESC; 

-- userTbl 테이블에서 가장 큰기, 가장 작은키의 레코드 출력
SELECT MAX(height) '가장큰키', MIN(height) '가장작은키'  FROM userTbl;

SELECT * FROM userTbl 
WHERE (height = 166) OR (height = 186);

-- 서브쿼리 이용
SELECT * FROM userTbl
WHERE height = (SELECT MAX(height) FROM userTbl)
	OR height = (SELECT MIN(height) FROM userTbl);
    

-- 전체 레코드 수 count(*) 이용, NULL 미포함  
-- userTbl 에서 휴대폰(mobile1) 유/무 에 따라 출력하기 
SELECT COUNT(*) FROM userTbl
WHERE mobile1 IS NOT NULL;

SELECT COUNT(*) '전체 사용자',
	   COUNT(mobile1) '휴대폰 보유자 수', 
	   COUNT(*) - COUNT(mobile1) '휴대폰 미보유자 수'
FROM userTbl;


-- ##########################       
-- HAVING 절 : WHERE와 비슷하게 조건 제한, 주로 집계함수에 대해서 조건을 제한할때 사용 
-- 순서 주의 
-- SELECT .. FROM 테이블명 
-- GROUP BY 컬럼명 HAVING 조건 
-- ORDER BY 컬럼명 LIMIT 숫자;

-- buyTbl 테이블에서 총구매액이 1000 이상 조건으로 사용자(userID)별 총 구매액 표시 
SELECT userID '회원아이디', SUM(price*amount) '총구매액' FROM buyTbl
GROUP BY userID
HAVING SUM(price*amount) >= 1000;

SELECT * FROM buyTbl;


-- 퀴즈
-- buyTbl 테이블에서 userID 별 평균 구매 횟수(AVG(amount))가 
-- 1~3 사이인 레코드만 출력하여라 
SELECT userID, AVG(amount) '평균구매횟수' FROM buyTbl
GROUP BY userID
HAVING AVG(amount) BETWEEN 1 AND 3;


--  WITH ROLLUP : 중간 합계, 순서 주의 
-- SELECT .. FROM 테이블명 
-- GROUP BY 컬럼명 HAVING 조건 
-- WITH ROLLUP
-- ORDER BY 컬럼명 LIMIT 숫자;

-- buytbl 테이블에서 종목(groupName) 별로 구매액 SUM(price*amount)  및 총합 구하기 

-- 그룹바이 기준이 종목(groupName)
SELECT num, groupName AS '종목', SUM(price*amount) AS '구매액'
   FROM buytbl 
    GROUP BY groupName;

-- 그룹바이 기준이 종목(groupName), 주문번호(num)
SELECT num, groupName AS '종목', SUM(price*amount) AS '구매액'
   FROM buytbl 
    GROUP BY groupName, num;

-- WITH ROLLUP 이용 
-- 종목별 합계가 함께 표시 : NULL 행 삽입 
-- 그룹바이 기준이 종목(groupName), 주문번호(num)
-- 맨 하단 NULL, NULL 행은 총합 
SELECT num, groupName AS '종목', SUM(price*amount) AS '구매액'
   FROM buytbl 
    GROUP BY groupName, num
    WITH ROLLUP;

SELECT groupName AS '종목', SUM(price*amount) AS '구매액'
   FROM buytbl 
    GROUP BY groupName
    WITH ROLLUP;



-- CRUD 명령어,  DML(Data Manupulation Language)
CREATE TABLE buyTbl2 
      (SELECT * FROM buyTbl);
 DESC buyTbl2;   
 
-- 레코드 삽입 1
-- INSERT INTO 테이블명 VALUES(값1, 값2 .. )
INSERT INTO buyTbl2 VALUE (13, 'TTT', '손난로', '디지털', 20000, 3);
SELECT * FROM  buyTbl2;       

-- 레코드 삽입 2
-- INSERT INTO 테이블명 (컬럼명1, 컬럼명2... ) VALUES(값1, 값2 .. )
INSERT INTO buyTbl2 (num, userID, prodName, groupName, price, amount)
VALUE (14,'KKK','가습기','디지털', 50000,1);

-- NULL 허용하는 groupname값 인서트 생략 (NULL값으로 들어감)
INSERT INTO buyTbl2 (num, userID, prodName,  price, amount)
VALUE (15,'SMY','로봇청소기', 500000,1);


-- 다른 테이블의 레코드를 SELECT 문으로 삽입하기 => INSERT INTO 테이블명 (컬럼명1, 컬러명2 ... ) SELECT 문 
-- buyTbl3 테이블 생성 후 buyTbl 테이블에서 '전자' groupName 레코드 삽입하기 
CREATE TABLE buyTbl3 
(  num 		INT AUTO_INCREMENT NOT NULL PRIMARY KEY, -- 순번(PK)
   userID  	CHAR(8) NOT NULL, -- 아이디(FK)
   prodName 	CHAR(6) NOT NULL, --  물품명
   groupName 	CHAR(4)  , -- 분류
   price     	INT  NOT NULL, -- 단가
   amount    	SMALLINT  NOT NULL -- 수량
);
SHOW TABLES;

-- '전자' 레코드 삽입
INSERT INTO buyTbl3 (userID, prodName, groupName, price, amount)
SELECT userID, prodName, groupName, price, amount FROM buyTbl WHERE groupName = '전자';

SELECT * FROM buyTbl3;


-- ************************************************** 점심시간 ******************************************************
-- *** 수정이 적용되게 MySQL 환경 설정하기  [Edit]-[Preferences] 클릭 후  SQL Editor 클릭후 맨 아래 Safe ~ 선택을 해제한다. 워크벤치 재실행 
-- 레코드 수정과 삭제 => UPDATE 테이블명 SET 컬럼명=값 WHERE 절;
UPDATE buyTbl3 SET amount=10 WHERE prodName = '노트북';
SELECT * FROM buyTbl3; -- 변경여부 확인

-- 레코드의 price 가격 모두를 150%로 변경하여라  (price*1.5)
UPDATE buytbl3 SET price = price*1.5;
SELECT * FROM buytbl3; 

-- 테이블 구조 제외 레코드만 삭제 => TRUNCATE TABLE 테이블명;
-- 테이블 삭제 =>  DROP TABLE 테이블명;

-- buyTbl을 이용해 3개의 테이블 생성 
CREATE TABLE IF NOT EXISTS buytbl_b
   (SELECT userID, prodName, price FROM buyTbl);   
CREATE TABLE IF NOT EXISTS buytbl_c
   (SELECT userID, prodName, price FROM buyTbl);   
CREATE TABLE IF NOT EXISTS buytbl_a
   (SELECT userID, prodName, price FROM buyTbl);   
    
-- DB안에 등록된 테이블 목록 확인하기 
SHOW TABLES;

-- 특정 레코드 삭제 =>  DELETE FROM 테이블명 WEHRE 절 
-- (WHERE 절 생략시 레코드 모두 삭제 -> TRUNCATE와 결과 동일)
SELECT * FROM buytbl_a;
DELETE FROM buyTbl_a WHERE userID = 'BBK';
DELETE FROM buyTbl_a;

SELECT * FROM buyTbl_b;
DELETE FROM buyTbl_B WHERE userID = 'EJW'; -- 조건 만족하는 레코드만 삭제
DELETE FROM buyTbl_b; -- 모든 레코드 삭제

-- 테이블 삭제 => DROP TABLE 테이블명;
-- 테이블 구조 제외 레코드만 삭제 => TRUNCATE TABLE 테이블명;



 -- =========================================================================   SQL 퀴즈 
 -- 1) userTBL 테이블에서 구조만 복사하여 userTbl_sample 테이블을 생성하여라. 
DROP TABLE userTbl_sample;
CREATE TABLE userTbl_sample LIKE userTbl;
SELECT * FROM userTbl_sample;

 -- 2) userTbl_sample에 아래  데이터를 참조하여 데이터를 삽입하고 출력하여라.
/*
USERID   USERNAME    BIRTHYEAR      ADDR      MOBILE1    MOBILE2    HEIGHT       MDATE   
--------    ----------           ---------- -- --- -------- ---------- -       -------
PJM   박지민   1995   경남      010   22222222   173   2016-04-04
KSJ   김석진   1993   경기                  186   2015-04-04
KJD   김자두   1997   전남      010   33333333   162   2017-07-07
GGD   고길동   1995   서울      010   11111111   165   2018-08-08
*/

INSERT INTO userTbl_sample VALUES ('PJM', '박지민', 1995, '경남', '010', '22222222', 173, '2016-4-4');
INSERT INTO userTbl_sample (userID, Name, birthYear, addr, height, mDate) VALUE ('KSJ', '김석진', 1993, '경기', 186, '2015-4-4');
INSERT INTO userTbl_sample VALUES ('KJD', '김자두', 1997, '전남', '010', '33333333', 162, '2017-7-7');
INSERT INTO userTbl_sample VALUES ('GGD', '고길동', 1995, '서울', '010', '11111111', 165, '2018-8-8');

-- 3) userTbl 테이블에서 휴대폰 번호가 011로 시작하는 레코드만 userTbl_sample로 복사하여라. 
INSERT INTO userTbl_sample
SELECT * FROM userTbl WHERE mobile1 = '011';

-- 4) userTbl_sample 테이블에서 ADDR 컬럼값이 경남인 경우 경남을 부산으로 데이터값을 수정하여라.
UPDATE userTbl_sample SET addr = '부산' WHERE addr = '경남'; 

-- 5) userTbl_sample 테이블에서 MOBILE1과 MOBILE2 값이 NULL 인 경우 019, 55555555 값으로 수정하여라.
UPDATE userTbl_sample SET mobile1='019', mobile2='55555555' WHERE mobile1 IS NULL AND mobile2 IS NULL;
SELECT * FROM userTbl_sample;

-- 6) userTbl_sample 테이블에서 레코드를 이름순으로 정렬한 후 복사하여 userTbl_sample2 테이블을 생성하여라. 
CREATE TABLE userTbl_sample2 (SELECT * FROM userTbl_sample ORDER BY name);

-- 7) userTbl_sample2 테이블에서 국번이 011인 데이터를 삭제하여라
DELETE FROM userTbl_sample2 WHERE mobile1 = '011';

-- 8) userTbl_sample2 테이블에서 모든 레코드를 삭제하여라. 
DELETE FROM userTbl_sample2;
SELECT * FROM userTbl_sample2;

-- 9) userTbl_sample1, userTbl_sample2 테이블을 모두 삭제하여라.  
DROP TABLE userTbl_sample;
DROP TABLE userTbl_sample2;

-- 10) sqldb2 데이타베이스를 생성하여라 
CREATE DATABASE sqldb2;
SHOW DATABASES;

-- 11) sqldb 데이타베이스의 userTbl 테이블을 sqldb2 테이블로 복사하여라 
CREATE TABLE sqldb2 (SELECT * FROM sqldb.usertbl);
DESC sqldb2;

-- 12) employees 데이타베이스의 employees 테이블에서 first_name 이 'S'로 시작하는 
--  레코드만 sqldb2 데이타베이스에 employees_S 테이블로 복사하여라. 
CREATE TABLE employees_S (SELECT * FROM employees.employees WHERE first_name LIKE 'S%');


-- #################### #################### #################### ####################
-- 변수 생성과 출력(p234)
USE sqldb;

-- SET @변수명 = 초기값;
SET @a = 5;
SET @b = 3.14;
SET @C = 'HELLO MYSQL';

-- SELECT @변수명;
SELECT @a, @b, @c;
SELECT @a 'A', @b 'B', @a+@b 'A+B', @a*@b 'A*B';

-- 테이블에서 변수 사용
SET @star = '*****';
SELECT name, @star, addr FROM userTbl;

/* 퀴즈
 usertbl 테이블에서 키가 180 넘는  레코드만 추출한 후 아래와 같은  형태로 출력하여라 
            이름   키   
 가수이름 => 김경호   ?  cm
 가수이름 => 이승기   ?  cm 
 
 */

SET @t1 = '가수이름 => ';
SET @t2 = 'cm';

SELECT @t1 AS ' ', 
       name AS '이름', 
       height AS '키', 
       @t2 AS ' ' 
         FROM userTbl WHERE height>180;

-- 데이터 형변환 CASTING (p236)
/*
CAST ( .. AS 데이터형식)
CONVERT ( .. , 데이터형식)

데이터형식 :
 BINARY, CHAR(), DATE , TIME, 
 SIGNED INTEGER, UNSIGNED INTEGER
*/

-- amount 평균 구매횟수 => 실수 
SELECT * FROM buyTbl;
SELECT AVG(amount) FROM buyTbl; -- 2.9167

-- CAST ( .. AS 데이터형식) 혹은 CONVERT ( .. , 데이터형식)
-- amount 평균 구매횟수 => 정수
SELECT CAST(AVG(amount) AS SIGNED INTEGER) FROM buyTbl;
SELECT CONVERT(AVG(amount), SIGNED INTEGER) FROM buyTbl;

-- 실수형숫자 -> 문자  /  숫자문자 -> 양의정수
SELECT CAST(3.14 AS CHAR(10)), CAST('23Python5667' AS SIGNED INTEGER); 
SELECT CONVERT(3.14 , CHAR(10)), CONVERT('23Python5667' , SIGNED INTEGER); 

-- 제어흐름함수 (p239)
-- IF(수식, True값1, False값2)
-- IFNULL(수식1, 수식2) : 수식1이 NULL이 아니면 수식1 반환, NULL 이면 수식2 반환   
-- NULLIF(수식1, 수식2) : 수식1과 수식2가 같으면 NULL, 다르면 수식1 반환
SELECT IF(100<500, '크다', '작다'), IF(100>500, '크다', '작다');
SELECT IFNULL(NULL, '널값이다'), IFNULL(500, '널값이다');

-- buytbl 테이블에서 groupName 컬럼값이 NULL 이면 '준비중..'으로 표시하여라 
SELECT * FROM buyTbl; 
SELECT prodName '상품명', IFNULL(groupName, '준비중..') '종목',  price '가격' 
FROM buyTbl;


-- 다중분기 
/*
	CASE 값1 
		WHEN 값2 THEN 결과값1 
        WHEN 값3 THEN 결과값2 
        .
        .
        ELSE 결과값 n 
        END
*/
-- 값1이 값2와 같다면 결과값1 그렇지 않다면 결과값2 반환
-- SET @age = CAST(10 AS SIGNED INTEGER);

SET @age = 3;
SELECT CASE @age
	WHEN 3 THEN '셋'
    WHEN 11 THEN '십일'
    ELSE '...'
END AS '다중분기 TEST';
    
-- @price 변수값에 따라 짝수, 홀수 출력하기
SET @price = 11;
SELECT @price AS '변수' ,
CASE @price%2
	WHEN 0 THEN '짝수'
    ELSE '홀수'
END '결과';

-- buytbl 테이블에서 price 컬럼값이 따라 짝수, 홀수 출력하기
SELECT price '변수',
CASE price%2
	WHEN 0 THEN '짝수'
    ELSE '홀수'
END '결과'
FROM buyTbl;

-- 문자열 함수 =>  CONCAT(EXP...) : 문자열을 함께 출력할 때 사용 
-- CONCAT_WS(구분자, 문자열1, 문자열2 ...) : 문자열을 구분자와 함께 표시 

SET @singer = 'Emily King';
SELECT CONCAT('Hello ', @singer,' World') AS '결과1', 
      CONCAT_WS('/','Hello', 'World', 'MySQL', @SINGER) AS '결과2';

-- CONCAT()이용해서 하나의 컬럼에 2개의 컬럼값 표시 (단가  X  수량 = 입금액)
SELECT * FROM buyTbl;
SELECT prodName, price, amount, price*amount 
      FROM buyTbl LIMIT 3;

-- CONCAT()이용해서 하나의 컬럼에 3개의 컬럼값 표시         
SELECT prodName, 
      concat(price,' X', amount, ' = ', price*amount ) AS '가격*수량'
      FROM buyTbl LIMIT 3;

/* 퀴즈 - CONCAT() 활용 
 usertbl 테이블에서 키가 175 넘는 레코드만 추출한 후 아래와 같은 형태로 출력하여라.  
        이름          키   
 가수이름 => 김경호   ?  cm
 가수이름 => 이승기   ?  cm 
 */
 SELECT CONCAT('가수이름 => ',name) '이름', CONCAT (height,' cm') '키' 
 FROM usertbl WHERE height > 175;


-- 소숫점 자리 표시  => FORMAT(숫자, 소숫점 자릿수)        
SET @X = 123.456789;
SELECT @X, FORMAT(@X, 2), FORMAT(@X, 5);

-- 각 종목의 평균 가격을 groupName을 기준으로 정렬하여 표시하기 
SELECT groupName, FORMAT(AVG(price),2) '평균가격' 
FROM buytbl GROUP BY groupName ORDER BY groupName;


-- 특정 글자로 교체하기 
-- INSERT(문자열, 시작위치(인덱스처럼 0부터 시작 X , 1부터 시작함), 길이, 교체문자열)
-- REPLACE(문자열, 원래문자열, 교체문자열)
SET @mobile = '010-1234-5678';
SELECT INSERT (@mobile,5,4,'****') 'INSERT문 개인정보보호',
	   REPLACE (@mobile,'1234','****') 'REPLACE 개인정보보호';

