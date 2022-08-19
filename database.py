from os import environ
import pymysql

# connection to mysql db
db = pymysql.connect(host=environ.get('DB_HOSTNAME'),
                     user=environ.get('DB_USERNAME'),
                     password=environ.get('DB_PASSWORD'),
                     database=environ.get('DB_NAME'))
