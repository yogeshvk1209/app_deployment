#!/usr/bin/env python

from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import sys
import optparse
import time
import os


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
# Add secrete for session management (Required for Debug)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required(), validators.Length(min=4, max=12)])
    action = TextField('action:', validators=[validators.required(), validators.Length(min=5, max=40)])

@app.route("/", methods=['GET', 'POST'])
def webapp():
    form = ReusableForm(request.form)

    print (form.errors)
    if request.method == 'POST':
        name=request.form['name']
        action=request.form['action']
        print (action, " ", name)
        # Exclude delete action form form validation
        if (action != "Do not display typed username"):
            if form.validate():
                # Display comment for post action.
                flash(name)
                flash('Action "'+ action +'" performed on User '+ name)
            else:
                flash('Error: Username field of form is required for action -> '+ action)
        else:
            flash('Username not displayed as selected action -> '+ action)
    return render_template('webapp.html', form=form)

# Def a function for user create

if __name__ == "__main__":
    parser = optparse.OptionParser(usage="python pytask.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        print ("Missing required argument: -p/--port")
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=True)
