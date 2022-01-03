select B.book_id, B.name 
from Books B
left join Orders O
on B.book_id = O.book_id and dispatch_date  >= date_sub('2019-06-23', interval 1 year)
where  B.available_from < date_sub('2019-06-23', interval 1 month)
group by B.book_id 
having ifnull(sum(O.quantity),0) < 10