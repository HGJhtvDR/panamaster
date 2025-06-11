from app import db
from datetime import datetime

class Training(db.Model):
    __tablename__ = 'trainings'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, active, completed, cancelled
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = db.relationship('User', backref=db.backref('trainings', lazy=True))
    course = db.relationship('Course', backref=db.backref('trainings', lazy=True))
    
    def __repr__(self):
        return f'<Training {self.id}: {self.user_id} - {self.course_id}>' 