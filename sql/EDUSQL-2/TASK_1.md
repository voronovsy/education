### SELECT - запросы

SELECT * FROM <table>; - Получение всех данных из таблицы

SELECT - оператор
* - пол, данные из которых нужно вывести
FROM - оператор
table - имя таблицы

Результатом выаолнения SELECT - запроса - всегда таблица


Вывод отдельных полей таблиц

SELECT field1, field2
FROM <table>;

field - название поля


Изменение имен полей в запросах

SELECT
    field1 AS f1,
    field2 AS f2
FROM <table>

Оператор AS можно не указывать


Изменение данных в SELECT - запросах

SELECT
    (field1 + field2) AS total
FROM <table>;