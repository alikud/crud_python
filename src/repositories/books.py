class BooksRepository():
    def __init__(self, repo) -> None:
        self.repo = repo

    def create_book(self, data: dict):
        insert_query = "INSERT INTO books (title) VALUES (%s) RETURNING ID"
        insrted_data = (data.get('title'), )
        return self.repo.execute_query(insert_query, insrted_data)

    def get_all_books(self):
        query = "SELECT title FROM books"
        return self.repo.execute_query(query)


    def get_book_by_id(self, book_id):
        query = "SELECT title FROM books WHERE id = %s"
        insrted_data = (book_id,)
        return self.repo.execute_query(query, insrted_data)

    def find_book_by_title(self, title):
            query = "SELECT * FROM books WHERE title ILIKE %s"
            data = (f"%{title}%",)  # Добавляем знаки % для нечеткого поиска
            result = self.repo.execute_query(query, data)
            return result

    def update_book_by_id(self, book_id, data):
        query = "UPDATE books SET (title) = (%s) WHERE id = %s"
        insrted_data = (data.get('title'), book_id, )
        return self.repo.execute_query(query, insrted_data)


    def delete_book_by_id(self, book_id):
        query = "DELETE FROM books WHERE id = %s RETURNING title"
        data = (book_id,)
        result = self.repo.execute_query(query, data)
        return result[0] if result else None

    def make_author_book_link(self, author_id, book_id):
        query_link_author_book = "INSERT INTO authors_books (author_id, book_id) VALUES (%s, %s) RETURNING ID"
        data_link_author_book = (author_id, book_id)
        return self.repo.execute_query(query_link_author_book, data_link_author_book)
