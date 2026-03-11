from app.celery_worker import celery
import csv
from datetime import date, timedelta


# --------------------------------------------------
# 1️⃣ EXPORT APPLICATIONS CSV
# --------------------------------------------------
@celery.task(name="app.tasks.export_applications_csv")
def export_applications_csv(student_id):

    from app import create_app
    from app.models import Application, PlacementDrive, CompanyProfile, StudentProfile, User

    app = create_app()

    with app.app_context():

        apps = Application.query.filter_by(student_id=student_id).all()

        filename = f"applications_{student_id}.csv"

        with open(filename, "w", newline="") as f:

            writer = csv.writer(f)

            writer.writerow([
                "Student ID",
                "Company",
                "Drive",
                "Status",
                "Applied Date"
            ])

            for app_row in apps:

                drive = PlacementDrive.query.get(app_row.drive_id)
                company = CompanyProfile.query.get(drive.company_id)

                writer.writerow([
                    student_id,
                    company.company_name,
                    drive.title,
                    app_row.status,
                    app_row.applied_at
                ])

        print("CSV export completed")


# --------------------------------------------------
# 2️⃣ DAILY DEADLINE REMINDER
# --------------------------------------------------
@celery.task(name="app.tasks.send_deadline_reminders")
def send_deadline_reminders():

    from app import create_app
    from app.models import PlacementDrive, StudentProfile, User
    from app.extensions import mail
    from flask_mail import Message

    app = create_app()

    with app.app_context():

        tomorrow = date.today() + timedelta(days=1)

        drives = PlacementDrive.query.filter(
            PlacementDrive.application_deadline == tomorrow
        ).all()

        students = StudentProfile.query.all()

        for drive in drives:

            for student in students:

                user = User.query.get(student.user_id)

                msg = Message(
                    subject="Placement Drive Deadline Reminder",
                    sender=app.config["MAIL_USERNAME"],
                    recipients=[user.email]
                )

                msg.body = f"""
Hello {user.name},

Reminder: Application deadline for {drive.title} is tomorrow.

Location: {drive.location}
Salary: {drive.salary}

Please apply before the deadline.

Placement Portal
"""

                mail.send(msg)

        print("Daily reminders sent")


# --------------------------------------------------
# 3️⃣ MONTHLY ADMIN REPORT
# --------------------------------------------------
@celery.task(name="app.tasks.generate_monthly_report")
def generate_monthly_report():

    from app import create_app
    from app.models import PlacementDrive, Application, User
    from app.extensions import mail
    from flask_mail import Message

    app = create_app()

    with app.app_context():

        total_drives = PlacementDrive.query.count()
        total_applications = Application.query.count()

        selected_students = Application.query.filter_by(
            status="Selected"
        ).count()

        html_report = f"""
        <h2>Monthly Placement Activity Report</h2>

        <p><b>Total Drives Conducted:</b> {total_drives}</p>
        <p><b>Total Applications:</b> {total_applications}</p>
        <p><b>Students Selected:</b> {selected_students}</p>

        <br>

        <p>Generated automatically by Placement Portal</p>
        """

        admin = User.query.filter_by(role="ADMIN").first()

        msg = Message(
            subject="Monthly Placement Activity Report",
            sender=app.config["MAIL_USERNAME"],
            recipients=[admin.email]
        )

        msg.html = html_report

        mail.send(msg)

        print("Monthly report sent to admin")