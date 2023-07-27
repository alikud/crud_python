import logging

import psycopg2


# Строка подключения к базе данных PostgreSQL
class Postgres():
    def __init__(self, config) -> None:
        self.conn_string = f"host='localhost' dbname='{config.POSTGRES_DB}' \
            user='{config.POSTGRES_USER}' password='{config.POSTGRES_PASSWORD}'"
        self.conn = psycopg2.connect(self.conn_string)
        self.cur = self.conn.cursor()

    def execute_query(self,query, data=None):
        try:
            if data:
                self.cur.execute(query, data)
            else:
                self.cur.execute(query)
            result = self.cur.fetchall()
            self.conn.commit()
            # self.cur.close()
            # self.conn.close()

            return result
        except Exception as e:
            logging.warning(f"Error with add author data: {e}")
