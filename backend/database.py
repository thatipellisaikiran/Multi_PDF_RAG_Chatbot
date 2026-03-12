import sqlite3
import os

# create database folder
os.makedirs("data", exist_ok=True)

DB_PATH = "data/chat.db"

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS chats(
id INTEGER PRIMARY KEY AUTOINCREMENT,
question TEXT,
answer TEXT
)
""")

conn.commit()


# function to save chat
def save_chat(question, answer):
    cursor.execute(
        "INSERT INTO chats (question, answer) VALUES (?, ?)",
        (question, answer)
    )
    conn.commit()


# function to load chat history
def load_chats():
    cursor.execute("SELECT * FROM chats")
    return cursor.fetchall()