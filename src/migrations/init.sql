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
    Author_ID UUID,
    Book_ID UUID,
    PRIMARY KEY (Author_ID, Book_ID),
    FOREIGN KEY (Author_ID) REFERENCES Authors(ID),
    FOREIGN KEY (Book_ID) REFERENCES Books(ID)
);

-- Таблица "Бронирование_книг"
CREATE TABLE Book_Reservations (
    User_ID UUID,
    Book_ID UUID,
    Reservation_Date DATE,
    PRIMARY KEY (User_ID, Book_ID),
    FOREIGN KEY (User_ID) REFERENCES Users(ID),
    FOREIGN KEY (Book_ID) REFERENCES Books(ID)
);