from cgitb import reset

from fastapi import APIRouter, status
from models.authors import AuthorBase

from api.dependencies import author_repo

router = APIRouter(
    prefix="/authors",
    tags=["authors"],
)


@router.post("")
def add_author(author: AuthorBase, status_code = status.HTTP_200_OK):
    """
    Эндпоинт создания автора в базе данных, возвращает id созданной записи
    """
    res = author_repo.create_author(author.dict())
    return {"Created": res}


@router.get("")
def get_authors(status_code = status.HTTP_200_OK):
    """
    Эндпоинт для получения всех авторов из базы
    """
    res = author_repo.get_all_authors()
    return {"Result": res}

@router.get("/{author_name}")
def find_author_by_name(auhtor_name: str):
    """
    Эндпоинт для поиска автора по его имени(возможно с опечатками),
    возвращает список от наиболее подходящего до наименее
    """
    res = author_repo.find_author_by_name(auhtor_name)
    return {"Result": res}

@router.post("")
def get_author_by_name(author: AuthorBase):
    """
    Эндпоинт для получения id автора по его имени, если оно известно заранее
    """
    res = author_repo.get_author_by_name(author.name)
    return {"id": res}

@router.post("/{author_id}", status_code=status.HTTP_200_OK)
def get_author_by_id(author_id: str):
    """
    Эндпоинт для получения информации об авторе  по его id
    """
    res = author_repo.get_author_by_id(author_id)
    return {"Author": res}

@router.delete("/{author_id}", status_code=status.HTTP_200_OK)
def delete_author_by_id(author_id: str):
    """
    Эндпоинт удаления автора из базы
    """
    res = author_repo.delete_author_by_id(author_id)
    return {"Deleted": res}

@router.patch("/{author_id}")
def update_author_by_id(author_id: str, author: AuthorBase, status_code=status.HTTP_200_OK):
    """
    Эндпоинт для обновления информации об авторе по его id
    """
    res = author_repo.update_author(author_id, author.dict())
    return {"Updated": res}
