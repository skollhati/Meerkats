import asyncio
import math
import time
import os
import json

async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888,
                                                   loop=loop)

    file = open('./FileStore/Kings.mp4' , 'rb')
    cnt = math.ceil(os.path.getsize('./FileStore/Kings.mp4') / 100)
    l = file.read(100)

    message = {
        "cnt": 1,
        "file": "Kings.mp4",
        "max_cnt": cnt,
        # "data":b64encode(l).decode('utf8')
    }
    # print(len(message['data']))
    print(len(l))

    writer.write(json.dumps(message).encode())

    while (message["cnt"] < cnt):
        l = file.read(100)
        message["cnt"] += 1
        # message["data"]=b64encode(l).decode('utf8')
        # print(len(message['data']))
        print(len(l))
        writer.write("1".encode())



    # print('Send: %r' % message)
    # writer.write(message.encode())
    #
    # data = await reader.read(100)
    # print('Received: %r' % data.decode())
    #
    # print('Close the socket')
    # writer.close()


message = 'Hello World!'
loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()