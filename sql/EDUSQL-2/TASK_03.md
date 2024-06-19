### Фильтрация данных, оператор WHERE

# Фильтрация равенство числу:

SELECT `id`, `name`
FROM `good`
WHERE `count` = 0

WHERE(где)

# Фильтрация по числам больше или меньше

SELECT `id`, `name`
FROM `good`
WHERE `count` <= 50

# Фильтрация: строка и неравенство


SELECT *
FROM `order_status`
WHERE `code` != 'NEW' - строка в одинарных обычных кавычках

# Фильтрация: Даты

SELECT `id`, `name`, `reg_date`
FROM `user`
WHERE `reg_date` >= '2019-01-01'

# Фильтрация по диапазону дат и времени

SELECT * FROM `user`
WHERE
    `reg_date` >= '2021-09-08 00:00:00'
    AND
    `reg_date` >= '2021-09-08 23:59:59'

SELECT * FROM `user`
WHERE `reg_date` BETWEEN
    '2021-09-08 00:00:00' AND
    '2021-09-08 23:59:59'