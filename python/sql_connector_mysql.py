import pymysql

try:
    connection = pymysql.connect(
        host='212.109.219.94',
        database='test',
        user='root',
        password='Apach1Mysql2'
    )

    with connection.cursor() as cursor:
        cursor.execute("SELECT DATABASE();")
        result = cursor.fetchone()
        print(f"You're connected to database: {result}")

except pymysql.MySQLError as e:
    print(f"Error while connecting to MySQL: {e}")
finally:
    connection.close()
    print("MySQL connection is closed")
