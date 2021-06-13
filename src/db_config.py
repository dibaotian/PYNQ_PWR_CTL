import psycopg2
# USER_TABLE_NAME = "user_table"
# MACHINE_TABLE_NAME = "machine_table"
# RECHARGE_TABLE_NAME = "recharge_table"

# tables = (USER_TABLE_NAME, MACHINE_TABLE_NAME, RECHARGE_TABLE_NAME)

#configuration
HOST_IP = "localhost"
PORT = "5432"
DB_NAME = "powerdb"
USER_NAME = "xilinx"
PASSWORD = "xilinx"


def db_conn_config():
    """ the basic db connection info"""
    db_conn_config = {
        'host': HOST_IP,
        'user': USER_NAME,
        'password': PASSWORD,
        'dbname': DB_NAME,
        'port': PORT
    }

    return db_conn_config