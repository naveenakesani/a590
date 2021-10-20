WITH 
  r1 AS (select country, 
                dense_rank() over (order by count(c.comment_id) desc) AS 2020_rank
          from users u left join comments c 
            on extract(year from c.posted_at)=2020 and c.user_id=u.user_id
          group by country),
  r2 AS (select country, 
                dense_rank() over (order by count(c.comment_id) desc) AS 2021_rank
          from users u left join comments c 
            on extract(year from c.posted_at)=2021 and c.user_id=u.user_id
          group by country)     
SELECT  r1.country, 2020_rank, 2021_rank,
        (2020_rank - 2021_rank) AS rise
FROM    r1 JOIN r2 ON r1.country = r2.country
WHERE   2021_rank < 2020_rank
;  
