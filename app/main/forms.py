from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Book review', validators=[Required()])
    submit = SubmitField('Submit')


class OrderForm(FlaskForm):
    Name = StringField('Enter your full name',validators = [Required()])
    Mobile = StringField('Enter your mobile number',validators = [Required()])
    Amount = StringField('Enter amount:(ksh)',validators = [Required()])
    submit = SubmitField('Order')