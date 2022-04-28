# import sqlalchemy
from traceback import print_tb
from sqlalchemy import null
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3


# ____________ SQLLite database connection _______________-
cnt = sqlite3.connect("password.db")
cnt.execute('''CREATE TABLE IF NOT EXISTS password ( password TEXT)''')
cnt.execute('''CREATE TABLE IF NOT EXISTS configuration ( website TEXT, email TEXT, password TEXT,hash_password TEXT)''')
cnt.cursor()

def get_password_dataBase():
	records = cnt.execute("SELECT password FROM password")
	return records

def get_configuration_dataBase():
	return cnt.execute("SELECT * FROM configuration")


def check_matches_passwords(password1,password2):
	if password1 == password2:
		return True
	return False


def insert_password(password):
	cnt.execute("INSERT INTO password VALUES (:password)", {
		'password': generate_password_hash(password)})
	cnt.commit()

def insert_details(website,email,password):
	cnt.execute("INSERT INTO configuration VALUES (:website, :email, :password, :hash_password)", {
		'website': website,
		'email': email,
		'password': password,
		'hash_password':len(password) * '*'
	})
	cnt.commit()

def delete_details(name):
	try:
		print("db.py : " + name)
		print(len(name))
		cnt.execute("DELETE FROM configuration WHERE website=(?)", (name,))
		cnt.commit()
	except Exception as e:
		print(e)

def print_dataBase():
	for i in cnt.execute("SELECT * FROM configuration"):
		print(i)
def if_password_exist():
	try:
		password = cnt.execute("SELECT password FROM password")
		password = list(password)
		password = password[0]
		print(password)
		if password != null:
			print("True")
			return True

	except IndexError as error:
		print(error)
		return False

