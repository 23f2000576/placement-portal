from celery import Celery
from celery.schedules import crontab

celery = Celery(
    "placement_portal",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["app.tasks"]   # automatically load tasks
)

# ----------------------------
# Celery Beat Scheduled Jobs
# ----------------------------

celery.conf.beat_schedule = {

    # DAILY DEADLINE REMINDER
    "daily-deadline-reminder": {
        "task": "app.tasks.send_deadline_reminders",
        "schedule": crontab(hour=9, minute=0),  # everyday 9 AM
    },

    # MONTHLY ADMIN REPORT
    "monthly-placement-report": {
        "task": "app.tasks.generate_monthly_report",
        "schedule": crontab(day_of_month=1, hour=9, minute=0),
    },

}

celery.conf.timezone = "Asia/Kolkata"