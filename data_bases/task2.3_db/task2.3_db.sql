--Задание 1
--Создайте новую таблицу potential customers с полями id, email, name, surname, second_name, city
--не понятно id новой таблицы соответствует id таблицы Users?
--пока так(новый id)
CREATE TABLE IF NOT EXISTS Potential_customers
(
    id SERIAL NOT NULL PRIMARY KEY,
    email VARCHAR(50),
    name VARCHAR(50),
    surname VARCHAR(50),
    second_name VARCHAR(50),
    city VARCHAR(50)
);

--Заполните данными таблицу.
INSERT INTO Potential_customers (id, email, name, surname, second_name, city)
VALUES ("email@gmail.com", "ivan", "ivanov", "ivanovich", "city 17"),
        ("my_mail@gmail.com", "petr", "petrov", "petrovich", "city 25"),
        ("good_mail@mail.ru", "stepan", "stepanov", "stepanovich", "saint-petersburg"),
        ("mail@gmail.com", "jhon", "blake", NULL, "city 32")
        ;

--Выведите имена и электронную почту потенциальных и существующих пользователей из города city 17
SELECT P.name, P.email FROM Potential_customers WHERE P.city = 'city 17'
UNION
SELECT U.name, U.email FROM Users WHERE U.city = 'city 17';