from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import *
from app import db

company_bp = Blueprint("company", __name__)
from datetime import datetime

@company_bp.route("/create-drive", methods=["POST"])
@jwt_required()
def create_drive():

    company_id = get_jwt_identity()

    data = request.get_json()

    deadline = datetime.strptime(
        data["deadline"], "%Y-%m-%d"
    ).date()

    drive = PlacementDrive(
        company_id=company_id,
        title=data["title"],
        job_description=data["description"],
        salary=data["salary"],
        location=data["location"],
        application_deadline=deadline,
        status="Upcoming"
    )

    db.session.add(drive)
    db.session.commit()

    return jsonify({"message": "Drive created"})
# LIST DRIVES
@company_bp.route("/drives", methods=["GET"])
@jwt_required()
def get_drives():

    user_id = get_jwt_identity()

    print("Company requesting drives:", user_id)

    drives = PlacementDrive.query.filter_by(company_id=user_id).all()

    result = []

    for d in drives:
        result.append({
            "id": d.id,
            "title": d.title,
            "deadline": str(d.application_deadline),
            "status": d.status
        })

    return jsonify(result)


# MARK DRIVE COMPLETE
@company_bp.route("/drive/<int:id>/complete", methods=["PUT"])
@jwt_required()
def complete_drive(id):

    drive = PlacementDrive.query.get(id)

    drive.status = "Closed"

    db.session.commit()

    return jsonify({"message": "Drive completed"})

@company_bp.route("/drive/<int:drive_id>/applications", methods=["GET"])
@jwt_required()
def get_applications(drive_id):

    applications = Application.query.filter_by(drive_id=drive_id).all()

    result = []

    for app in applications:

        student = StudentProfile.query.filter_by(id=app.student_id).first()
        user = User.query.filter_by(id=student.user_id).first()

        result.append({
            "application_id": app.id,
            "student_name": user.name,
            "branch": student.branch,
            "cgpa": student.cgpa,
            "status": app.status
        })

    return jsonify(result)
# UPDATE APPLICATION STATUS
@company_bp.route("/application/<int:id>/status", methods=["PUT"])
@jwt_required()
def update_status(id):

    data = request.get_json()

    app = Application.query.get(id)

    app.status = data["status"]

    db.session.commit()

    return jsonify({"message": "Status updated"})