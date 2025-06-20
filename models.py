from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class TodoModel(Base):
    __tablename__ = 'todos'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)             # Added length
    description = Column(String(500), index=True, nullable=True)  # Added length
    completed = Column(Boolean, index=True, default=False)        # Use Boolean not 0/1 directly
