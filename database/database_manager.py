from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.lego_database import *


def init_database():
    engine = create_engine(DB_SQLITE_URI, echo=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add_all([
        Theme(name="Star Wars"),
        Theme(name="Monster Fighters"),
        Theme(name="City"),
        Theme(name="Harry Potter"),
        LegoSet(serial="75054", name="AT-AT Walker", theme_name="Star Wars"),
        LegoSet(serial="75128", name="TIE Advanced Prototype", theme_name="Star Wars"),
    ])
    session.commit()
    # print(DB_SQLITE_URI)
    # print(DB_SQLITE_URI_REL)


if __name__ == "__main__":
    init_database()
