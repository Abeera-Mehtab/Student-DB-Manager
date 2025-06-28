from flask import Flask, render_template, request, redirect, session, url_for
from flask.cli import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import redirect
from forms import StudentForm
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'firstapp.db')
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=True,  # Enable in production (requires HTTPS)
    SESSION_COOKIE_SAMESITE='Lax',
    PERMANENT_SESSION_LIFETIME=900  # 15 minutes session timeout
)
db = SQLAlchemy(app)
csrf = CSRFProtect(app)


class Admin(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 username = db.Column(db.String(50), unique=True)
 password = db.Column(db.String(100))

class Students(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    # First Section
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    age = db.Column(db.Integer)
    city = db.Column(db.String(50))
    # Second Section
    roll_no = db.Column(db.Integer)
    batch = db.Column(db.String(20))
    degree = db.Column(db.String(50))
    faculty = db.Column(db.String(50))
    # Third Section
    email_uni = db.Column(db.String(100))
    email_personal = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    address = db.Column(db.String(150))
    # NEW FIELD - Fourth Section
    zip_code = db.Column(db.Integer, nullable=False)  # Added as separate section


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'admin' not in session:
        return redirect('/login')
    form = StudentForm()
    if form.validate_on_submit():
        new_student = Students(
            # First Section
            fname=form.fname.data,
            lname=form.lname.data,
            age=form.age.data,
            city=form.city.data,
            # Second Section
            roll_no=form.roll_no.data,
            batch=form.batch.data,
            degree=form.degree.data,
            faculty=form.faculty.data,
            # Third Section
            email_uni=form.email_uni.data,
            email_personal=form.email_personal.data,
            phone=form.phone.data,
            address=form.address.data,
            #fourth Section
            zip_code=form.zip_code.data
        )
        db.session.add(new_student)
        db.session.commit()
        return redirect('/')
    data = Students.query.all()
    return render_template('index.html', data=data, form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if Admin.query.first():
        return redirect('/login')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Hash the password before storing
        password_hash = generate_password_hash(password)
        # Create new admin with hashed password
        new_admin = Admin(username=username, password=password_hash)
        db.session.add(new_admin)
        db.session.commit()
        session['admin'] = username
        return redirect('/')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if not Admin.query.first():
        return redirect('/register')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Find admin by username only
        admin = Admin.query.filter_by(username=username).first()
        # Verify password against stored hash
        if admin and check_password_hash(admin.password, password):
            session['admin'] = username
            return redirect('/')
        else:
            return "Invalid credentials. Try again."
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('admin', None)
    return redirect('/login')

@app.route('/home')
def home():
    if 'admin' not in session:
        return redirect('/login')
    data = Students.query.all()
    return render_template('database_view.html', data=data)

@app.route('/delete/<int:sno>')
def delete(sno):
    student = Students.query.get_or_404(sno)
    db.session.delete(student)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    student = Students.query.get_or_404(sno)
    form = StudentForm(obj=student)  # Pre-populate form with student data
    if form.validate_on_submit():
        form.populate_obj(student)  # Update student object with form data
        db.session.commit()
        return redirect('/home')
    return render_template('update.html', form=form, student=student)

if __name__ == '__main__':
    with app.app_context():
        #db.drop_all()
        db.create_all()
    app.run(debug=True)