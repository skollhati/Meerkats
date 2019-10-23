import asyncio
from Meerkats import *

class DataMeerkats(Meerkats):
    redis_type = "data"
    log = BCloudLogger(log_config['DataMeerkats'], log_config['LOG_PATH']).get_logger().Get_Logger()
    endpoint = endpoint_config['DATA'][0]
    port = endpoint_config['DATA'][1]