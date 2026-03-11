pip install -r requirements.txt
pip install flask-cors
"C:\Program Files\Redis\redis-server.exe"
python run.py
celery -A app.celery_worker.celery worker --loglevel=info
celery -A app.celery_worker.celery worker --pool=solo --loglevel=info
celery -A app.celery_worker.celery beat
pip install flower
celery -A app.celery_worker.celery flower


Placement Portal (Flask + Vue + Celery)

A Placement Management System built using:

Flask – Backend API

VueJS – Frontend UI

SQLite – Database

Redis – Caching & Task Queue

Celery – Background Jobs

SMTP Email – Notifications

The portal supports Students, Companies, and Admin workflows for placement drives.

Features
Student

View companies with placement drives

Apply for drives

Upload resume

View application history

Export application history as CSV (Async Job)

Receive deadline reminder emails

Company

Create placement drives

View applications

Review student resume

Update application status (Shortlisted / Waiting / Rejected)

Admin

View all companies and students

Approve companies

Manage placement drives

View student applications

Search companies and students

Async Jobs (Celery)

The system includes three background jobs:

1️⃣ Daily Reminder Job

Runs daily and sends reminder emails to students about upcoming application deadlines.

2️⃣ Monthly Admin Report

Generates a monthly report including:

Number of drives conducted

Number of applications

Placement activity summary

Sent to Admin via email.

3️⃣ Export Applications (User Triggered)

Students can export their application history as CSV.

CSV includes:

Student ID

Company Name

Drive Title

Application Status

Applied Date

Export runs as a Celery background job.

Project Structure
backend
│
├── app
│   ├── routes
│   │   ├── student.py
│   │   ├── company.py
│   │   └── admin.py
│   │
│   ├── models.py
│   ├── tasks.py
│   ├── celery_worker.py
│   ├── extensions.py
│   └── utils
│
├── uploads
│
├── run.py
├── requirements.txt
Installation
1️⃣ Clone Repository
git clone <repository_url>
cd backend
2️⃣ Create Virtual Environment

Windows:

python -m venv venv

Activate:

venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Install Redis

Download Redis for Windows.

Install Redis and ensure it is available in:

C:\Program Files\Redis
Start Redis Server
"C:\Program Files\Redis\redis-server.exe"

Test Redis:

redis-cli ping

Expected output:

PONG
Run Flask Backend
python run.py

Server runs on:

http://127.0.0.1:5000
Run Celery Worker

Celery processes background jobs like:

CSV export

Email sending

Reminder jobs

Run Celery worker:

celery -A app.celery_worker.celery worker --pool=solo --loglevel=info

⚠️ Windows requires:

--pool=solo
Run Celery Beat (Scheduled Jobs)

For daily and monthly tasks:

celery -A app.celery_worker.celery beat
Optional: Monitor Celery Tasks (Flower)

Install:

pip install flower

Run:

celery -A app.celery_worker.celery flower

Open dashboard:

http://localhost:5555
Email Configuration

SMTP is used for notifications.

Example Gmail configuration:

SMTP_SERVER = smtp.gmail.com
SMTP_PORT = 587
EMAIL = your_email@gmail.com
PASSWORD = gmail_app_password

Use Google App Password, not your Gmail password.

Default Admin Account

When the server starts, an admin account is automatically created.

Email: admin@ppa.com
Password: admin123
Redis Caching

Redis is used to cache frequently used APIs such as:

Companies list

Placement drives

This improves performance.

requirements.txt

Add the following:

Flask
Flask-JWT-Extended
Flask-SQLAlchemy
Flask-Cors
celery
redis
flower
python-dotenv
werkzeug

Install with:

pip install -r requirements.txt
Running the Full System

Open three terminals.

Terminal 1

Start Redis

"C:\Program Files\Redis\redis-server.exe"
Terminal 2

Run Flask

python run.py
Terminal 3

Run Celery

celery -A app.celery_worker.celery worker --pool=solo --loglevel=info
Technology Stack
Component	Technology
Backend	Flask
Frontend	VueJS
Database	SQLite
Cache	Redis
Background Jobs	Celery
Email	SMTP
Future Improvements

Interview scheduling

Real-time notifications

Company analytics

Placement statistics dashboard
