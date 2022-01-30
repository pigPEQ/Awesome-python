### 关键字
![redis](/Note/redis/res/redis.png)



### 与python交互

```python
import redis

# 可以不传参数，即默认本地
client = redis.Redis(host='localhost',port=6379，database=0)
# 数据操作
client.set('name','zhangsan')
...
```



### redis优化

- 主从模式
- 服务器集群（cluster）多个节点，一主一从

