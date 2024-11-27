import os

db_user: str = 'postgres'
db_port: int = 4221
db_host: str = 'localhost'
db_password: str = 'Edwige_sroot'
db_table: str = 'diarydb'

# DATABASE_URL = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_table}'

class Config:
    SECRET_KEY = '51b06bae406ef1d771a8380955ddc8ac9b2e56e7f0211b7c'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_table}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

