from . import db
from datetime import datetime

# ---------------- USERS ----------------
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20))  # ADMIN, STUDENT, COMPANY
    is_active = db.Column(db.Boolean, default=True)
    is_blacklisted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# ---------------- STUDENT PROFILE ----------------
class StudentProfile(db.Model):
    __tablename__ = "student_profiles"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    roll_number = db.Column(db.String(50))
    branch = db.Column(db.String(50))
    year = db.Column(db.Integer)
    cgpa = db.Column(db.Float)
    phone = db.Column(db.String(20))
    resume_path = db.Column(db.String(200))
    skills = db.Column(db.Text)
    placement_status = db.Column(db.String(20), default="Not Placed")


# ---------------- COMPANY PROFILE ----------------
class CompanyProfile(db.Model):
    __tablename__ = "company_profiles"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    company_name = db.Column(db.String(100))
    website = db.Column(db.String(200))
    hr_name = db.Column(db.String(100))
    hr_email = db.Column(db.String(120))
    hr_phone = db.Column(db.String(20))
    description = db.Column(db.Text)
    approval_status = db.Column(db.String(20), default="Pending")
    is_blacklisted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# ---------------- PLACEMENT DRIVE ----------------
class PlacementDrive(db.Model):
    __tablename__ = "placement_drives"

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("company_profiles.id"))
    title = db.Column(db.String(100))
    job_description = db.Column(db.Text)
    salary = db.Column(db.Integer)
    location = db.Column(db.String(100))
    drive_date = db.Column(db.Date)
    application_deadline = db.Column(db.Date)
    status = db.Column(db.String(20), default="Pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# ---------------- DRIVE ELIGIBILITY ----------------
class DriveEligibility(db.Model):
    __tablename__ = "drive_eligibility"

    id = db.Column(db.Integer, primary_key=True)
    drive_id = db.Column(db.Integer, db.ForeignKey("placement_drives.id"))
    allowed_branches = db.Column(db.String(200))  # CSV
    min_cgpa = db.Column(db.Float)
    passing_year = db.Column(db.Integer)


# ---------------- APPLICATIONS ----------------
class Application(db.Model):
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student_profiles.id"))
    drive_id = db.Column(db.Integer, db.ForeignKey("placement_drives.id"))
    applied_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default="Applied")
    remarks = db.Column(db.Text)

    __table_args__ = (
        db.UniqueConstraint("student_id", "drive_id"),
    )


# ---------------- INTERVIEWS ----------------
class Interview(db.Model):
    __tablename__ = "interviews"

    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey("applications.id"))
    interview_date = db.Column(db.DateTime)
    mode = db.Column(db.String(50))  # Online / Offline
    result = db.Column(db.String(50))
    notes = db.Column(db.Text)


# ---------------- NOTIFICATIONS ----------------
class Notification(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    message = db.Column(db.Text)
    type = db.Column(db.String(50))
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# ---------------- ACTIVITY LOG ----------------
class ActivityLog(db.Model):
    __tablename__ = "activity_logs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    action = db.Column(db.String(200))
    entity_type = db.Column(db.String(50))
    entity_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
