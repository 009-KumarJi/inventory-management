import os
from dotenv import load_dotenv
import mysql.connector

# Load environment variables from .env file
load_dotenv()

password = os.getenv('sql_pass')
user = os.getenv('sql_user')

cnx = mysql.connector.connect(user=user, password=password,
                              host='127.0.0.1',
                              database='inventory')
cnx.close()
