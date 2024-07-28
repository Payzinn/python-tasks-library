import logging
import time
import requests

http = logging.getLogger('htttp_utils.logger_utils')
http.setLevel('INFO')
GET_IP_URL = 'https://api.ipify.org/?format=json'

def get_ip_address() -> str:
    http.info('Start calling http_utils')
    start =time.time()
    try:
        ip = requests.get(GET_IP_URL).json()['ip']
    except Exception as e:
        http.exception(e)
        raise e
    http.debug('Done requesting ip in {:.4f} seconds'.format(time.time() - start))
    http.info('IP address is: {}'.format(ip))
    return ip
