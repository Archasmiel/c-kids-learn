from sqlalchemy.sql import func
from ..services.database import db


class TeacherRequest(db.Model):
    __tablename__ = "teacher_requests"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)
    status = db.Column(db.String(16), nullable=False, server_default="pending")  # pending|approved|rejected
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)

    user = db.relationship("User", backref=db.backref("teacher_request", uselist=False))
