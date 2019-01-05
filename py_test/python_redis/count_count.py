#基于redis实现一个计数器
import redis
conn = redis.Redis(host='127.0.0.1',port=6179)
conn.set('count',1000)

with conn.pipeline('count') as pipe:   #
    while 1:
        try:
           #先监视，自己的值没有被修改过
            conn.watch('count')
           #事物开始
        except:
            pass



