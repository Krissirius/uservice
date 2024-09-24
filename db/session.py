from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import DB_HOST2, DB_NAME2, DB_PASS2, DB_PORT2, DB_USER2
from db.base_class import Base  # Импортируем Base для работы с моделями

DATABASE_URL = f"mssql+pyodbc://{DB_USER2}:{DB_PASS2}@{DB_HOST2}:{DB_PORT2}/{DB_NAME2}?driver=ODBC+Driver+17+for+SQL+Server&timeout=60&Encrypt=no"

engine=create_engine(DATABASE_URL,pool_size=200, max_overflow=300,pool_timeout=30)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание всех таблиц, если они ещё не существуют
def init_db():
    Base.metadata.create_all(bind=engine)  # Создаёт таблицы