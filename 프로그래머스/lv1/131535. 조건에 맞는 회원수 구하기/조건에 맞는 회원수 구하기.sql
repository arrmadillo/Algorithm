-- 코드를 입력하세요
SELECT 
    COUNT(*)
FROM
    USER_INFO
WHERE
    JOINED LIKE '2021%'
    AND
    AGE > 19 AND AGE < 30;