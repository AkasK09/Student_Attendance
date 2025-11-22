from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    dept = db.Column(db.String(50))
    rollno = db.Column(db.String(50))
    college = db.Column(db.String(150))

# Create DB
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/save', methods=['POST'])
def save():
    student = Student(
        name=request.form['name'],
        dept=request.form['dept'],
        rollno=request.form['rollno'],
        college=request.form['college']
    )

    db.session.add(student)
    db.session.commit()

    return "Data saved! <br><a href='/'>Go back</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)