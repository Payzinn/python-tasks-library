from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
import re
app = Flask(__name__)



class Registration(FlaskForm):
    email = StringField()
    phone = IntegerField()
    name = StringField()
    address = StringField()
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
        if email == None and phone == None:
            return 'None phone and email',400
        elif email == None:
            return 'None email',400
        elif phone == None:
            return 'None phone',400
        elif len(str(phone)) != 10:
            return 'Phone length has to be 10 symbols',400
        elif not result:
            return "Name has to be in format Ivan I.I.",400
        

        return f"Successfully registered user {email} with phone {phone}"
    return f"Error, invalid input, {form.errors}", 400

if __name__=="__main__":
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug = True)