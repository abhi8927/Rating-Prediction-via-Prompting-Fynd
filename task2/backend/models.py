"""
Database models for the feedback system.
Uses SQLite with SQLAlchemy for ORM.
"""

from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Review(Base):
    """
    Review model representing a user submission.
    """
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_rating = Column(Integer, nullable=False)
    user_review = Column(Text, nullable=False)
    ai_response = Column(Text, nullable=True)
    ai_summary = Column(Text, nullable=True)
    recommended_actions = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    def to_dict(self):
        """
        Converts the review to a dictionary for JSON serialization.
        """
        return {
            "id": self.id,
            "user_rating": self.user_rating,
            "user_review": self.user_review,
            "ai_response": self.ai_response,
            "ai_summary": self.ai_summary,
            "recommended_actions": self.recommended_actions,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


def init_database(db_path="database.db"):
    """
    Initializes the database and creates tables.
    Returns a session factory for creating database sessions.
    """
    engine = create_engine(f'sqlite:///{db_path}', echo=False)
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal
