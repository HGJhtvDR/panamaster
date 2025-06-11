from datetime import datetime

from app import db

class Job(db.Model):
    __tablename__ = 'jobs'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    requirements = db.Column(db.Text)
    location = db.Column(db.String(100))
    salary_range = db.Column(db.String(100))
    employment_type = db.Column(db.String(50))  # full-time, part-time, contract
    department = db.Column(db.String(100))
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    applications = db.relationship('JobApplication', backref='job', lazy=True)
    
    def __repr__(self):
        return f'<Job {self.title}>'

class JobApplication(db.Model):
    __tablename__ = 'job_applications'
    
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    cover_letter = db.Column(db.Text)
    resume = db.Column(db.String(200))
    status = db.Column(db.String(50), default='pending')  # pending, reviewed, accepted, rejected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('job_applications', lazy=True))
    
    def __repr__(self):
        return f'<JobApplication {self.id}>' 