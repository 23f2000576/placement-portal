from app import create_app
from app.extensions import db
from app.models import User
from app.utils.security import hash_password

app = create_app()


def init_db():

    with app.app_context():

        db.create_all()

        if not User.query.filter_by(role="ADMIN").first():

            admin = User(
                name="Admin",
                email="admin@ppa.com",
                password=hash_password("admin123"),
                role="ADMIN"
            )

            db.session.add(admin)
            db.session.commit()

            print("Admin created")


if __name__ == "__main__":

    init_db()

    app.run(debug=True)