from sqlmodel import SQLModel, create_engine

DB_PATH = f"sqlite:///database.db"

engine = create_engine(DB_PATH)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
