from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import (
    User,
    StudentProfile,
    CompanyProfile,
    PlacementDrive,
    Application
)
from app import db

admin_bp = Blueprint("admin", __name__)


# ---------------- ROLE CHECK ----------------
def admin_required():
    identity = get_jwt_identity()
    if identity["role"] != "ADMIN":
        return False
    return True


# =====================================================
# DASHBOARD
# =====================================================
@admin_bp.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():
    if not admin_required():
        return jsonify({"error": "Admin only"}), 403

    data = {
        "total_students": StudentProfile.query.count(),
        "total_companies": CompanyProfile.query.count(),
        "total_drives": PlacementDrive.query.count(),
        "total_applications": Application.query.count()
    }

    return jsonify(data)


# =====================================================
# STUDENTS
# =====================================================
@admin_bp.route("/students", methods=["GET"])
@jwt_required()
def get_students():
    if not admin_required():
        return jsonify({"error": "Admin only"}), 403

    students = StudentProfile.query.all()
    result = []

    for s in students:
        user = User.query.get(s.user_id)
        result.append({
            "student_id": s.id,
            "name": user.name,
            "email": user.email,
            "branch": s.branch,
            "cgpa": s.cgpa,
            "year": s.year,
            "blacklisted": user.is_blacklisted
        })

    return jsonify(result)


# =====================================================
# COMPANIES
# =====================================================
@admin_bp.route("/companies", methods=["GET"])
@jwt_required()
def get_companies():
    if not admin_required():
        return jsonify({"error": "Admin only"}), 403

    companies = CompanyProfile.query.all()
    result = []

    for c in companies:
        user = User.query.get(c.user_id)
        result.append({
            "company_id": c.id,
            "company_name": c.company_name,
            "email": user.email,
            "approval_status": c.approval_status,
            "blacklisted": c.is_blacklisted
        })

    return jsonify(result)


# =====================================================
# APPROVE / REJECT COMPANY
# =====================================================
@admin_bp.route("/company/<int:company_id>/approve", methods=["PUT"])
@jwt_required()
def approve_company(company_id):
    if not admin_required():
        return jsonify({"error": "Admin only"}), 403

    company = CompanyProfile.query.get_or_404(company_id)
    company.approval_status = "Approved"
    db.session.commit()

    return jsonify({"message": "Company approved"})


@admin_bp.route("/company/<int:company_id>/reject", methods=["PUT"])
@jwt_required()
def reject_company(company_id):
    if not admin_required():
        return jsonify({"error": "Admin only"}), 403

    company = CompanyProfile.query.get_or_404(company_id)
    company.approval_status = "Rejected"
    db.session.commit()

    return jsonify({"message": "Company rejected"})


# =====================================================
# BLACKLIST / ACTIVATE USER
# =====================================================
@admin_bp.route("/user/<int:user_id>/blacklist", methods=["PUT"])
@jwt_required()
def blacklist_user(user_id):
    if not admin_required():
        return jsonify({"error": "Admin only"}), 403

    user = User.query.get_or_404(user_id)
    user.is_blacklisted = True

    # If company, blacklist company profile also
    company = CompanyProfile.query.filter_by(user_id=user_id).first()
    if company:
        company.is_blacklisted = True

    db.session.commit()

    return jsonify({"message": "User blacklisted"})


@admin_bp.route("/user/<int:user_id>/activate", methods=["PUT"])
@jwt_required()
def activate_user(user_id):
    if not admin_required():
        return jsonify({"error": "Admin only"}), 403

    user = User.query.get_or_404(user_id)
    user.is_blacklisted = False

    company = CompanyProfile.query.filter_by(user_id=user_id).first()
    if company:
        company.is_blacklisted = False

    db.session.commit()

    return jsonify({"message": "User activated"})


# =====================================================
# DRIVES
# =====================================================
@admin_bp.route("/drives", methods=["GET"])
@jwt_required()
def get_all_drives():
    if not admin_required():
        return jsonify({"error": "Admin only"}), 403

    drives = PlacementDrive.query.all()
    result = []

    for d in drives:
        result.append({
            "drive_id": d.id,
            "title": d.title,
            "company_id": d.company_id,
            "status": d.status,
            "deadline": d.application_deadline.isoformat() if d.application_deadline else None
        })

    return jsonify(result)


# ---------------- Pending Drives ----------------
@admin_bp.route("/drives/pending", methods=["GET"])
@jwt_required()
def pending_drives():
    if not admin_required():
        return jsonify({"error": "Admin only"}), 403

    drives = PlacementDrive.query.filter_by(status="Pending").all()
    result = []

    for d in drives:
        result.append({
            "drive_id": d.id,
            "title": d.title,
            "company_id": d.company_id,
            "deadline": d.application_deadline.isoformat() if d.application_deadline else None
        })

    return jsonify(result)


# ---------------- Approve / Reject Drive ----------------
@admin_bp.route("/drive/<int:drive_id>/approve", methods=["PUT"])
@jwt_required()
def approve_drive(drive_id):
    if not admin_required():
        return jsonify({"error": "Admin only"}), 403

    drive = PlacementDrive.query.get_or_404(drive_id)
    drive.status = "Approved"
    db.session.commit()

    return jsonify({"message": "Drive approved"})


@admin_bp.route("/drive/<int:drive_id>/reject", methods=["PUT"])
@jwt_required()
def reject_drive(drive_id):
    if not admin_required():
        return jsonify({"error": "Admin only"}), 403

    drive = PlacementDrive.query.get_or_404(drive_id)
    drive.status = "Rejected"
    db.session.commit()

    return jsonify({"message": "Drive rejected"})


# =====================================================
# APPLICATIONS
# =====================================================
@admin_bp.route("/applications", methods=["GET"])
@jwt_required()
def all_applications():
    if not admin_required():
        return jsonify({"error": "Admin only"}), 403

    apps = Application.query.all()
    result = []

    for a in apps:
        result.append({
            "application_id": a.id,
            "student_id": a.student_id,
            "drive_id": a.drive_id,
            "status": a.status,
            "applied_at": a.applied_at.isoformat()
        })

    return jsonify(result)


# =====================================================
# SEARCH (Bonus - good for viva)
# =====================================================
@admin_bp.route("/search", methods=["GET"])
@jwt_required()
def search_users():
    if not admin_required():
        return jsonify({"error": "Admin only"}), 403

    keyword = request.args.get("q")

    users = User.query.filter(User.name.ilike(f"%{keyword}%")).all()

    result = []
    for u in users:
        result.append({
            "user_id": u.id,
            "name": u.name,
            "email": u.email,
            "role": u.role,
            "blacklisted": u.is_blacklisted
        })

    return jsonify(result)
