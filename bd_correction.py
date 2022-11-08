import sqlite3

connectinon = sqlite3.connect("for_typing_test.bd")
cursor = connectinon.cursor()

result = cursor.execute(f"SELECT * FROM users WHERE user_name='keysiks';").fetchone()
print(result)