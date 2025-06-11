from app import db

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=True)
    duration = db.Column(db.String(64), nullable=True)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Course {self.name}>' 