import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection



connection = create_connection(
    database = 'ohgamibpdcnDB',
    user = 'ohgami',
    password = 'ohgamiohgami',
    host = 'database-1.cwrf3vhm3q2w.us-west-1.rds.amazonaws.com',
    port = '5432'
)