from datetime import datetime

from app import db

class Knowledge(db.Model):
    __tablename__ = 'knowledge'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text)
    category = db.Column(db.String(50))  # codimag, parker, etc.
    type = db.Column(db.String(50))      # manual, firmware, driver, case
    file_path = db.Column(db.String(200))
    version = db.Column(db.String(50))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    published = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    author = db.relationship('User', backref=db.backref('knowledge', lazy=True))
    
    def __repr__(self):
        return f'<Knowledge {self.title}>' 