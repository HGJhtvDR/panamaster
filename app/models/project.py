from app import db

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(256), nullable=True)
    client = db.Column(db.String(128), nullable=True)
    completion_date = db.Column(db.Date, nullable=True)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Project {self.name}>' 