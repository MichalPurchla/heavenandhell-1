from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    pesel = Column(String(11), unique=True, nullable=False)
    phone = Column(String(20))
    address = Column(String(50))


class OnlineCourse(Base):
    __tablename__ = "online_courses"

    id = Column(Integer, primary_key=True)
    url = Column(String(50), nullable=False)


class OnsiteCourse(Base):
    __tablename__ = "onsite_courses"

    id = Column(Integer, primary_key=True)
    address = Column(String(50), nullable=False)
    time = Column(String(10), nullable=False)
    days = Column(Integer, nullable=False)


class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    pesel = Column(String(11), unique=True, nullable=False)
    phone = Column(String(20))
    address = Column(String(50))
    enrollment_date = Column(DateTime, nullable=False, default=datetime.now)


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    budget = Column(Float, nullable=False)
    address = Column(String(50))
