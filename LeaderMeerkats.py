import asyncio
from ModuleLoader import *
from queue import Queue
import json
from base64 import b64decode
class LeaderMeerkats(asyncio.Protocol):
    tmp=b''
    def __init__(self):
        try:

            self.messageType = {
                "data":"data",
                "control":"control",
                "file":"file"
            }

        except Exception as e:
            print(str(e))

    def connection_made(self, transport):
        peername = transport.get_extra_info('')
        print("Connection made From : {peer}".format(peer=peername))
        self.transport = transport

    def data_received(self, data):

        self.tmp += data
        tmp_dict = self.tmp.split(b'\\0')
        # b'\\0' 패킷 단위 구분자
        # b'\\1' 패킷의 완성본인지 구분 - '}'로 구분해버리면 다중 json 문제가 생길 수 있다

        for x in tmp_dict:
            if not x.endswith(b'\\1'):
                self.tmp = x
            else:
                packet = json.loads(x.replace(b'\\1', b'').decode())

                self.Classification(packet)

        print('Data received: {!r}'.format(data))

    #종류에 따라 작업이 필요한 경우 사용
    def Classification(self,message):
        packet_type =self.messageType[message['type']]
        if  packet_type == 'file':
            self.InsertCave(message)
        elif packet_type == 'control':
            self.InsertCave(message)
        elif packet_type == 'data':
            self.InsertCave(message)
        else:
            log.info('Unknown Message : %s'%message)
    # Relay로 보내면 되서 굳이 저장할 필요성 없으나 만약 저장해야하는 정책이 있다면 사용
    # def ReceiveFile(self,message):
    #     global file_tmp
    #
    #     # 잘라낸 바이너리에 구분자가 있는지
    #     # 잘라낸 바이너리가 한개일때 구분자가 있는가 없는가
    #
    #
    #     if message['max_cnt'] == message['cnt']:
    #
    #         f = open("%s" % message['file'], 'wb')
    #         if message['data'] != b'':
    #             tm = file_tmp + b64decode(message['data'].encode('utf8'))
    #         else:
    #             tm = file_tmp
    #         f.write(tm)
    #         del file_tmp[message['file']]
    #         self.InsertCave()
    #     else:
    #         if message['cnt'] == 1:
    #             file_tmp[message['file']] =b''
    #         file_tmp += b64decode(message['data'].encode('utf8'))
    #

    def InsertCave(self,message):
        MeerkatsStore.lpush(self.messageType[message['type']],json.dumps(message))
