-- employees + dept_emp + departments 
-- emp_no, birth_date, first_name, last_name, gender, hire_date
-- emp_no, dept_no(부서번호), from_date(부서근무시작일), to_date(부서근무마지막날짜)
-- dept_no(부서번호), dept_name(부서명) 
SELECT * 
FROM dept_emp DE
    INNER JOIN employees E ON DE.emp_no = E.emp_no
    INNER JOIN departments D ON DE.dept_no = D.dept_no;
    
-- 사원번호, 이름, 부서번호, 부서명, 성별
SELECT 
    DE.emp_no AS '사원번호',
    concat(E.first_name,' ', E.last_name) AS '사원이름',
    D.dept_no AS '부서번호',
    D.dept_name AS '부서명',
    E.gender AS '성별'
FROM dept_emp DE
      INNER JOIN employees E ON DE.emp_no = E.emp_no
      INNER JOIN departments D ON DE.dept_no = D.dept_no;


-- 사원번호, 이름, 부서번호, 부서명, 성별 필드 출력 
-- 성별은 여자,  정렬 기준은 이름  
SELECT 
   DE.emp_no AS '사원번호',
    concat(E.first_name,' ', E.last_name) AS '사원이름',
    D.dept_no AS '부서번호',
    D.dept_name AS '부서명',
    E.gender AS '성별'
 FROM dept_emp DE
      INNER JOIN employees E ON DE.emp_no = E.emp_no
	  INNER JOIN departments D ON DE.dept_no = D.dept_no
 WHERE E.gender = 'F' ORDER BY 사원이름 LIMIT 10;
 
-- ======================================================= 
-- 1. 현재 근무 중인 직원 정보를 출력하시오.(employees 테이블과 dept_emp 테이블 조인 )
-- 현재 근무 중은? to_date='9999-01-01'
/*
사원번호  이름  성별   입사일(hire_date)  현재 근무중 
  ?      ?   ?           ?       9999-01-01 
*/

 SELECT 
		DE.emp_no AS '사원번호',
		concat(E.first_name,' ', E.last_name) AS '이름',
		E.gender AS '성별',
		E.hire_date '입사일',
		DE.to_date '현재근무중'
FROM dept_emp DE
	 INNER JOIN employees E ON DE.emp_no = E.emp_no;
    
-- 2. 현재 근무 중인 직원의 모든 정보(수행업무 포함) 를 출력하시오.
-- 현재 근무 중은? to_date='9999-01-01'
-- Step1 : employees 테이블과 title 테이블 조인 
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가 
/*
사원번호  이름   성   직무(title)  현재 근무중 
  ?      ?    ?        ?     9999-01-01 
*/
 SELECT 
		DE.emp_no AS '사원번호',
		concat(E.first_name,' ', E.last_name) AS '이름',
		D.dept_name '직무',
		DE.to_date '현재근무중'
FROM dept_emp DE
	 INNER JOIN employees E ON DE.emp_no = E.emp_no
     INNER JOIN departments D ON DE.dept_no = D.dept_no;
     
-- 3. 현재 근무 중인 부서명를 출력하시오. (사원번호, 사원명, 부서코드, 부서명)
-- 3개의 테이블 조인 
-- Step1 : dept_emp , employees, departments 테이블에서 
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가 
/*
사원번호  사원명  부서코드(dept_no)  부서명(dept_name)  현재 근무중 
  ?      ?        ?               ?             9999-01-01 

*/
 SELECT 
      DE.emp_no AS '사원번호',
      concat(E.first_name,' ', E.last_name) AS '사원명',
      D.dept_no '부서코드',
	  D.dept_name '부서명',
      DE.to_date '현재근무중'
FROM dept_emp DE
     INNER JOIN employees E ON DE.emp_no = E.emp_no
     INNER JOIN departments D ON DE.dept_no = D.dept_no
WHERE DE.to_date = '9999-01-01';


-- 4. 가장오래 근무한 직원 10명의 현재 부서를 출력하시오.
-- 3개의 테이블 조인 
-- Step1 : dept_emp , employees, departments 테이블에서 
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가 
-- Step3 : ORDER BY hire_date 정렬 옵션과 LIMIT 10 출력레코드 수 추가 
 SELECT 
		DE.emp_no AS '사원번호',
		concat(E.first_name,' ', E.last_name) AS '사원명',
        D.dept_name '부서명',
        E.hire_date '입사일',
		DE.to_date '현재근무중'
FROM dept_emp DE
	 INNER JOIN employees E ON DE.emp_no = E.emp_no
     INNER JOIN departments D ON DE.dept_no = D.dept_no
WHERE DE.to_date = '9999-01-01' ORDER BY hire_date LIMIT 10;




 -- 부서별로 직원수 표시. 부서 이름도 함께 표시한다. 현재근무중, group by, count()
SELECT * 
FROM dept_emp DE
    INNER JOIN departments D
    ON DE.dept_no = D.dept_no
WHERE DE.to_date = '9999-01-01';
 
SELECT D.dept_name AS '부서명', count(*) AS '직원수'
FROM dept_emp DE
    INNER JOIN departments D
    ON DE.dept_no = D.dept_no
WHERE DE.to_date = '9999-01-01'
GROUP BY D.dept_name ORDER BY 직원수 DESC; 

-- 부서별로 직원의 성별 인원수로 표시. 부서 이름도 함께 표시한다. 현재근무중, group by, count()
/*
  부서명    성별   직원수 
  Sales    M     ?
  Sales    F     ?
  ...
*/
 SELECT 
	  D.dept_name '부서명',
	  E.gender '성별',
      count(*) '직원수'
FROM dept_emp DE
     INNER JOIN employees E ON DE.emp_no = E.emp_no
     INNER JOIN departments D ON DE.dept_no = D.dept_no
WHERE DE.to_date = '9999-01-01'
GROUP BY D.dept_name, E.gender 
ORDER BY D.dept_name, E.gender DESC LIMIT 10;



--  급여 평균이 가장 높은 부서 5개만 출력하여라 
--  dept_emp + departments + salaries
show tables;
select * from salaries; -- 사원번호, 급여, from-date, to_date 
/*
부서명              평균급여
   ?                ?
   ?                ?
   ... 
*/

SELECT 
	  D.dept_name '부서명',
	  AVG(S.salary) '급여평균'
FROM dept_emp DE
     INNER JOIN salaries S ON DE.emp_no = S.emp_no
     INNER JOIN departments D ON DE.dept_no = D.dept_no
WHERE DE.to_date = '9999-01-01'
GROUP BY D.dept_name
ORDER BY 급여평균 DESC LIMIT 5;

/* ===========================================================================
외부조인 (OUTER JOIN) 조인의 조건에 만족되지 않는 행까지도 포함시킴
LEFT는 FROM 다음에 적은 테이블 (먼저 작성한 테이블), RIGHT는 OUTER JOIN 뒤에 적은 테이블 (나중에 작성한 테이블)이며
LEFT는 FROM 다음에 적은 테이블의 레코드를 다보여주겠다, 
RIGHT은 OUTER JOIN 뒤에 적은 테이블의 레코드를 다 보여주겠다 (오른쪽에 해당하는 테이블의 모든 레코드 모두 표시하겠다)...
UNION은 왼쪽,오른쪽 해당하는 테이블의 레코드 모두 출력

SELECT * 또는 컬럼명 
   FROM 테이블1
     <LEFT/RIGHT/UNION> OUTER JOIN 테이블2
        ON 조인될조건:테이블1.컬럼명 = 테이블2.컬럼명  
				(서로 공통된 관계의 컬럼이용)
   [WHERE 조건절];
*/

-- LEFT OUTER JOIN
-- 전체회원의 구매기록 확인하기. 구매기록이 없는 회원도 모두 출력되어야 한다.
-- 왼쪽에 정의된 테이블 userTbl의 레코드가 모두 표시되어야한다. 구매경력이 없는 회원 레코드도 모두 출력 

USE SQLDB;
SELECT * 
   FROM userTbl U
    LEFT OUTER JOIN buytbl B
    ON U.userID = B.userID
    ORDER BY U.userID;

SELECT count(*)
   FROM userTbl U
    LEFT OUTER JOIN buytbl B
    ON U.userID = B.userID
    ORDER BY U.userID;
    
-- RIGHT OUTER JOIN
SELECT * 
   FROM userTbl U
    RIGHT OUTER JOIN buytbl B
    ON U.userID = B.userID
    ORDER BY B.userID;

SELECT count(*) 
   FROM userTbl U
    RIGHT OUTER JOIN buytbl B
    ON U.userID = B.userID
    ORDER BY B.userID;    
    
    
    
-- stdTbl + stdclubTbl
-- <<이너조인>> : 동아리에 가입한 학생 
SELECT  *  FROM stdTbl S
INNER JOIN  stdclubTbl SC ON S.stdName = SC.stdName;  
        
SELECT count(*) -- 6 
FROM stdTbl S INNER JOIN  stdclubTbl SC ON S.stdName = SC.stdName;     
        

-- <<아우터 조인>> : stdTbl, 동아리에 가입하지 않은 학생 목록도 출력한다. 
SELECT  * FROM stdTbl S
LEFT OUTER JOIN  stdclubTbl SC ON S.stdName = SC.stdName;  

SELECT count(*) -- 7
FROM stdTbl S
LEFT OUTER JOIN  stdclubTbl SC ON S.stdName = SC.stdName;  

-- 동아리에 가입하지 않은 학생 레코드만 출력하여라
SELECT  *  FROM stdTbl S
LEFT OUTER JOIN  stdclubTbl SC ON S.stdName = SC.stdName
WHERE SC.stdName IS NULL;  


-- =======================================================
-- 퀴즈 : stdTbl, clubtbl, stdclubtbl 테이블에서
-- 동아리를 기준으로 가입한 학생 목록을 OUTER JOIN을 이용하여 출력하여라.
-- 이때 가입학생이 아무도 없는 동아리 목록도 출력한다.
-- 동아리명  동아리번호  학생이름  지역 
--   ?       ?       ?     ?

SELECT * FROM stdTbl; -- strName,addr
SELECT * FROM stdclubTbl; -- num, stdName, clubName
SELECT * FROM clubTbl; -- clubName, roomNo

SELECT SC.clubName '동아리명', C.roomNo '동아리 방번호', SC.stdName '학생이름', S.addr '지역'
FROM stdTbl S 
LEFT OUTER JOIN stdclubTbl SC ON S.stdName = SC.stdName
RIGHT OUTER JOIN clubTbl C ON C.clubName = SC.clubName;

-- 강사님 답
SELECT 
   C.clubName AS '동아리명', 
   C.roomNo AS '동아리방', 
   S.stdName AS '학생 이름', 
   S.addr AS '지역'
FROM stdTbl S
      LEFT OUTER JOIN stdclubtbl SC ON S.stdName = SC.stdName
      RIGHT OUTER JOIN clubtbl C  ON SC.clubName = C.clubName
ORDER BY C.clubName;   
    
    
    
    
    
    
    
    
-- =======================================================    
-- 전체 아우터 조인 : FULL OUTER JOIN  => UNION 명령을 이용해서 조인한 모든 레코드 출력하기 
/*
SELECT 조인 명령1 
   UNION
SELECT 조인 명령2; 
*/

-- stdTbl, clubtbl, stdclubtbl 테이블에서 
-- 학생을 기준으로 동아리 학생 목록을 OUTER JOIN을 이용하여 출력하여라. 
-- 이때 동아리에 가입하지 않은 학생 목록과 가입학생이 없는 동아리 목록도 함께 출력한다.
-- UNION 활용. SELECT 문에 컬럼명이 같아야 한다. 
 
 SELECT 
   S.stdName AS '이름', S.addr AS '지역', 
   C.clubName AS '동아리명', C.roomNo AS '동아리방'
   FROM stdTbl S
      LEFT OUTER JOIN stdclubtbl SC
         ON S.stdName = SC.stdName
        LEFT OUTER JOIN clubtbl C
         ON SC.clubName = C.clubName 
UNION
SELECT 
   S.stdName AS '이름', S.addr AS '지역', 
    C.clubName AS '동아리명', C.roomNo AS '동아리방' 
   FROM stdTbl S
      LEFT OUTER JOIN stdclubtbl SC
         ON S.stdName = SC.stdName
        RIGHT OUTER JOIN clubtbl C
         ON SC.clubName = C.clubName;







-- =======================================================
-- 크로스 조인 (상호조인) => 키가 정의되어 있지 않아도 되고 모든행이 반복됨 
-- 카티션곱 => 한쪽 테이블의 모든 행과 다른쪽 테이블의 모든 행이 조인됨
/* SELECT * 또는 컬럼명
      FROM 테이블1 
        CROSS JOIN 테이블2; */
        
-- buyTbl, userTbl 테이블에서 CROSS JOIN을 적용하여라. 
SELECT * FROM buyTbl CROSS JOIN userTbl;
SELECT count(*) FROM buyTbl CROSS JOIN userTbl;  









-- =======================================================
-- 셀프 조인(자체 조인) => INNER JOIN의 일종. 같은 테이블을 조인, 조직도등에 이용  
-- sqlDB 안에 empTBL 테이블 생성 
DROP TABLE IF EXISTS empTbl;
CREATE TABLE empTbl 
   (emp CHAR(4), manager CHAR(4), empTel VARCHAR(8));

INSERT INTO empTbl VALUES('나사장',NULL,'0000');
INSERT INTO empTbl VALUES('김재무','나사장','2222');
INSERT INTO empTbl VALUES('김부장','김재무','2222-1');
INSERT INTO empTbl VALUES('이부장','김재무','2222-2');
INSERT INTO empTbl VALUES('우대리','이부장','2222-2-1');
INSERT INTO empTbl VALUES('지사원','이부장','2222-2-2');
INSERT INTO empTbl VALUES('이영업','나사장','1111');
INSERT INTO empTbl VALUES('한과장','이영업','1111-1');
INSERT INTO empTbl VALUES('최정보','나사장','3333');
INSERT INTO empTbl VALUES('윤차장','최정보','3333-1');
INSERT INTO empTbl VALUES('이주임','윤차장','3333-1-1');

SELECT * FROM empTBL;
SELECT COUNT(*) FROM empTBL;
    
SELECT * FROM empTbl A 
INNER JOIN empTbl B ON A.manager = B.emp;

SELECT A.emp '사원명', A.manager '상관명', A.empTel '사원구내번호', B.manager '상관의 상관명', B.empTel '상관구내번호' FROM empTbl A 
INNER JOIN empTbl B ON A.manager = B.emp;

-- 우대리 직원의 상관의 구내번호를 찾기 / 직원(emp), 상관(manager), 구내번호(empTel) 
SELECT A.emp '사원명', A.manager '상관명', B.empTel '상관구내번호' FROM empTbl A 
INNER JOIN empTbl B ON A.manager = B.emp
WHERE a.emp = '우대리';

-- 강사님 답
 SELECT B.empTel AS '우대리의 상관구내번호' FROM empTBL A
 INNER JOIN empTBL B ON A.manager = B.emp WHERE A.emp = '우대리';   
 
 
 
 
 
 
 
 
 -- =======================================================
-- UNION / UNION ALL => 쿼리의 결과를 합쳐서 보여준다. 
-- (UNION 중복 허용 X, UNION ALL 중복 허용)

-- SELECT ... -- 쿼리1
-- UNION / UNION ALL
-- SELECT ... -- 쿼리2

SELECT * FROM clubtbl; -- 동아리정보 
SELECT * FROM stdtbl; -- 학생정보 
SELECT * FROM stdclubTbl; -- 학생동아리정보 
    
-- 동아리 이름     
SELECT clubName FROM clubtbl;
-- 학생 이름     
SELECT stdName FROM stdtbl;  

-- 동아리 이름     
SELECT clubName FROM clubtbl
UNION
SELECT stdName FROM stdtbl; 

-- 중복 X "UNION"
SELECT clubName AS '결과' FROM clubtbl 
UNION
SELECT clubName FROM stdclubTbl;  

-- 중복 O "UNION ALL"
SELECT clubName AS '결과' FROM clubtbl 
UNION ALL
SELECT clubName FROM stdclubTbl;  





-- =======================================================
-- NOT IN : 첫번째 쿼리의 결과중 두번째 쿼리에 해당하는 것을 제외 
-- IN : 두번째 쿼리의 결과만 조회 

-- SELECT 첫번째 쿼리 
--   WHERE ... [NOT IN / IN ] ( SELECT 두번째 쿼리 )

-- SELECT * 또는 컬럼명 FROM 테이블1
--    WHERE 조건절1 NOT IN 또는 IN ( SELECT * 또는 컬럼명 FROM 테이블2 WHERE 조건절2) ;

-- 전화가 없는 사람을 출력 
SELECT name FROM userTbl WHERE mobile1 IS NULL;

SELECT name, CONCAT(mobile1, mobile2) AS '전화번호' FROM userTbl
WHERE name NOT IN (SELECT name FROM userTbl WHERE mobile1 IS NULL); -- 조건에 포함되지 않는 결과 출력 (사용자중 전화가 없는 사람을 제외하고 싶다. NOT IN)

SELECT name, CONCAT(mobile1, mobile2) AS '전화번호' FROM userTbl
WHERE name IN (SELECT name FROM userTbl WHERE mobile1 IS NULL); -- 조건에 포함되는 결과를 출력 (사용자중 전화가 없는 사람만 조회 IN)






-- =======================================================
-- 뷰(View)란?
-- 테이블 자료의 일부만 보여주고자 할 때 사용하는 기능, 원본 데이터중에서 보는 사람에게 필요한 데이터만을 보여줌
-- 장점 : 보안, 복잡한 쿼리의 단순화 등

-- 쇼핑몰 예) 
-- 메인 관리자 화면 - 매출액 , 상품목록, 주문목록
-- 부 관리자 화면 - 상품목록, 주문목록 

-- 뷰의 생성과 삭제
/*
(삭제) DROP VIEW IF EXISTS 뷰이름;
(생성) CREATE VIEW 뷰이름
	  ASv_buytbl
	  SELECT 구문
*/

-- 뷰 호출 : 테이블처럼 호출, 뷰를 테이블이라고 생각해도 무방 =>  SELECT * FROM 뷰이름;
-- num, userID, price, amount => v_buyTbl  뷰 생성 
CREATE VIEW v_buyTbl AS SELECT num, userID, price, amount FROM buyTbl;
-- 뷰의 레코드 확인     
SELECT * FROM v_buyTbl;   

-- 뷰 목록 확인 1
-- 워크벤치의 [Navigator] -[SCHEMAS] 탭에서 새로고침한 후 데이타베이스 목록 아래에 [Views] 클릭한 후 목록 확인

-- 뷰 목록 확인 2,  VIEW 로 확인 
-- SHOW FULL TABLES IN 데이타베이명;
SHOW FULL TABLES IN sqldb;
SHOW FULL TABLES IN sqldb WHERE Table_type = 'VIEW';
   
 -- 뷰 삭제
-- DROP VIEW IF EXISTS 뷰이름;
DROP VIEW IF EXISTS v_buyTbl;
SHOW FULL TABLES IN sqldb WHERE Table_type = 'VIEW';  
    
-- 예제에 사용될 테이블 만들기 
-- userTbl = > userTbl_a
CREATE TABLE userTbl_a ( SELECT * FROM userTbl );
SHOW TABLES;
SELECT * FROM userTbl_a;
-- 필수 필드명 확인하기 userID, name, birthYear, addr
DESC userTbl_a;

-- userTbl_a 테이블에서 필수 항목으로 구성된 뷰 생성 
-- v_userTbl_a => userID, name, birthYear, addr
CREATE VIEW v_userTbl_a
   AS 
   SELECT userID, name, birthYear, addr FROM userTbl_a;
      
SHOW FULL TABLES IN sqldb
WHERE Table_type = 'VIEW';

-- 뷰를 통한 레코드 데이타 삽입(뷰에서 등록한 컬럼의 데이타만 삽입 가능)
-- INSERT INTO 뷰이름 (컬럼명1, 컬럼명2 ... ) VALUES (값1, 값2 ... );
-- INSERT INTO 뷰이름 VALUES (값1, 값2 ... );
INSERT INTO v_userTbl_a (userID, name, birthYear, addr) VALUES ('KJK', '김종국', 1977, '안양');
INSERT INTO v_userTbl_a VALUES ('KKD', '고길동', 1960, '제주');

SELECT * FROM v_userTbl_a;
SELECT * FROM userTbl_a;

-- 전남 => 남원 
UPDATE v_userTbl_a SET addr = '남원' 
WHERE  addr = '전남'; 

SELECT * FROM v_userTbl_a;
SELECT * FROM userTbl_a;

-- 복사본 테이블 생성 
-- buytbl => buyA (userID, prodName, price, amount) 
CREATE TABLE buyA (
      SELECT userID, prodName, price, amount FROM buytbl);
SHOW TABLES;
SELECT * FROM buyA;

-- 뷰 생성 (테이블 별칭 이용)
CREATE VIEW v_buyA AS 
SELECT userID AS id, prodName AS pName, price, amount AS cnt
FROM buyA;

-- v_buyA 뷰에서 사용자별로 구매(price*cnt) 구하기 
SELECT  id AS '사용자 아이디', sum(price*cnt) AS '총구매액'
FROM v_buyA GROUP BY id;


-- =======================================================
-- 퀴즈 1. employees 테이블에서 사원번호, 이름, 성별, 생년월일로 구성된
--        복사본 테이블 empA 테이블을 생성하여라. (필드명은 별칭 이용) 
SELECT * FROM employees;
CREATE TABLE empA 
(SELECT emp_no '사원번호', CONCAT(first_name,' ', last_name) '이름', gender '성별', birth_date '생년월일' FROM employees); 

-- 퀴즈 2. empA 테이블의 뷰 v_empA를 생성하여라.
CREATE VIEW v_empA AS SELECT * FROM empA;
SELECT * FROM v_empA;

-- 퀴즈 3. 뷰 v_empA를 이용하여 나이가 제일 적은 사원 레코드 10개를 출력하여라.
SELECT * FROM v_empA ORDER BY 생년월일 DESC LIMIT 10;

-- 퀴즈 4. 뷰 v_empA를 이용하여 이름이 'd'로 끝나는 사원만 삭제하여라
DELETE FROM v_empA WHERE 이름 LIKE '%d';

-- 퀴즈 5. 뷰 v_empA를 이용하여 사원번호 10501~10503인 사원의 레코드를 삽입하여라.
--          나머지 레코드의 데이타는 임의로 한다.
INSERT INTO v_empA VALUES (10501,'multi campus','F','2020-11-24'),(10502,'python class','M','2020-11-23'),(10503,'mysql class','F','2020-11-24');

-- 퀴즈 6. 뷰 v_empA를 이용하여 'A'로 시작하는 사원 이름을 검색하여
--        이름 모두를 대문자로 수정하여라. (first_name, last_name 모두 대문자), upper(필드명)  문자열 함수 이용
SELECT 사원번호, IF(이름 LIKE 'A%', UPPER(이름), 이름) '이름', 성별, 생년월일 
FROM v_empA 
WHERE 이름 LIKE 'A%';

-- LOWER => 소문자
SELECT 사원번호, IF(이름 LIKE 'A%', LOWER(이름), 이름) '이름', 성별, 생년월일 
FROM v_empA 
WHERE 이름 LIKE 'A%';

-- 대문자
UPDATE v_empA SET 이름 = UPPER(이름) WHERE 이름 LIKE 'A%';

-- 소문자
UPDATE v_empA SET 이름 = UPPER(이름) WHERE 이름 LIKE 'A%';
