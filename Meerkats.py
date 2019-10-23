from ModuleLoader import *
import asyncio
from _socket import TCP_NODELAY
import socket
class MeerkatsProtocol(asyncio.Protocol):
    def __init__(self, loop):
        # self.message = message
        self.loop = loop

    def connection_made(self, transport):
        self.transport = transport
        # transport.write(json.dumps(self.message).encode())

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        self.loop.stop()





class Meerkats:
    port=8000
    endpoint='127.0.0.1'
    def __init__(self):
        self.redis_interface = RedisInterface()
        self.redis_interface.RegistRedisConnection("MeerkatsCave", 10, "bc1234", 600, Redis_config["endpoint"])
        self.MeerkatsCave = redis_interface.GetRedisConnection("MeerkatsCave")
        self.MeerkatsStore = MeerkatsCave.redis_conn


    @classmethod
    def StartVigilance(cls):

        while(1):
            try:
                cls.loop = cls.AwakeMeerKats()
                cls.loop.run_forever()
            except KeyboardInterrupt:
                cls.loop.close()
                break
            except (RuntimeError,ConnectionError):
                cls.future.cancel()
                continue
            except Exception as e:
                print(str(e))
                break

    @classmethod
    def AwakeMeerKats(cls):
        loop = asyncio.get_event_loop()

        cls.future = asyncio.Future()
        coro = loop.create_connection(lambda: MeerkatsProtocol(loop),
                                      cls.endpoint, cls.port,flags=socket.TCP_NODELAY)

        cls.transport, cls.serv_conn = loop.run_until_complete(coro)
        Meerkat = loop.run_until_complete(cls.Vigilance(cls.future))
        return loop

    @classmethod
    async def Vigilance(cls,Future):
        while (1):
            if MeerkatsStore.llen(cls.redis_type) > 0:
                msg = MeerkatsStore.rpop(cls.redis_type)
                cls.log.info(msg)
                cls.Carrying(msg)
            await asyncio.sleep(0.1)

    @classmethod
    def Carrying(cls,msg):

        cls.transport.write(msg.encode()+b'\\1\\0')




