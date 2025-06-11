from datetime import datetime
from slugify import slugify

from app import db

class Article(db.Model):
    __tablename__ = 'articles'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.String(500))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    published = db.Column(db.Boolean, default=False)
    meta_title = db.Column(db.String(200))
    meta_description = db.Column(db.String(300))
    
    author = db.relationship('User', backref=db.backref('articles', lazy=True))
    
    def __init__(self, *args, **kwargs):
        if 'title' in kwargs and 'slug' not in kwargs:
            kwargs['slug'] = slugify(kwargs['title'])
        super().__init__(*args, **kwargs)
        
    def __repr__(self):
        return f'<Article {self.title}>' 