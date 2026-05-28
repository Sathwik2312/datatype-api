import psycopg2

db_host = "dpg-d8c0ctrbc2fs738n8nog-a"
db_user = "datatype_user"
db_password = "atbM4c8RzAA4wlEGg9ueBzi2zHEEeUc2"
db_port = "5432"
db_name = "upd_7g4e"

def db_connection():

    try:

        connection = psycopg2.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            dbname=db_name,
            port=db_port
        )

        return connection

    except Exception as e:

        print("Database connection failed:", e)

        return None