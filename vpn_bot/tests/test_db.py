import unittest
from connectors.db_con import PgSQLCon
from dotenv import load_dotenv
import os
load_dotenv()


class TestDBMetrhods(unittest.TestCase):
    def test_connect(self):
        db_con = PgSQLCon(dbname=os.getenv("DB_USER"), usr=os.getenv("DB_USER"), pwd=os.getenv(
            "DB_PWD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))
        result = db_con.select('SELECT 1')
        print(result)
        self.assertTrue('FOO'.isupper())
