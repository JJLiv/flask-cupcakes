from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, validators, FloatField

class AddCupcakeForm(FlaskForm):
    flavor = StringField("Flavor")
    size = StringField("Size")
    rating = FloatField("Rating")
    image = StringField("Image")