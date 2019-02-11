import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy_utils import JSONType

Base = declarative_base()
DB_URI = 'sqlite:///database.db'


class History(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    radius = Column(Integer, nullable=False)
    initial_latitude = Column(Float, nullable=False)
    initial_longitude = Column(Float, nullable=False)
    items = Column(JSONType, nullable=False)
    dbDistance = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.now)


if __name__ == "__main__":
    from sqlalchemy import create_engine

    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
