import os

from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
DB_FILE_NAME = f'{os.path.basename(__file__).split(".")[0]}.db'
DB_PATH = os.path.join(os.path.dirname(__file__), DB_FILE_NAME)
DB_PATH_REL = os.path.relpath(DB_PATH, PROJECT_ROOT)
DB_SQLITE_URI = f"sqlite:///{DB_PATH}"
DB_SQLITE_URI_REL = f"sqlite:///./{DB_PATH_REL}"

Base = declarative_base()


class LegoSet(Base):
    __tablename__ = "lego_set"
    id = Column(Integer, primary_key=True, autoincrement=True)
    serial = Column(String)
    name = Column(String)
    theme_name = Column(String, ForeignKey("theme.name"))
    theme = relationship("Theme", back_populates="lego_sets")


class Theme(Base):
    __tablename__ = "theme"
    name = Column(String, primary_key=True)
    lego_sets = relationship("LegoSet", back_populates="theme")
