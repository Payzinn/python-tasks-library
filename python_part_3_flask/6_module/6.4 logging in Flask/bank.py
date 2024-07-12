from flask import Flask
import csv
from werkzeug.exceptions import InternalServerError
from typing import Optional
import logging

app = Flask(__name__)
logger = logging.getLogger('bank-api')

@app.route("/bank/<branch>/<int:person_id>", methods = ['POST', 'GET'])
def bank_api(branch, person_id):
    branch_card_file_name = f"bank_data/{branch}.csf"

    with open(branch_card_file_name, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter = ',')

        for record in csv_reader:
            if int(record['id']) == person_id:
                return record['name']
        else:
            logger.warning('Человек не найден')
            return 'Person not found', 404
        
@app.errorhandler(InternalServerError)
def handle_exception(e: InternalServerError):
    original: Optional[Exception] = getattr(e, 'original_exception', None)

    if isinstance(original, FileNotFoundError):
        logger.exception('Ошибка: Файл не найден ', original.strerror)
    elif isinstance(original, OSError):
        logger.exception('Ошибка: Система ', original.strerror)

    logger.error(f'Ошибка: {e}')
    return "Internal server error", 500

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.info('Запущен сервер bank-api')
    app.run()
