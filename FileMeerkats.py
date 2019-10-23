import asyncio
from Meerkats import *
import os
import math
import time
import sys
from ast import literal_eval
from base64 import b64encode,b64decode
class FileMeerkats(Meerkats):
    redis_type = "file"
    log = BCloudLogger(log_config['FileMeerkats'], log_config['LOG_PATH']).get_logger().Get_Logger()
    endpoint = endpoint_config['FILE'][0]
    port = endpoint_config['FILE'][1]
    #파일을 게이트웨이 서버에 저장했다가 보내야할 경우 사용
    # @classmethod
    # def Carrying(cls, msg):
    #     # print("max: %s"%cls.transport.get_write_buffer_limits())
    #     file = open('./FileStore/%s'%msg,'rb')
    #     cnt = math.ceil(os.path.getsize("./FileStore/%s"%msg)/(1024*10))
    #     message = {
    #         "cnt":1,
    #         "file": msg,
    #         "max_cnt": cnt,
    #         "data":None
    #     }
    #     for x in range(cnt):
    #         l = file.read((1024 * 10))
    #         message['cnt'] = x+1
    #         message["data"] = b64encode(l).decode('utf8')
    #         cls.transport.write(json.dumps(message).encode() + b'\\1\\0')
