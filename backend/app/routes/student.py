from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import (
    db,
    StudentProfile,
    CompanyProfile,
    PlacementDrive,
    Application
)
from werkzeug.utils import secure_filename
import os

student_bp = Blueprint("student", __name__)

UPLOAD_FOLDER = "uploads/resumes"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# ---------------------------------------------------------
# 1️⃣ LIST ORGANIZATIONS
# ---------------------------------------------------------
@student_bp.route("/companies", methods=["GET"])
@jwt_required()
def get_companies():

    drives = PlacementDrive.query.filter_by(status="Upcoming").all()

    companies = {}

    for drive in drives:

        company = CompanyProfile.query.get(drive.company_id)

        if company:

            companies[company.id] = {
                "id": company.id,
                "name": company.company_name,
                "description": company.description
            }

    return jsonify(list(companies.values()))


# ---------------------------------------------------------
# 2️⃣ GET DRIVES OF COMPANY
# ---------------------------------------------------------
@student_bp.route("/company/<int:company_id>/drives", methods=["GET"])
@jwt_required()
def get_company_drives(company_id):

    company = CompanyProfile.query.get(company_id)

    if not company:
        return jsonify({"error": "Company not found"}), 404

    drives = PlacementDrive.query.filter_by(
        company_id=company.id,
        status="Upcoming"
    ).all()

    return jsonify([
        {
            "id": d.id,
            "title": d.title,
            "description": d.job_description,
            "salary": d.salary,
            "location": d.location,
            "deadline": d.application_deadline
        }
        for d in drives
    ])


# ---------------------------------------------------------
# 3️⃣ APPLY FOR DRIVE (WITH RESUME)
# ---------------------------------------------------------
@student_bp.route("/apply/<int:drive_id>", methods=["POST"])
@jwt_required()
def apply_for_drive(drive_id):

    user = get_jwt_identity()

    student = StudentProfile.query.filter_by(user_id=user).first()

    if not student:
        return jsonify({"error": "Student profile not found"}), 404

    drive = PlacementDrive.query.get(drive_id)

    if not drive:
        return jsonify({"error": "Drive not found"}), 404

    existing = Application.query.filter_by(
        student_id=student.id,
        drive_id=drive_id
    ).first()

    if existing:
        return jsonify({"error": "Already applied"}), 400

    resume = request.files.get("resume")

    if resume:
        filename = secure_filename(resume.filename)
        path = os.path.join(UPLOAD_FOLDER, filename)
        resume.save(path)
        student.resume_path = path

    application = Application(
        student_id=student.id,
        drive_id=drive_id,
        status="Applied"
    )

    db.session.add(application)
    db.session.commit()

    return jsonify({"message": "Application submitted"})


# ---------------------------------------------------------
# 4️⃣ STUDENT HISTORY
# ---------------------------------------------------------
@student_bp.route("/history", methods=["GET"])
@jwt_required()
def student_history():

    user = get_jwt_identity()

    student = StudentProfile.query.filter_by(user_id=user).first()

    applications = Application.query.filter_by(
        student_id=student.id
    ).all()

    result = []

    for app in applications:

        drive = PlacementDrive.query.get(app.drive_id)

        company = CompanyProfile.query.get(drive.company_id)

        result.append({
            "drive": drive.title,
            "company": company.company_name if company else None,
            "status": app.status,
            "date": app.applied_at
        })

    return jsonify(result)


# ---------------------------------------------------------
# 5️⃣ GET STUDENT PROFILE
# ---------------------------------------------------------
@student_bp.route("/profile", methods=["GET"])
@jwt_required()
def get_profile():

    user = get_jwt_identity()

    student = StudentProfile.query.filter_by(user_id=user).first()

    if not student:
        return jsonify({"error": "Profile not found"}),404

    return jsonify({
        "roll_number": student.roll_number,
        "branch": student.branch,
        "year": student.year,
        "cgpa": student.cgpa,
        "phone": student.phone,
        "skills": student.skills,
        "resume": student.resume_path
    })

# ---------------------------------------------------------
# 6️⃣ UPDATE STUDENT PROFILE
# ---------------------------------------------------------
@student_bp.route("/profile", methods=["PUT"])
@jwt_required()
def update_profile():

    user = get_jwt_identity()

    student = StudentProfile.query.filter_by(user_id=user).first()

    if not student:
        return jsonify({"error": "Profile not found"}), 404

    roll_number = request.form.get("roll_number")
    branch = request.form.get("branch")
    year = request.form.get("year")
    cgpa = request.form.get("cgpa")
    phone = request.form.get("phone")
    skills = request.form.get("skills")

    student.roll_number = roll_number
    student.branch = branch
    student.year = year
    student.cgpa = cgpa
    student.phone = phone
    student.skills = skills

    resume = request.files.get("resume")

    if resume:
        filename = secure_filename(resume.filename)

        path = os.path.join(UPLOAD_FOLDER, filename)

        resume.save(path)

        student.resume_path = path

    db.session.commit()

    return jsonify({"message": "Profile updated"})