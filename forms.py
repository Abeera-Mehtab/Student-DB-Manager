from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.fields import EmailField  # This line is required for EmailField
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, Email

class StudentForm(FlaskForm):
    # First Row - Basic Info
    fname = StringField('First Name', validators=[
        DataRequired(),
        Length(max=20),
        Regexp(r'^[A-Za-z]+$', message="Only letters allowed")
    ])
    lname = StringField('Last Name', validators=[
        DataRequired(),
        Length(max=20),
        Regexp(r'^[A-Za-z]+$', message="Only letters allowed")
    ])
    age = IntegerField('Age', validators=[
        DataRequired(),
        NumberRange(min=1, max=90, message="Enter a valid age (1-90)")
    ])
    city = StringField('City', validators=[
        DataRequired(),
        Length(max=20),
        Regexp(r'^[A-Za-z\s]+$', message="Only letters and spaces allowed")
    ])

    # Second Row - Academic Info
    roll_no = IntegerField('Roll No', validators=[
        DataRequired(),
        NumberRange(min=1, max=999999, message="Roll number must be 1-6 digits")
    ])
    batch = StringField('Batch', validators=[
        DataRequired(),
        Length(max=20),
        Regexp(r'^[A-Za-z0-9\-/]+$', message="Alphanumeric with -/ allowed")
    ])
    degree = StringField('Degree', validators=[
        DataRequired(),
        Length(max=50),
        Regexp(r'^[A-Za-z\s\-\.]+$', message="Letters, spaces, hyphens and dots allowed")
    ])
    faculty = StringField('Faculty', validators=[
        DataRequired(),
        Length(max=50),
        Regexp(r'^[A-Za-z\s]+$', message="Only letters and spaces allowed")
    ])

    # Third Row - Contact Info
    email_uni = EmailField('University Email', validators=[
        DataRequired(),
        Email(),
        Length(max=100)
    ])
    email_personal = EmailField('Personal Email', validators=[
        DataRequired(),
        Email(),
        Length(max=100)
    ])
    phone = StringField('Phone', validators=[
        DataRequired(),
        Regexp(r'^\+92-3\d{2}-\d{7}$', message="Format: +92-3xx-xxxxxxx")
    ])
    address = StringField('Home Address', validators=[
        DataRequired(),
        Length(max=150, message="Maximum 150 characters allowed")
    ])
    # New change
    # Fourth Section - Location Info
    zip_code = IntegerField('Zip Code', validators=[
        DataRequired(),
        NumberRange(min=0, message="Zip code cannot be negative")
    ])
