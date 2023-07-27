from config.config import Config
from db.psql import Postgres
from repositories.authors import AuthorRepository
from repositories.books import BooksRepository


config = Config()
psql_db = Postgres(config)
author_repo = AuthorRepository(repo=psql_db)
book_repo = BooksRepository(repo=psql_db)
