import redis
pool = redis.ConnectionPool(host = '127.0.0.1',port = 6379)
r = redis.Redis(connection_pool=pool)

pipe = r.pipeline(transaction=True)  #将多个操作组合成原子性操作，一个失败将意味着全部失败

pipe.multi()  #事物开始
# pipe.set('name','apple')
# pipe.set('age','2')

pipe.execute() #执行原子性操作  事物正真的向redis_server提交

print(r.get('name'))
print(r.get('age'))