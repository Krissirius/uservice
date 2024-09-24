from sqlalchemy import Column, Integer, String
from db.base_class import Base

class Department(Base):
    __tablename__ = "ref_departments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)