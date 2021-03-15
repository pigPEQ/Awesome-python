### 1.登录数据库

```sql
# 1.登录mysql
mysql -uroot -p;

# 2.查看当前时间
select now();

# 3.退出数据库
exit; |  quit; | \q  | ctrl d
```



### 2.数据库操作语句

```sql
# 1.显示所有数据库
show databases ;

# 2.创建数据库
create database python2 charset=utf8;

# 3.删除数据库
drop database 【database_name】;

# 3.使用数据库
use 【database_name】;

# 4.查看当前使用的数据库
select database();

# 5.查看创建数据库的sql语句
show create database 【database_name】
```



### 3.表结构操作语句

```sql
# 1.查看所有表
show tables;

# 2.创建表
create table teacher(
  # 字段名称  数据类型  数据约束
  id int unsigned primary key auto_increment not null,
  name varchar(10) not null,
  age tinyint,
  sex enum("男","女") default "女" 
);

# 3.查看表结构
desc 【table_name】

# 4.修改表结构
# 4.1 添加字段
alter table 【table_name】 add 字段名 数据类型 约束;
# 4.2 修改字段类型
alter table 【table_name】 modify 字段名 [数据类型] [约束]
# 4.3 修改字段名称和字段类型
alter table 【table_name】 change 原字段名 修改字段名 数据类型 约束
# 4.4 删除字段
alter table 【table_name】 drop 字段名

# 5.查看创建表的sql语句
show create table 【table_name】
```



### 4.表数据的操作语句

#### 4.1 查询数据

```sql
# 1.查询所有列
select * from 【table_name】

# 2.指定行列查询
select 【row】,【col】 from 【table_name】
```



#### 4.2 添加数据

```sql
# 1.插入数据
insert into 【table_name】[(指定字段)] values(【数据1】)[，(【数据2】)...]
```



#### 4.3 修改数据

```sql
update 【table_name】 set 【修改内容 eg.age=20】 where 【过滤条件】
```



#### 4.4 删除数据

```sql
# 删除不建议物理删除
delete from 【table_name】 where 【过滤条件】
```



### 5.as和distinct

```sql
# 为字段或表起别名
select name [as] '姓名',age [as] '年龄' from 【table_name】
select name,age from 【table_name】 as 【new_table_name】

# 过滤重复的数据
select distinct name,age from 【table_name】
```



