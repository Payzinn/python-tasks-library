from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, NumberRange
import logging
app = Flask(__name__)
logger = logging.getLogger('divider')
class DivideForm(FlaskForm):
    a = IntegerField(validators=[InputRequired()])
    b = IntegerField(validators=[InputRequired()])

@app.route("/divide/", methods = ['POST'])
def divide():
    form = DivideForm()

    if form.validate_on_submit():
        a, b = form.a.data, form.b.data
        logger.debug(f"Форма валидна. a={a}, b={b}")
        return f"a / b = {a/b:.2f}"
    logger.error(f'Форма не валидна, error={form.errors}')
    return f'Error:{form.errors}', 400

@app.errorhandler(ZeroDivisionError)
def handle_exception(e: ZeroDivisionError):
    logger.exception("Ошибка деление на ноль: ", exc_info=e)
    return 'На 0 делить нельзя\n', 400

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.info('Started divider server!')
    app.config['WTF_CSRF_ENABLED'] = False 
    app.run()