create table company_users 
(
company_id int,
user_id int,
language varchar(20)
);

insert into company_users values (1,1,'English')
,(1,1,'German')
,(1,2,'English')
,(1,3,'German')
,(1,3,'English')
,(1,4,'English')
,(2,5,'English')
,(2,5,'German')
,(2,5,'Spanish')
,(2,6,'German')
,(2,6,'Spanish')
,(2,7,'English');


# filter comnpanies that having atleast 2 users speakig german and english subquery method

select company_id from (select company_id,user_id from company_users
where language in ("German","English")
group by company_id,user_id
having count(language) = 2) a
group by company_id
having count(User_id) >= 2;
