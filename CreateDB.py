from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()


class Site(Base):
    __tablename__ = "Site"
    site_id = Column(Integer, primary_key=True)
    url = Column(String)
    time_active = Column(Integer)
    html5 = Column(Boolean)
    ssl = Column(Boolean)


class Page(Base):
    __tablename__ = "Page"
    page_id = Column(Integer, primary_key=True)
    url = Column(String)
    title = Column(String)
    description = Column(String)
    website = Column(Integer)
    dirty_words = Column(String)
