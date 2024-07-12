from flask import Flask
import csv
from werkzeug.exceptions import InternalServerError
from typing import Optional
import logging

app = Flask(__name__)
logger = logging.getLogger("bank_api")

@app.route("/bank/<branch>/<int:person_id>", methods = ['POST'])
def bank_api(branch, person_id):
    logger.debug(f'Запрос {person_id} из {branch}')
    branch_card_file_name = f"bank_data/{branch}.csv"

    with open(branch_card_file_name, 'r') as file:
        logger.debug(f"Успешно открыт {branch} файл")
        csv_reader = csv.DictReader(file, delimiter = ',')

        for record in csv_reader:
            if int(record['id']) == person_id:
                logger.debug(f"Успешно найден файл для {person_id}")
                return record['name']
        else:
            logger.debug(f'Человек {person_id} не был найден в {branch}')
            return 'Person not found', 404
        
        
@app.errorhandler(InternalServerError)
def handle_exception(e: InternalServerError):
    original: Optional[Exception] = getattr(e, 'original_exception', None)

    if isinstance(original, FileNotFoundError):
        logger.error(f'Ошибка: Файл {original.filename} не найден.{original.strerror}')
    elif isinstance(original, OSError):
        logger.error(f'Ошибка: Файл csv не найден.{original.strerror}')

    return "Internal server error", 500

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, 
                        filename='banking.log', 
                        format = '%(asctime)s - %(name)s %(levelname)s - %(message)s',)
    logger.info(f'Запущен сервер bank-api')
    app.run(debug = True)
