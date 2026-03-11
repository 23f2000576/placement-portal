from flask_mail import Mail

mail = Mail()

def init_mail(app):

    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 587
    app.config["MAIL_USE_TLS"] = True

    app.config["MAIL_USERNAME"] = "kehachandrakar07@gmail.com"
    app.config["MAIL_PASSWORD"] = "mcidbpgoilngaqtv"

    mail.init_app(app)