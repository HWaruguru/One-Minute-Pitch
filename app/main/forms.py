from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.fields.core import SelectField
from wtforms.validators import Required

class CommentForm(FlaskForm):
    comment = TextAreaField('comment',validators=[Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    category_choices = ['Product', 'Pickup', 'Interview']
    title = StringField('Title',validators=[Required()])
    category = SelectField('Category', choices = category_choices, validators = [Required()])
    pitch = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')






