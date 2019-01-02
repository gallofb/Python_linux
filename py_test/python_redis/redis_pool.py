import redis
#创建连接池
pool = redis.ConnectionPool(host = '127.0.0.1',post = 6379,deode_respomses = True)
#创建链接对象
r = redis.Redis(connection_pool=pool)
#设置集合
r.sadd('set1','v1','v2','v3')
r.sadd('set1','')
