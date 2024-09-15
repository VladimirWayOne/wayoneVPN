from utils.db_query import *
from connectors.db_con import PgSQLCon


def check_user(con: PgSQLCon, user_id: int):
    user_exist = con.select(check_user_query(), [user_id])
    if user_exist[0][0] == 0:
        return False
    else:
        return True


def add_user(con: PgSQLCon, user_id: int, fullname: str = None, username: str = None):
    if not check_user(con, user_id):
        con.insert(add_user_query(), [user_id, fullname, username])
