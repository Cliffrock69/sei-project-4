import os

db_uri = os.getenv('DATABASE_URL', 'postgres://localhost:5432/electric')

secret = os.getenv('SECRET', 'my secret')
