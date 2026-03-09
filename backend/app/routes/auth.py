from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models import User, StudentProfile, CompanyProfile
from app import db
from app.utils.security import hash_password, verify_password

auth_bp = Blueprint("auth", __name__)


# ---------------- SIGNUP ----------------
@auth_bp.route("/signup", methods=["POST"])
def signup():

    print("\n----- SIGNUP REQUEST RECEIVED -----")

    data = request.get_json()
    print("Signup Data:", data)

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    print("Name:", name)
    print("Email:", email)
    print("Role:", role)

    # Admin signup not allowed
    if role == "ADMIN":
        print("Admin signup attempted - blocked")
        return jsonify({"error": "Admin registration not allowed"}), 403

    # Check existing user
    existing = User.query.filter_by(email=email).first()

    if existing:
        print("User already exists:", email)
        return jsonify({"error": "Email already exists"}), 400

    print("Creating new user...")

    user = User(
        name=name,
        email=email,
        password=hash_password(password),
        role=role
    )

    db.session.add(user)
    db.session.commit()

    print("User created with ID:", user.id)

    # Create profile based on role
    if role == "STUDENT":
        print("Creating Student Profile")
        profile = StudentProfile(user_id=user.id)
        db.session.add(profile)

    elif role == "COMPANY":
        profile = CompanyProfile(
        user_id=user.id,
        company_name=name,   # important
        description=""
    )

    db.session.add(profile)

    db.session.commit()

    print("Signup successful\n")

    return jsonify({"message": f"{role} registered successfully"}), 201


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

    access_token = create_access_token(identity=str(user.id))

    return jsonify({
        "token": access_token,
        "role": user.role,
        "user_id": user.id
    })