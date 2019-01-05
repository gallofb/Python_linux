import redis
r = redis.Redis(host='127.0.0.1',port=6379,decode_responses=True)
#存储键值对
# r.set('name','gallo')
# r.set('age','16')
#获取值
# print(r.get('name'))
# print(r.get('age'))


# r.lpush('list','gallo','school','xiyou')
# print(r.lrange('list',0,-1))
# print(r.llen('list'))
r.delete('name')

#获取数据库中所有的建  返回的是一个列表
print(r.keys())
