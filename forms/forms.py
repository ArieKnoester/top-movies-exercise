# https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/
# https://wtforms.readthedocs.io/en/3.0.x/
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class EditMovieForm(FlaskForm):
    rating = FloatField(
        label="Your Rating Out of 10 e.g. 7.5",
        validators=[
            NumberRange(
                min=0,
                max=10
            ),
            DataRequired()
        ]
    )
    review = StringField(
        label="Your Review",
        validators=[DataRequired()]
    )
    submit = SubmitField(label="Done")
