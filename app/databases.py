import models
from sqlmodel import SQLModel, create_engine , Session


sqlite_file_name = "database.db"
sqlite_url = "mysql://root:Start2022@localhost/Fastapi"

engine = create_engine(sqlite_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session