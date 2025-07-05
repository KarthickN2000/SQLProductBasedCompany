CREATE TABLE [students](
 [studentid] [int] NULL,
 [studentname] [nvarchar](255) NULL,
 [subject] [nvarchar](255) NULL,
 [marks] [int] NULL,
 [testid] [int] NULL,
 [testdate] [date] NULL
)
data:
insert into students values (2,'Max Ruin','Subject1',63,1,'2022-01-02');
insert into students values (3,'Arnold','Subject1',95,1,'2022-01-02');
insert into students values (4,'Krish Star','Subject1',61,1,'2022-01-02');
insert into students values (5,'John Mike','Subject1',91,1,'2022-01-02');
insert into students values (4,'Krish Star','Subject2',71,1,'2022-01-02');
insert into students values (3,'Arnold','Subject2',32,1,'2022-01-02');
insert into students values (5,'John Mike','Subject2',61,2,'2022-11-02');
insert into students values (1,'John Deo','Subject2',60,1,'2022-01-02');
insert into students values (2,'Max Ruin','Subject2',84,1,'2022-01-02');
insert into students values (2,'Max Ruin','Subject3',29,3,'2022-01-03');
insert into students values (5,'John Mike','Subject3',98,2,'2022-11-02');



#MYSQL query

-- write an sql query to get the percentage of students who scored more than 90 in any subject amongnst all the students

select count(distinct case when marks > 90 then studentid else null end) / count(distinct studentid) * 100  as percentage
from students

select * from students;

with ranked_cte as(select subject,marks,
		rank() over(partition by subject order by marks asc) rank_asc,
		rank() over(partition by subject order by marks desc) rank_desc
from students)

select subject,max(case when rank_asc = 2 then marks else null end) as second_lowest_mark,
max(case when rank_desc = 2 then marks else null end) as second_highest_mark
from ranked_cte
group by subject

