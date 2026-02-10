from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    db.create_all()

    if not User.query.filter_by(role="ADMIN").first():
        admin = User(
            name="Admin",
            email="admin@ppa.com",
            password="admin123",
            role="ADMIN"
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin created")

if __name__ == "__main__":
    app.run(debug=True)
