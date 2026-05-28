import psycopg2

db_host = "host.docker.internal"
db_user = "postgres"
db_password = "1234"
db_port = "5432"
db_name = "upd"

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