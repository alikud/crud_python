## О проекте
Приложение реализует CRUD для библиотеки, можно добавить книгу, найти по названию, изменить и удалить. Так же можно добавить автора, связать с книгой, у автора может быть много книг, а у книг может быть много авторов (N:M). Использован фреймворк FastApi , база данных - PostgreSQL


### Запуск приложения
1. Создать виртуальное окружение и установить зависимости, так же создать .env файл
   ```
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   touch .env
   ```
   Пример содержимого .env файла
   ```
   POSTGRES_USER=myuser
   POSTGRES_PASSWORD=mypassword
   POSTGRES_DB=mydatabase
   ```

   
3. Вызвать в терминале `python3 src/main.py` или make serv


### Документация к API
![Документация к проекту](https://github.com/alikud/crud_python/blob/master/library_doc_screen.png)
