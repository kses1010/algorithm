## 모든 레코드 조회하기
문제 [링크](https://programmers.co.kr/learn/courses/30/lessons/59034)

```mysql
SELECT ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS ORDER BY ANIMAL_ID;
``` 

## 최댓값 구하기
문제 [링크](https://programmers.co.kr/learn/courses/30/lessons/59415)

```mysql
SELECT MAX(DATETIME) FROM ANIMAL_INS
```
