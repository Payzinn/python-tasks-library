from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, NumberRange
import re
app = Flask(__name__)



class Registration(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberRange(min = 1000000000, max = 9999999999)])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField()
    comment = StringField()

pattern = r'\w+ \w{1}.\w{1}.'
@app.route('/reg', methods=['POST'])
def reg():
    form = Registration()
    result = re.search(pattern, str(form.name))
    print(str(form.name))
    if form.validate_on_submit():
        email, phone, name = form.email.data, form.phone.data, form.name.data        

        return f"Successfully registered user {email} with phone {phone}"
    return f"Error, invalid input, {form.errors}", 400

if __name__=="__main__":
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug = True)