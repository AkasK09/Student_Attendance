from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    dept = db.Column(db.String(50))
    rollno = db.Column(db.String(50))
    college = db.Column(db.String(150))


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    # Home = Add Student page
    return render_template('form.html')


@app.route('/students')
def students():
    all_students = Student.query.order_by(Student.id.desc()).all()
    total = Student.query.count()
    return render_template('students.html', students=all_students, total=total)


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
    return redirect(url_for('students'))


@app.route('/delete/<int:id>')
def delete(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('students'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
