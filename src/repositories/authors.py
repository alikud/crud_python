from fastapi import HTTPException
import logging

class AuthorRepository():
    def __init__(self, repo) -> None:
        self.repo = repo

    def create_author(self, data: dict):
        insert_query = "INSERT INTO authors (name) VALUES (%s) RETURNING ID"
        insrted_data = (data.get('name'), )
        return self.repo.execute_query(insert_query, insrted_data)

    def get_all_authors(self):
        query = "SELECT name FROM authors"
        return self.repo.execute_query(query)


    def get_author_by_id(self, author_id):
        query = "SELECT name FROM authors WHERE id = %s"
        insrted_data = (author_id,)
        return self.repo.execute_query(query, insrted_data)

    def get_author_by_name(self, name):
        query_author = "SELECT id FROM authors WHERE name = %s"
        data_author = (name,)
        author_id = self.repo.execute_query(query_author, data_author)

        if not author_id:
            raise HTTPException(status_code=404, detail="Автор не найден.")

        return author_id

    def find_author_by_name(self, name):
        query = "SELECT * FROM authors WHERE name ILIKE %s"
        data = (f"%{name}%",)  # Добавляем знаки % для нечеткого поиска
        result = self.repo.execute_query(query, data)
        return result

    def update_author(self, auhtor_id, data):
        query = "UPDATE authors SET (name) = (%s) WHERE id = %s"
        insrted_data = (data.get('name'), auhtor_id, )
        return self.repo.execute_query(query, insrted_data)


    def delete_author_by_id(self, author_id):
        query = "DELETE FROM authors WHERE id = %s RETURNING *"
        data = (author_id,)
        result = self.repo.execute_query(query, data)
        return result[0] if result else None
