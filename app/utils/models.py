from flask_sqlalchemy import SQLAlchemy
from app import create_app, db

db.Model.metadata.reflect(db.engine)

class Monster(db.Model):
    __tablename__ = 'monsters'
    __table_args__ = { 'extend_existing': True }
    name = db.Column(db.Text, primary_key=True)

class BiomeMonster(db.Model):
    __tablename__ = 'biome_monsters'
    __table_args__ = { 'extend_existing': True }
    monster_id = db.Column(db.Integer, primary_key=True)