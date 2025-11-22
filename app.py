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

@app.route('/students')
def students():
    all_students = Student.query.all()

    html = """
    <h2>Saved Students</h2>
    <table border="1" cellpadding="8" cellspacing="0">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Department</th>
            <th>Roll No</th>
            <th>College</th>
        </tr>
    """

    for s in all_students:
        html += f"""
        <tr>
            <td>{s.id}</td>
            <td>{s.name}</td>
            <td>{s.dept}</td>
            <td>{s.rollno}</td>
            <td>{s.college}</td>
        </tr>
        """

    html += "</table>"
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)