import os
import logging
from dotenv import load_dotenv
import mysql.connector

load_dotenv()


class DatabaseConnection:
    def __init__(self):
        self.cnx = None

    def connect(self):
        if self.cnx is None:
            try:
                self.cnx = mysql.connector.connect(
                    user=os.getenv('sql_user'),
                    password=os.getenv('sql_pass'),
                    host=os.getenv('sql_host'),
                    database=os.getenv('sql_database')
                )
                logging.info("Connected to database")
            except mysql.connector.Error as err:
                logging.error(f"Failed to connect to database: {err}")
                raise
        return self.cnx

    def disconnect(self):
        if self.cnx is not None:
            try:
                self.cnx.close()
                logging.info("Closed database connection")
            except mysql.connector.Error as err:
                logging.error(f"Failed to close database connection: {err}")
                raise
