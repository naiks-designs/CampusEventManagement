Campus Event Management Platform

Project Overview

For my assignment I built a campus event management platform to help colleges manage events efficiently.

1.Admin Portal (Web): Allows staff to create events like hackathons, workshops, tech talks, and fests.

2.Student App / API: Lets students browse events, register, mark attendance, and give feedback.
I focused on keeping the prototype simple and functional And adding core features like registration ,attendance, tracking feedback collection and generating reports.

Step instructions are: 
1.Make sure Python latest version is installed. 
2.Open command prompt in the project folder you created.
3.Install the required packages for the prototype.
-- pip install flask flask_sqlalchemy requests
4.Start the flash server
-- python app.py

5.You should see:
 Running on http://127.0.0.1:5000

6.Keep this command window open and open new command window , where run this command below:
   python test_api.py

This will process adding students, creating events, registering, marking attendance, and submitting feedback.

Features / Endpoints

Student Management
POST /students → Add a student
Example JSON: {"name":"Alice", "email":"alice@example.com"}

Event Management
POST /events → Create an event
Example JSON: {"name":"Tech Workshop", "type":"Workshop", "date":"2025-09-10"}

Registration
POST /register → Register a student for an event
Example JSON: {"student_id":1, "event_id":1}

Attendance
POST /attendance → Mark attendance
Example JSON: {"student_id":1, "event_id":1, "status":"Present"}

Feedback
POST /feedback → Submit feedback
Example JSON: {"student_id":1, "event_id":1, "rating":5, "comment":"Great event!"}

Reports
GET /reports/registrations/<event_id> → Total registrations per event

GET /reports/attendance/<event_id> → Attendance percentage

GET /reports/feedback/<event_id> → Average feedback score

Reports / Outputs
When I ran the test script, I got results like:

{'message': 'Student Alice added!'}
{'message': 'Event Tech Workshop created!'}
{'message': 'Student registered successfully!'}
{'message': 'Attendance marked!'}
{'message': 'Feedback submitted!'}
{'event_id': 1, 'total_registrations': 1}
{'attendance_percent': 100.0, 'event_id': 1}
{'average_feedback': 5.0, 'event_id': 1}

Total registrations: Shows how many have registered.
Attendance report: Shows the percentage of registered students who have attended.
Feedback report: Shows the average rating of the event.

Personal Touch / Deviations
1.I used Flask and SQLite to keep the project light  and easy to run.
2.I created a test_api.py  to test the APIs without Postman.
3.Kept the JSON responses simple and readable.

Clarity and Simplicity of the project is considered rather than making it complex.
