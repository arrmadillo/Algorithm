-- 코드를 입력하세요
SELECT 
    COUNT(USER_ID)
FROM
    USER_INFO
WHERE
    (AGE >= 20 AND AGE <= 29) # 20세이상 29세 이하이면서
    AND
    YEAR(JOINED) = 2021; # 2021년에 가입한 사람
    # JOINED LIKE '2021%'; 요렇게도 연도 필터링 가능