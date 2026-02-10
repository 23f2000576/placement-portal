from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models import User, StudentProfile, CompanyProfile
from app import db
from app.utils.security import hash_password, verify_password

auth_bp = Blueprint("auth", __name__)


# ---------------- SIGNUP ----------------
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")  # STUDENT or COMPANY

    # Admin signup not allowed
    if role == "ADMIN":
        return jsonify({"error": "Admin registration not allowed"}), 403

    # Check existing user
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 400

    # Create user
    user = User(
        name=name,
        email=email,
        password=hash_password(password),
        role=role
    )
    db.session.add(user)
    db.session.commit()

    # Create profile based on role
    if role == "STUDENT":
        profile = StudentProfile(user_id=user.id)
        db.session.add(profile)

    elif role == "COMPANY":
        profile = CompanyProfile(user_id=user.id)
        db.session.add(profile)

    db.session.commit()

    return jsonify({"message": f"{role} registered successfully"}), 201


# ---------------- LOGIN ----------------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user or not verify_password(user.password, password):
        return jsonify({"error": "Invalid credentials"}), 401

    if not user.is_active or user.is_blacklisted:
        return jsonify({"error": "Account inactive or blacklisted"}), 403

    access_token = create_access_token(identity={
        "id": user.id,
        "role": user.role
    })

    return jsonify({
        "token": access_token,
        "role": user.role,
        "user_id": user.id
    })
