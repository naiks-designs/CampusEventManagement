from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campus_event.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ----------------- Models -----------------
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    type = db.Column(db.String(30))
    date = db.Column(db.String(20))

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    event_id = db.Column(db.Integer)
    status = db.Column(db.String(10))  # Present/Absent

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    event_id = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String(100))

# ----------------- Endpoints -----------------
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    student = Student(name=data['name'], email=data['email'])
    db.session.add(student)
    db.session.commit()
    return jsonify({"message": f"Student {data['name']} added!"})

@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    event = Event(name=data['name'], type=data['type'], date=data['date'])
    db.session.add(event)
    db.session.commit()
    return jsonify({"message": f"Event {data['name']} created!"})

@app.route('/register', methods=['POST'])
def register_student():
    data = request.get_json()
    reg = Registration(student_id=data['student_id'], event_id=data['event_id'])
    db.session.add(reg)
    db.session.commit()
    return jsonify({"message": "Student registered successfully!"})

@app.route('/attendance', methods=['POST'])
def mark_attendance():
    data = request.get_json()
    att = Attendance(student_id=data['student_id'], event_id=data['event_id'], status=data['status'])
    db.session.add(att)
    db.session.commit()
    return jsonify({"message": "Attendance marked!"})

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    fb = Feedback(student_id=data['student_id'], event_id=data['event_id'], rating=data['rating'], comment=data['comment'])
    db.session.add(fb)
    db.session.commit()
    return jsonify({"message": "Feedback submitted!"})

# ----------------- Reports -----------------
@app.route('/reports/registrations/<int:event_id>', methods=['GET'])
def registrations_report(event_id):
    total = Registration.query.filter_by(event_id=event_id).count()
    return jsonify({"event_id": event_id, "total_registrations": total})

@app.route('/reports/attendance/<int:event_id>', methods=['GET'])
def attendance_report(event_id):
    regs = Registration.query.filter_by(event_id=event_id).count()
    present = Attendance.query.filter_by(event_id=event_id, status="Present").count()
    percent = (present/regs*100) if regs > 0 else 0
    return jsonify({"event_id": event_id, "attendance_percent": percent})

@app.route('/reports/feedback/<int:event_id>', methods=['GET'])
def feedback_report(event_id):
    feedbacks = Feedback.query.filter_by(event_id=event_id).all()
    avg = sum(f.rating for f in feedbacks)/len(feedbacks) if feedbacks else 0
    return jsonify({"event_id": event_id, "average_feedback": avg})

# ----------------- Run -----------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    print("Database ready. Starting server...")
    app.run(debug=True)
