import flask
import logging

from http_utils import get_ip_address
from subprocess_utils import get_kernel_version

logger = logging.getLogger('app-logger')
logging.basicConfig(level='DEBUG')

app = flask.Flask(__name__)


@app.route('/home')
def get_system_info():
    logger.info('Start')
    ip = get_ip_address()
    kernel = get_kernel_version()
    return "<p>{}</p><p>{}</p>".format(ip, kernel)

if __name__ == '__main__':
    app.run(debug=True)