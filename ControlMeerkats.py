import asyncio
from Meerkats import *

class ControlMeerkats(Meerkats):
    redis_type = "control"
    log = BCloudLogger(log_config['ControlMeerkats'], log_config['LOG_PATH']).get_logger().Get_Logger()
    endpoint = endpoint_config['CONTROL'][0]
    port = endpoint_config['CONTROL'][1]

