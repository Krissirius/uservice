from sqlalchemy import Column, Integer, String, Boolean#, DateTime, ForeignKey
#from sqlalchemy.orm import relationship
#from datetime import datetime
from db.base_class import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    userName = Column(String)
    email = Column(String)
    numberPhone = Column(String)
    password = Column(String)

    status = Column(Boolean, default=True)
    idDepartment = Column(Integer, nullable=True)
    code = Column(String)

    # Boolean fields
    accept = Column(Boolean, default=False)
    share = Column(Boolean, default=False)
    created = Column(Boolean, default=False)#Column(DateTime, default=datetime.utcnow)
    checked = Column(Boolean, default=False)
    closed = Column(Boolean, default=False)
    contract = Column(Boolean, default=False)
    admin = Column(Boolean, default=False)
    editor = Column(Boolean, default=False)

    # Additional fields
    completed = Column(Boolean, default=False)
    techSpecification = Column(Boolean, default=False)

    # Foreign key to the electronic signature
    idElecSignature = Column(Integer, nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, login={self.login}, email={self.email}, status={self.status})>"