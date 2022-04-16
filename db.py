# import sqlalchemy
from traceback import print_tb
from sqlalchemy import null
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3

# ____________ SQLLite database connection _______________-
cnt = sqlite3.connect("password.db")
cnt.execute('''CREATE TABLE IF NOT EXISTS password ( password TEXT)''')
cnt.cursor()

def get_dataBase():
	records = cnt.execute("SELECT password FROM password")
	return records
def check_matches_passwords(password1,password2):
	if password1 == password2:
		return True
	return False
def insert_password(password):
	cnt.execute("INSERT INTO password VALUES (:password)", {
		'password': generate_password_hash(password)})
	cnt.commit()

def if_password_exist():
	password = cnt.execute("SELECT password FROM password")
	password = list(password)
	password = password[0]
	print(password)
	if password != null:
		print("True")
		return True
	return False