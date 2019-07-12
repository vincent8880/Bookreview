from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
   bio = TextAreaField('Tell us about you',validators = [Required()])
   location = TextAreaField('Location',validators = [Required()])
   preferences = TextAreaField('Preferences',validators = [Required()])
   submit = SubmitField('Add Bio')