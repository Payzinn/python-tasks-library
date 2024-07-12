from flask import Flask
import csv
from werkzeug.exceptions import InternalServerError
from typing import Optional
app = Flask(__name__)

@app.route("/bank/<branch>/<int:person_id>", methods = ['POST'])
def bank_api(branch, person_id):
    branch_card_file_name = f"bank_data/{branch}.csf"

    with open(branch_card_file_name, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter = ',')

        for record in csv_reader:
            if int(record['id']) == person_id:
                return record['name']
        else:
            return 'Person not found', 404
        
@app.errorhandler(InternalServerError)
def handle_exception(e: InternalServerError):
    original: Optional[Exception] = getattr(e, 'original_exception', None)

    if isinstance(original, FileNotFoundError):
        with open('invalid_eror.log', 'a') as file_error:
            file_error.write(
                f'Tried to access {original.filename}. Exception info {original.strerror}\n'
            )
    elif isinstance(original, OSError):
        with open('invalid_error.log', 'a') as file_error:
            file_error.write(f'Unable to access card. Exception info {original.strerror}\n')
    
    return "Internal server error", 500
if __name__ == '__main__':
    app.run()
