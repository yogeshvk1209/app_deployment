#!/usr/bin/env python3

from flask import Flask, render_template, flash, request
from wtforms import Form, StringField, TextAreaField, validators, SubmitField
import sys
import argparse
import time
import os

# App config
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
# Secret key for session management (use environment variable in production)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', '7d441f27d441f27567d441f2b6176a')

class ReusableForm(Form):
    name = StringField('Name:', validators=[validators.DataRequired(), validators.Length(min=4, max=12)])
    action = StringField('Action:', validators=[validators.DataRequired(), validators.Length(min=5, max=40)])

@app.route("/", methods=['GET', 'POST'])
def webapp():
    form = ReusableForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        name = request.form['name']
        action = request.form['action']
        print(action, " ", name)
        # Exclude delete action from form validation
        if action != "Do not display typed username":
            if form.validate():
                # Display comment for post action
                flash(name)
                flash(f'Action "{action}" performed on User {name}')
            else:
                flash(f'Error: Username field of form is required for action -> {action}')
        else:
            flash(f'Username not displayed as selected action -> {action}')
    return render_template('webapp.html', form=form)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Flask webapp")
    parser.add_argument('-p', '--port', type=int, required=True, help='The port to listen on')
    args = parser.parse_args()

    try:
        app.run(host='0.0.0.0', port=args.port, debug=True)
    except ValueError as e:
        print(f"Error: Invalid port number - {e}")
        sys.exit(1)
