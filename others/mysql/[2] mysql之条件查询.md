### 1.where的使用

- 比较运算【> < = !=...】

- 逻辑运算【and 、or、 not】
- 范围查询【between...and...、in(a,b,c)】
- 模糊查询【like】，其中%为任意多个字符，_为任意一个字符。
- 空判断查询【null】



### 2.排序查询

```sql
# esc为升序，默认；desc为降序
select * from 【table_name】 order by 【字段】 desc
```



### 3.分页查询

```sql
select * from 【table_name】 limit 【索引,(n-1)*m,n为分页】,【查询条数m】
```



### 4.聚合函数

```sql
# sum()、conut(*)、max、min、avg...[聚合函数不对空值进行统计]
select sum(age) from 【table_name】
select avg(ifnull(age,0)) from 【table_name】
```



### 5.分组查询

```sql
# 10.1   根据字段名A分组对字段名B的信息集合进行统计
select 【字段名A】,group_concat(【字段名B】) from 【table_name】group by 【字段名A】
eg.  select age,group_concat(name) from teacher group by age

# 10.2  按照年龄进行分组，并统计每个年龄的人数
select age,count(*) from teacher group by age

# 10.3 with rollup汇总总人数
select age,count(*) from teacher group by age with rollup

# 10.4 having对分组数据进行过滤
select age,count(*) from teacher group by age having count(*)>n
```



### 6.多表连接查询

```sql
# 6.1 内连接查询  inner join 
select * from 【table_name1】t1 inner join 【table_name2】 t2 on 【t1.attr】=【t2.attr】

# 6.2 左连接查询  left join 左表为主,查询不到填null
select * from 【table_name1】 t1 left join 【table_name12】t2 on 【t1.attr】=【t2.attr】

# 6.3 右连接查询 right join 右表为主
select * from 【table_name1】 t1 right join 【table_name12】t2 on 【t1.attr】=【t2.attr】

# 6.4 自连接查询 一张表模拟两张表
select * from 【table_name1】t1 inner join 【table_name1】t2 on 【t1.attr】=【t2.attr】
```



