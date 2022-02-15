### 1.范式

- 第一范式：字段不可拆分。
- 第二范式：存在唯一主键，非主键完全依赖主键，不存在部分依赖。
- 第三范式：不能存在传递依赖。



### 2.外键约束

```sql
# 添加外键约束
alter table 【table_name1 add foreign key(c_id) reference 【table_name2】(id)

# 创建表时添加外键约束
create table 【table_name1】(
  ...
  c_id tinyint not null,
  foreign key(c_id) reference 【table_name2】(id)
)

# 删除外键
alter table 【table_name1】 drop 【外键名】
```



### 3.将查询结果插入表中

```sql
#  1.创建表后插入查询数据
insert into 【table_name1】([字段名]) select * from ...

#  2.创建表时插入查询数据 查询的字段名要和创建的字段名一致
create table 【table_name1】(
	...
  name varchar(50) not null select u_name as name from 【table_name2】
)
```



### 4.pymql

```python
# pymysql支持事务
import pymysql

if __name__  == '__main__':
  # 创建连接对象
  conn = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='mysql',
                         database='python',
                         charset='utf8')
  # 获取游标
  cursor  =  conn.cursor()

  # 1.查询的sql
  sql1 = 'select * from table1;'
  cursor.excute(sql1)
  # 从游标中获取执行结果
  output = cursor.fetchall()
  for i in output:
    print(output)
  # 关闭游标，连接
  cursor.close()
  conn.close()

  # 2.修改、增加、删除的sql
  sql2 = 'update table1 set age=10 where name="zhangsan";'
  try:
    cursor.excute(sql2)
    conn.commit()
  except Exception as e:
    conn.rollback()
  finally:
    cursor.close()
    conn.close()
```



### 5.防止SQL注入

```python
# sql注入：用户输入的恶意的信息与sql语句拼接导致数据泄露
# sql语句参数化来防止sql注入,其中%s是占位符,如果有多个参数时，增加多个%s占位符
params = []
cursor.excute('select * from table1 where name = %s',params)
```



### 6.事务

##### 存储引擎：

1. InnoDB：支持事务
2. MyISAM：查询插入速度最快

##### 事务的特性：

- 原子性：事务不可再被分割为更小的工作单元，要么全部执行成功，要么全部失败回滚。

- 一致性：数据从一个一致性的状态转变到另一个一致性的状态。

- 隔离性：一个事务所做的修改操作在提交之前，对于其他事务来说是不可见的。

- 持久性：一旦提交事务，所做修改将会永远保存到数据库中。

##### 事务演练的sql语句：

```sql
# mysql数据库默认采用自动提交(autocommit)模式，临时设定取消 set autocommit = 0
begin;
insert into table1(name) values('zhangsan'),('lisi');
select * from table1;
commit;
```



### 7.索引

```sql
# 优点：加速数据查询速度 缺点：创建索引耗费时间和占用空间

# 添加索引
alter table table1 add index [index_name](name)

# 开启时间检测
set profiling = 1
# 查看sql执行时间
show profiles

# 添加联合索引,覆盖多个字段
# 联合索引的最左原则，使用联合索引时查询条件必须包含最左边的字段时索引才会生效
alter table table1 add index(name,age)
```

