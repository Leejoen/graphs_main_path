import sqlite3


def connect():
    try:
        sqlite_connection = sqlite3.connect('db.sqlite3')
        cursor = sqlite_connection.cursor()
        print("База успешно подключена\n")

        cursor.execute('''	
            DELETE FROM main_names;
        ''')
        sqlite_connection.commit()

        cursor.execute('''
            SELECT * FROM main_count; 
        ''')
        record = cursor.fetchall()
        print(record)

        for i in range(1, record[0][1] + 1):
            cursor.execute(f'''
                INSERT INTO main_names
                (num, name, dangerous) VALUES ({i}, 'Вершина {i}', {False})
            ''')
            sqlite_connection.commit()

        cursor.execute('''
            SELECT * FROM main_names;
        ''')
        rec = cursor.fetchall()
        print(rec)

        cursor.execute('''
            DELETE FROM main_count;
        ''')
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("\nСоединение с SQLite закрыто")
