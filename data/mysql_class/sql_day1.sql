-- 한줄 주석
-- select * from employees;

/*
여러줄 주석
select emp_no, first_name 
from employees;

select emp_no , first_name
from employees;
*/

-- 마지막 세미콜론 필수

-- 워크벤치에서 DB접속 => USE 데이터베이스명
use employees;

-- 현 계정에 있는 DB확인 =
show databases;

-- 선택한 DB의 테이블 정보 조회
show table status;

-- 테이블 이름만 간단히 보기
show tables;


-- world db의 테이블 정보 조회
use world;
show tables;

-- 테이블 구조 확인 => DESCRIBE(DESC) 테이블명;
use employees;
describe employees.titles;
desc salaries;

-- 테이블 레코드 표시하기 : SELECT
-- SELECT * FROM 데이타베이스명.테이블명;
-- SELECT * FROM 테이블명;

-- titles 테이블의 모든 레코드 확인하기 
SELECT * FROM titles;
-- employees 테이블의 모든 레코드 확인하기 
SELECT * FROM employees;
-- employees 테이블의 모든 레코드 확인하기 
SELECT * FROM dept_emp;
SELECT * FROM employees.dept_emp;

USE employees;
DESC employees; -- employees 테이블의 구조 확인하기 

-- employees 테이블에서 emp_no, first_name, last_name 필드만 출력 
SELECT * FROM employees;
SELECT emp_no, first_name, last_name FROM employees;

-- employees 접속상태인데 잠시 worlddb 데이타베이스의 city 테이블 확인 : SELECT * FROM 데이타베이스명.테이블명;
USE employees;
SELECT * FROM worlddb.city;

-- *****************************************************************
-- 책 p.194 실습예제 만들기, sqldb DB : userTbl, buyTbl
create database sqlDB;
show databases; -- 생성됐는지 확인
use sqlDB; -- 생성한 DB로 이동

-- 회원 테이블 생성
CREATE TABLE userTbl 
( userID     CHAR(8) NOT NULL PRIMARY KEY, -- 사용자 아이디(PK)
  name       VARCHAR(10) NOT NULL, -- 이름
  birthYear   INT NOT NULL,  -- 출생년도
  addr        CHAR(2) NOT NULL, -- 지역(경기,서울,경남 식으로 2글자만입력)
  mobile1   CHAR(3), -- 휴대폰의 국번(011, 016, 017, 018, 019, 010 등)
  mobile2   CHAR(8), -- 휴대폰의 나머지 전화번호(하이픈제외)
  height       SMALLINT,  -- 키
  mDate       DATE  -- 회원 가입일
);

-- 회원 구매 테이블
CREATE TABLE buyTbl 
(  num       INT AUTO_INCREMENT NOT NULL PRIMARY KEY, -- 순번(PK)
   userID     CHAR(8) NOT NULL, -- 아이디(FK)
   prodName    CHAR(6) NOT NULL, --  물품명
   groupName    CHAR(4)  , -- 분류
   price        INT  NOT NULL, -- 단가
   amount       SMALLINT  NOT NULL, -- 수량
-- usrTbl의 userID를 참조. 외래키로 정의 
   FOREIGN KEY (userID) REFERENCES userTbl(userID)
);

show tables;
desc buytbl;
desc usertbl;

select * from buytbl;  -- 구조만 만들어놓아서 아직 껍데기 

-- 각각의 테이블안에 레코드 삽입
insert into usertbl values('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
SELECT * FROM usertbl;

-- 나머지 레코드 삽입후 확인하기 
INSERT INTO userTbl VALUES('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');
INSERT INTO userTbl VALUES('KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7');
INSERT INTO userTbl VALUES('JYP', '조용필', 1950, '경기', '011', '4444444', 166, '2009-4-4');
INSERT INTO userTbl VALUES('SSK', '성시경', 1979, '서울', NULL  , NULL      , 186, '2013-12-12');
INSERT INTO userTbl VALUES('LJB', '임재범', 1963, '서울', '016', '6666666', 182, '2009-9-9');
INSERT INTO userTbl VALUES('YJS', '윤종신', 1969, '경남', NULL  , NULL      , 170, '2005-5-5');
INSERT INTO userTbl VALUES('EJW', '은지원', 1972, '경북', '011', '8888888', 174, '2014-3-3');
INSERT INTO userTbl VALUES('JKW', '조관우', 1965, '경기', '018', '9999999', 172, '2010-10-10');
INSERT INTO userTbl VALUES('BBK', '바비킴', 1973, '서울', '010', '0000000', 176, '2013-5-5');


-- 첫번째 컬럼명 NULL로 준 이유: create table 할 때 자동숫자증감(AUTO_INCREMENT) 지정해줬기 때문 
INSERT INTO buyTbl VALUES(NULL, 'KBS', '운동화', NULL   , 30,   2);
INSERT INTO buyTbl VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1);
INSERT INTO buyTbl VALUES(NULL, 'JYP', '모니터', '전자', 200,  1);
INSERT INTO buyTbl VALUES(NULL, 'BBK', '모니터', '전자', 200,  5);
INSERT INTO buyTbl VALUES(NULL, 'KBS', '청바지', '의류', 50,   3);
INSERT INTO buyTbl VALUES(NULL, 'BBK', '메모리', '전자', 80,  10);
INSERT INTO buyTbl VALUES(NULL, 'SSK', '책'    , '서적', 15,   5);
INSERT INTO buyTbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   2);
INSERT INTO buyTbl VALUES(NULL, 'EJW', '청바지', '의류', 50,   1);
INSERT INTO buyTbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);
INSERT INTO buyTbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   1);
INSERT INTO buyTbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);


SELECT * FROM usertbl;
SELECT * FROM buyTbl;

-- 테이블의 레코드수 확인하기 => SELECT count(*) FROM 테이블명;
SELECT count(*) FROM usertbl;
SELECT count(*) FROM buytbl; -- 순차적으로 번호 들어갔는지 확인 

-- *****************************************************************
-- where 절로 조건에 맞는 레코드 출력하기 
-- SELECT 컬러명1, 컬럼명2.. 또는 * FROM 테이블명 WHERE 조건절
-- WHERE 조건절 : 비교연산자(>,<,=, >=, <=) 논리연산자(AND, OR, NOT)

use sqldb;
SELECT num, userid FROM buytbl;

select * from userTbl where name='은지원';
select * from userTbl where height >= 180;


-- WHERE 컬럼명 BETWEEN 값1 AND 값2
-- 연속적인 값 사이에서 검색 

-- userTbl 테이블에서 아래 조건의 레코드 출력하기 
-- birthYear 이 1970 (AND, 보다 크거나 같고)(OR, 이거나) height 이 182보다 크다 
SELECT * FROM userTbl 
WHERE birthYear >= 1970 AND height > 182;

SELECT * FROM userTbl
WHERE birthYear >= 1970 OR height > 182;

SELECT userID, name FROM userTbl
WHERE height >= 180 and height <=183;

SELECT userID, name FROM userTbl 
WHERE height BETWEEN 180 and 183;  

-- BETWEEN..AND 연산자 : 범위를 지정할 때 사용 => WHERE 컬럼명 BETWEEN 값1 AND 값2
-- 연속적인 값 사이에서 검색 
-- userTbl 테이블에서 아래 조건의 레코드 출력하기 (BETWEEN..AND 연산자)         
-- height이 180~183 인 레코드에서 userID, Name, height 컬럼의 레코드 표시 
SELECT userID, Name, height FROM userTbl 
WHERE height BETWEEN 180 AND 183;

-- QUIZ
desc buyTbl;
select userid, prodname from buyTbl;
select * from buyTbl where userid = 'KBS';
select * from buyTbl where amount >= 5;
select * from buyTbl where prodname='청바지' or prodname= '운동화';
select * from buyTbl where prodname in ('청바지', '운동화');
select * from buyTbl where price between 30 and 80;
select * from buyTbl where price >= 30 and price <= 80; 


-- IN 연산자 특정값 만족 => WHERE 컬럼명 IN (값1, 값2 ...)
-- userTbl 테이블에서 addr 컬럼값이 경남, 전남, 경북인 레코드에서 Name, addr 컬럼만 출력하기 
-- OR, = 연산자 이용 
SELECT name, addr FROM userTbl
WHERE addr = '경남' OR addr = '전남' OR addr = '경북';
-- IN 연산자 이용         
SELECT name, addr FROM userTbl
WHERE addr IN ('경남','전남','경북');        

-- LIKE 연산자 이용 : 컬럼명의 데이터가 문자열인 경우 적용
-- 문자열이 내용 검색 LIKE ..%(모든 것, 무엇이든 = 글자수 제한 없음) 
-- 문자열이 내용 검색 LIKE _(글자수)..
SELECT * FROM userTbl WHERE name LIKE '김%';
SELECT * FROM userTbl WHERE name LIKE '김_수';

-- 서브쿼리 (값 하나여야 함)
SELECT name, height FROM userTbl      
WHERE height >= (SELECT height FROM userTbl WHERE name = '김경호');


-- any를 이용한 서브쿼리문 (서브쿼리는 값이 하나로 반환되어야 함, BUT, 서브쿼리 앞에 ANY를 쓰면 서브쿼리 값 여러개 가능)
-- 즉, 서브쿼리의 결과값이 한개이상인 경우 사용 
-- SELECT .. FROM.. WHERE  조건절1 
--      any(SELECT .. FROM.. WHERE 조건절2 )
SELECT height, addr  FROM userTbl 
WHERE height >= ANY (SELECT height  FROM userTbl WHERE addr = '경남');

-- 은지원과 김범수와 같은 고향(addr)인 레코드를 출력하여라. 
-- 서브쿼리 X
SELECT addr FROM userTbl WHERE name IN ('은지원', '김범수'); 
SELECT * FROM userTbl WHERE addr IN ('서울','경남');               
            
-- 서브쿼리 O
SELECT * FROM userTbl 
WHERE addr = ANY (SELECT addr FROM userTbl WHERE name IN ('은지원', '김범수'));

 
-- 정렬, 역정렬 => 결과가 출력되는 순서를 조절하는 구문 
-- 오름차순(ASCENDING) : ORDER BY 컬럼명, 기본값
-- 내림차순(DESCENDING) : ORDER BY 컬럼명 DESC;

-- mDate 컬럼명 기준으로 레코드 정렬 
SELECT * FROM userTbl
ORDER BY mDate;

-- mDate 컬럼명 기준으로 레코드 역정렬 
SELECT * FROM userTbl
ORDER BY mDate DESC;

-- 정렬기준 여러개         
-- SELECT 필드명나열|* FROM 테이블명 
-- WHERE 조건절 
-- ORDER BY 컬럼명1 (DESC|ASC), 컬럼명2 (DESC|ASC)
  
-- 2개의 컬럼명(height, name)으로 정렬. 키가 큰 순서로 정렬하되 만약 키가 같다면 이름순으로 정렬(키는 오름차순, 이름은 내림차순)
SELECT * FROM userTbl ORDER BY height ASC, name DESC;
-- 고향(addr)은 내림차순, 이름은 오름차순
SELECT * FROM userTbl ORDER BY addr DESC, name ASC;

-- WHERE 절이 있는 경우의 정렬 
-- mobile1 값이 011인 레코드를 name 오름차순으로 정렬 
SELECT * FROM userTbl WHERE mobile1 = '011'
ORDER BY name ASC;

-- 중복을 제거하는 DISTINCT => SELECT [DISTINCT] 컬럼명|* FROM 테이블명 [WHERE절...] [ORDER BY ...];
-- userTbl 테이블에서 지역(addr) 컬럼값을 중복없이 표시하여라.
SELECT DISTINCT addr FROM userTbl ORDER BY addr;

-- LIMIT는 레코드 출력수 제한, 마지막에 지정 
-- SELECT * | 필드명 FROM 테이블 WHERE 절  ORDER BY 절  LIMIT 숫자1, 숫자2;
SELECT * FROM usertbl ORDER BY name LIMIT 5 ;

-- userTbl 테이블에서 이름 가나다순으로 정렬한 후 레코드를 3개만 출력
SELECT * FROM userTbl ORDER BY NAME ASC LIMIT 3;

-- userTbl 테이블에서 키가 가장 큰 사람의 이름 (응용)
SELECT * FROM userTbl ORDER BY height DESC LIMIT 1;

-- LIMIT 중복 사용(순서(범위) 지정 방법)
-- ORDER BY 결과의 전체 행에서 인덱스(4)부터 2개의 값 결과 반환으로 LIMIT
-- 파이썬과 동일하게 0부터 시작이기 때문에 4번째 행에 위치한 성시경부터 2개의 레코드 반환됨
-- LIMIT 시작인덱번호, 갯수. 즉, 시작인덱스는 0부터 시작  
SELECT * FROM userTbl ORDER BY name LIMIT 3,2; 

-- 키 2,3번쨰로 큰 사람의 레코드 출력
SELECT * FROM userTbl ORDER BY height DESC LIMIT 1,2; 


-- 기존 테이블 복사해서 새로운 테이블 만들기,기본 테이블의 데이타도 함께 복사 => CREATE TABLE 새테이블명 (SELECT */컬럼명 FROM 테이블명);
SELECT * FROM userTbl WHERE addr='서울';
CREATE TABLE userTbl_seoul(SELECT * FROM userTbl WHERE addr='서울');
SHOW TABLES;
SELECT * FROM userTbl_seoul;

-- userTbl 테이블에서 키순으로 정렬한 후 5등까지만 useTbl_height로 저장
CREATE TABLE userTbl_height(SELECT * FROM userTbl ORDER BY height LIMIT 5);
SELECT * FROM userTbl_height;

-- 테이블 삭제  =>  DROP TABLE 테이블명;
DROP TABLE userTbl_height;
DROP TABLE userTbl_seoul;


-- QUIZ
-- 1) buyTbl 테이블의 구조 확인하기 
-- 2) buyTbl 테이블에서 userID, prodName 컬럼만 출력하기 
-- 3) buyTbl 테이블에서 userID가 'KBS'인 레코드 출력하기 
-- 4) buyTbl 테이블에서 prodName 컬럼을 중복없이 출력하기 
-- 5) buyTbl 테이블에서 groupName이 NULL인 레코드 출력하기 (IS NULL 이용)
-- 6) buyTbl 테이블에서 amount가 5보다 큰 레코드 출력하기 
-- 7) buyTbl 테이블에서 prodName 컬럼이 '청바지' 이거나 '운동화'인 레코드 출력구문을 2가지로 방법으로 작성하기(OR, IN 사용)
-- 8) buyTbl 테이블에서 price 컬럼값이 30~80인 레코드 출력구문을 2가지 방법으로 작성하기(AND 구문, BETWEEN .. AND 구문 이용)
-- 9) buyTbl 테이블에서 userID에 'K'로 시작하는 레코드 출력하기 (LIKE 이용)
-- 10) buyTbl 테이블에서 prodName이 ??화로 끝나는 레코드 출력하기 (LIKE 이용)
-- 11) buyTbl 테이블에서 userID 컬럼값이 'JYP'인 price 컬럼값 보다 큰 레코드 출력하기(서브쿼리 이용)
-- 12) buyTbl 테이블에서 userID 컬럼값이 'JYP'인 amount 컬럼값과 같은 레코드 출력하기(서브쿼리 이용)
-- 13) buyTbl 테이블에서 price 컬럼값이 큰 순서대로 5개만 출력하기(ORDER BY, LIMIT) 이용
-- 14) buyTbl 테이블에서 userID 컬럼값이 'KBS'인 레코드 목록 중 price 컬럼값이 가장 작은 레코드 출력하기(WHERE, ORDER BY, LIMIT 이용) 
-- 15) userTbl 테이블에서 addr 컬럼값이 '서울'인 레코드만 복사해서 새로운 테이블 userTbl1 생성하기(CREATE TABLE ~ 이용) 
-- 16) userTbl 테이블에서 name 컬럼값이 '은지원'인 레코드의 height 컬럼값보다 
--  큰 레코드만 height 값을 기준으로 정렬하여 복사해서 새로운 테이블 userTbl2 생성하기 (CREATE TABLE ~ 이용)

-- 풀이
desc buyTbl;
select userid, prodname from buyTbl;
select * from buyTbl where userid = 'KBS';
SELECT DISTINCT prodName FROM buyTbl;
SELECT * FROM buyTbl WHERE groupName IS NULL;
select * from buyTbl where amount >= 5;
select * from buyTbl where prodname='청바지' or prodname= '운동화';
select * from buyTbl where prodname in ('청바지', '운동화');
select * from buyTbl where price between 30 and 80;
select * from buyTbl where price >= 30 and price <= 80; 
SELECT * FROM buyTbl WHERE userid LIKE 'K%';
SELECT * FROM buyTbl WHERE prodName LIKE '%화';
SELECT * FROM buyTbl;
SELECT * FROM buyTbl WHERE price >= ANY (SELECT price FROM buyTbl WHERE userID = 'JYP');
SELECT * FROM buyTbl WHERE amount = (SELECT amount FROM buyTbl WHERE userID = 'JYP');
SELECT * FROM buyTbl ORDER BY price DESC LIMIT 5; 
SELECT * FROM buyTbl WHERE userID = 'KBS' ORDER BY price LIMIT 1;
CREATE TABLE userTbl1(SELECT * FROM userTbl WHERE addr = '서울');
CREATE TABLE userTbl2
(SELECT * FROM userTbl WHERE height > 
					 (SELECT height FROM userTbl WHERE name = '은지원')ORDER BY height DESC);
SHOW TABLES;


-- QUIZ (2)
-- employees 데이타베이스의 employees 테이블 기준입니다. 
USE employees;
show table status;
DESC employees;

-- 1. 직원 이름이 빠른 순(A, B, C …) 순으로 리스트를 출력하시오.
SELECT * FROM employees ORDER BY first_name;

-- 2. 직원 나이가 적은 순으로 출력하시오.
SELECT * FROM employees ORDER BY birth_date DESC;

-- 3. 직원들의 업무(titles)에는 직원별로 업무가 저장되어 있다.  이 회사의 업무 종류 리스트를 구하시오.
SELECT * FROM titles;
SELECT DISTINCT title FROM titles; 

-- 4. 이 회사의 업무 종류 개수를 구하시오. (COUNT이용) => 잘 모르겠음...(?)
SELECT COUNT(*) 업무종류개수 FROM titles;

-- 5. 가장 최근에 입사한 사람 10명만 출력하시오
SELECT * FROM employees ORDER BY hire_date DESC LIMIT 10; 
SELECT * FROM EMPLOYEES ORDER BY hire_date;

-- 6. 급여가 가장 많은 사람 10명을 구하시오.
SELECT * FROM salaries ORDER BY salary DESC LIMIT 10;

-- 7. 급여가 가장 많은 사람 10명을 제외하고 다음 10명을 구하시오. 즉, 11등부터 20등 까지…
SELECT * FROM salaries ORDER BY salary DESC LIMIT 10,10;

-- 8. 입사한지 가장 오래된 사람의 이름은 무엇인가?
SELECT  first_name, last_name, hire_date FROM employees
WHERE hire_date = (SELECT hire_date FROM employees ORDER BY hire_date LIMIT 1);

-- 9. 성(last_name)이 Senzako, Pettis, Henseler인 직원을 출력하시오.
SELECT * FROM employees 
WHERE last_name IN ('Senzako','Pettis','Henseler');

-- 10. EMPLOYEES 테이블에서 성별이 남자인 레코드를 EMPLOYEES2 테이블로 생성하여라. 
CREATE TABLE EMPLOYEES2 (SELECT * FROM employees WHERE gender = 'M');
SHOW TABLES;
SELECT * FROM employees2;

-- 11. EMPLOYEES 테이블에서 레코드는 복사하지 않고  구조만 복사하여  EMPLOYEES3 테이블을  생성하여라. 
CREATE TABLE employees3 LIKE employees;
SELECT * FROM employees3;

-- 12. EMPLOYEES3 테이블을 삭제하여라 
DROP TABLE employees3;
