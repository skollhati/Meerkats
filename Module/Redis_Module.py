
import redis
import Module.BModule_Singleton as Singleton
from Module.LogModule_Singleton import BCloudLogger
import json
import pickle

class ConnectionObject():
    def __init__(self,db,password,timeout=3600,host='127.0.0.1',port=6379):
        self.redis_conn = redis.StrictRedis(host=host, port=port, db=db, password=password,charset="utf-8",decode_responses=True)
        # self.redis_conn=redis.Redis(connection_pool=self.redis_pool)

        if timeout >0:
            self.timeout = timeout
        else:
            self.timeout=None

        # pubsub = self.redis_conn.pubsub()
        # pubsub.psubscribe('__keyevent@0__:expired')
        #
        # for msg in pubsub.listen():
        #     print(msg)


    def GetData(self, key):
        try:
            #redis_data=pickle.loads(self.redis_conn.get(key))
            data=self.redis_conn.get(str(key))

        #redis_data=self.redis_conn.hgetall(key)

            if data is not None:
                #return RedisSessionObject(key,redis_data)
                return json.loads(data)

            else:
                return False
        except Exception as e:

            return False
    def GetAllKeys(self):
        try:
            return self.redis_conn.keys(pattern='*')
        except Exception as e:
            return False
    def SetData(self, key, value):
        #self.redis_conn.setex(key,self.timeout,pickle.dumps(value))
        if key is not None:
            if self.timeout is not None:
                self.redis_conn.setex(key, self.timeout, value)
            else :
                self.redis_conn.set(key,value)


    def RemoveData(self, key):
        self.redis_conn.delete(key)

class RedisInterface():
    def __init__(self):
        self.redis_conn_pool=dict()

    def RegistRedisConnection(self,conn_key,db,password,timeout=3600,host='127.0.0.1',port=6379):
        self.redis_conn_pool[conn_key] = ConnectionObject(db,password,timeout,host,port)

    def GetRedisConnection(self,conn_key):
        return self.redis_conn_pool[conn_key]


# class RedisSessionObject():
#     def __init__(self,session_key,session_redis):
#         self.key = session_key
#         self.redis_conn=session_redis
#
#
#     def __del__(self):
#
#         del (self.key)




