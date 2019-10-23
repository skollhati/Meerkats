from Module.Redis_Module import *
import platform
import optparse


config={
    "local":'./Config/Meerkats_config_local.json',
    "service":'/bcloud_web/config/xcerfitCPS_server_config_service.json',
    "test":'/bcloud_web/config/xcerfitCPS_server_config_test.json'
}

if platform.system() =='Windows':
    json_data = open(config['local']).read()
else :
    json_data = open(config['local']).read()
    # parser = optparse.OptionParser()
    # parser.add_option("-m", "--mode", dest="mode", type="string", help="Sever Mode [test | service]")
    # (options, args) = parser.parse_args()
    # json_data = open(config[options.mode]).read()



config_json = json.loads(json_data)
log_config = config_json["LOG"]
endpoint_config = config_json["ENDPOINT"]

server_port = config_json["PORT"]
log = BCloudLogger(log_config["INFO"],log_config['LOG_PATH']).get_logger().Get_Logger()


Redis_config = config_json["REDIS"]


redis_interface = RedisInterface()
redis_interface.RegistRedisConnection("MeerkatsCave",10,"bc1234",600,Redis_config["endpoint"])
MeerkatsCave = redis_interface.GetRedisConnection("MeerkatsCave")
MeerkatsStore = MeerkatsCave.redis_conn






