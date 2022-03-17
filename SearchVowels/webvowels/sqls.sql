select distinct ip from log;
select letters, count(letters) as 'count', letters 
from log
group by letters
order by count desc
limit 1;
select browser_string, count(browser_string) as 'count',   
browser_string from log
group by browser_string
order by count desc
limit 1;