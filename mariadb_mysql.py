import pymysql.cursors

connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='!Potter123',
    db='clientes',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    cursor.execute('SELECT * FROM clientes')
    result = cursor.fetchone()
    print(result)

connection.close()
