import asyncio
from LeaderMeerkats import *
from multiprocessing import Process
from DataMeerkats import DataMeerkats
from ControlMeerkats import ControlMeerkats
from FileMeerkats import FileMeerkats

def ProcessSetting(proUnit,Meerkats):
    # config_json["PROCESS"]["DATA"]
    tmp_list = list()
    for x in range(proUnit):
        tmp_process = Process(target=Meerkats.StartVigilance)
        tmp_process.start()
        tmp_list.append(tmp_process)

    return tmp_list
def ProcessJoin(Meerkats_list):
    for x in Meerkats_list:
        x.join()


if __name__ == '__main__':
    dataMeerkat = ProcessSetting(config_json["PROCESS"]["DATA"],DataMeerkats)
    controlMeerkat = ProcessSetting(config_json["PROCESS"]["CONTROL"],ControlMeerkats)
    fileMeerkat = ProcessSetting(config_json["PROCESS"]["FILE"],FileMeerkats)

    loop = asyncio.get_event_loop()
    coro = loop.create_server(LeaderMeerkats,'0.0.0.0',9000)
    server = loop.run_until_complete(coro)

    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print("server closed")

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

    ProcessJoin(dataMeerkat)
    ProcessJoin(controlMeerkat)
    ProcessJoin(fileMeerkat)

