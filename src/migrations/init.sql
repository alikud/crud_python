-- Таблица "Авторы"
CREATE TABLE Authors (
    ID UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    Name VARCHAR(255) NOT NULL
);

-- Таблица "Книги"
CREATE TABLE Books (
    ID UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    Title VARCHAR(255) NOT NULL,
);

-- Таблица "Авторы_Книги"
CREATE TABLE Authors_Books (
    ID UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    Author_ID UUID,
    Book_ID UUID,
    FOREIGN KEY (Author_ID) REFERENCES Authors(ID),
    FOREIGN KEY (Book_ID) REFERENCES Books(ID)
);
