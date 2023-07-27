from fastapi import APIRouter, status
from models.books import BookBase

from api.dependencies import author_repo, book_repo

router = APIRouter(
    prefix="/books",
    tags=["books"],
)


@router.post("")
def add_book(book: BookBase, status_code = status.HTTP_201_CREATED):
    """
    эндпоинт для добавления книг в базу, учитывая, что автор может быть неизвестен
    когда создается книга, надо связать ее с автором в таблице аввторы_книги, для этого надо проверить,
    существует ли автор, если нет, его создать, далее взять book_id , взять author_id и занести их в базу авторы_книги
    """

    for author_name in book.authors:
        author_id = author_repo.get_author_by_name(author_name)
        if not author_id[0][0]:
            #если автора нет нужно его создать
            author_id = author_repo.create_author({"name": author_name})
        book_id = book_repo.create_book(book.dict())
        link_id = book_repo.make_author_book_link(author_id[0][0], book_id[0][0])
    return {"Created": link_id}

@router.get("")
def get_book_by_id(bookd_id):
    """
    Эндпоинт для получения информации о книге по ее id
    """
    res = book_repo.get_book_by_id(bookd_id)
    return {"Result": res}

@router.get("")
def get_books(skip: int = 0, limit: int = 10, status_code = status.HTTP_200_OK):
    """
    Эндпоинт для получения всех книг в базе, используются query params skip, limit
    http://127.0.0.1:8000/books/?skip=0&limit=10
    """
    res = book_repo.get_all_books()
    return {"Result": res}

@router.get("/{title}", status_code=status.HTTP_200_OK)
def find_book_by_title(title: str):
    """
    Эндопнит для поиска книги по ее названию
    """
    res = book_repo.find_book_by_title(title)
    return {"Result": res}

@router.delete("/{book_id}", status_code=status.HTTP_200_OK)
def delete_book_by_id(book_id: str):
    """
    Эндпоинт для удаления книги из базы по ее id
    """
    res = book_repo.delete_book_by_id(book_id)
    return {"Deleted": res}

@router.patch("/{book_id}")
def update_book_by_id(book_id: str, book: BookBase, status_code=status.HTTP_200_OK):
    """
    Эндпоинт для обновления информации о книге по ее id
    """
    res = book_repo.update_book_by_id(book_id, book.dict())
    return {"Updated": res}
