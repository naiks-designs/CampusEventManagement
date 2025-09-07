import requests

BASE = "http://127.0.0.1:5000"

# Add a student
r = requests.post(f"{BASE}/students", json={"name":"Alice","email":"alice@example.com"})
print(r.json())

# Create event
r = requests.post(f"{BASE}/events", json={"name":"Tech Workshop","type":"Workshop","date":"2025-09-10"})
print(r.json())

# Register student
r = requests.post(f"{BASE}/register", json={"student_id":1,"event_id":1})
print(r.json())

# Mark attendance
r = requests.post(f"{BASE}/attendance", json={"student_id":1,"event_id":1,"status":"Present"})
print(r.json())

# Submit feedback
r = requests.post(f"{BASE}/feedback", json={"student_id":1,"event_id":1,"rating":5,"comment":"Great!"})
print(r.json())

# Reports
r = requests.get(f"{BASE}/reports/registrations/1")
print(r.json())

r = requests.get(f"{BASE}/reports/attendance/1")
print(r.json())

r = requests.get(f"{BASE}/reports/feedback/1")
print(r.json())
