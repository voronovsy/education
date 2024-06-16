import psycopg2

hostname = '212.109.219.94'
database = 'postgres'
username = 'postgres'
password = 'postgres'
port = 5432


try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=password,
        port=port
    )
    print("Успешное подключение к базе данных")

    # Создание курсора
    cur = conn.cursor()

    # Выполнение запроса
    cur.execute("SELECT version();")

    # Получение результата
    db_version = cur.fetchone()
    print("Версия базы данных:", db_version)

    # Закрытие курсора и соединения
    cur.close()
    conn.close()
    print("Соединение закрыто")

except Exception as error:
    print("Ошибка при подключении к базе данных:", error)
