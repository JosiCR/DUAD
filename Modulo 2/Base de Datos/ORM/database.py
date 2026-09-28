from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg://postgres:JosiCR_14@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)