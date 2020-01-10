from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Enter the puppy name: ')
    submit = SubmitField('Submit name')

class DelForm(FlaskForm):

    id = IntegerField('Enter the puppy ID to be deleted')
    submit = SubmitField('Submit the id to be deleted')

class AddOwnerForm(FlaskForm):

    name = StringField('Owner name: ')
    pup_id = IntegerField('Puppy ID: ')
    submit = SubmitField('Add new Owner')