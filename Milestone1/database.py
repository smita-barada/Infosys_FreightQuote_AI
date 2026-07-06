import sqlite3
import bcrypt
import datetime
import time
import os

DB_NAME = "milestone1.db"
MAX_LOGIN_ATTEMPTS = 3
LOCKOUT_TIME = 300  # 5 minutes in seconds

def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def init_db():
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                email TEXT PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                security_question TEXT NOT NULL,
                security_answer_hash TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS password_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                set_at TEXT NOT NULL,
                FOREIGN KEY(email) REFERENCES users(email) ON DELETE CASCADE
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS login_attempts (
                email TEXT PRIMARY KEY,
                attempts INTEGER DEFAULT 0,
                last_attempt REAL NOT NULL
            )
        """)
        conn.commit()
        
    preseed_users = [
        ("springboardmentor018@gmail.com", "Mentor_018", "Welcome@123", "What is your favourite city?", "bengaluru"),
        ("springboardmentor038@gmail.com", "Mentor_038", "Welcome@123", "What is your pet name?", "shadow")
    ]
    
    for email, username, pwd, sq, sa in preseed_users:
        if not check_user_exists(email) and not check_username_exists(username):
            register_user(email, username, pwd, sq, sa)

def _get_timestamp():
    return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

def hash_text(text):
    return bcrypt.hashpw(text.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_hash(text, hashed):
    if not hashed:
        return False
    try:
        return bcrypt.checkpw(text.encode('utf-8'), hashed.encode('utf-8'))
    except Exception:
        return False

def get_login_attempts(email):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT attempts, last_attempt FROM login_attempts WHERE email = ?", (email,))
        row = c.fetchone()
        return row if row else (0, 0.0)

def increment_login_attempts(email):
    attempts, _ = get_login_attempts(email)
    new_attempts = attempts + 1
    now = time.time()
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("""
            INSERT OR REPLACE INTO login_attempts (email, attempts, last_attempt)
            VALUES (?, ?, ?)
        """, (email, new_attempts, now))
        conn.commit()

def reset_login_attempts(email):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("DELETE FROM login_attempts WHERE email = ?", (email,))
        conn.commit()

def is_rate_limited(email):
    attempts, last_attempt = get_login_attempts(email)
    if attempts >= MAX_LOGIN_ATTEMPTS:
        elapsed = time.time() - last_attempt
        if elapsed < LOCKOUT_TIME:
            return True, int(LOCKOUT_TIME - elapsed)
        else:
            reset_login_attempts(email)
    return False, 0

def check_user_exists(email):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT 1 FROM users WHERE email = ?", (email.lower().strip(),))
        return c.fetchone() is not None

def check_username_exists(username):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT 1 FROM users WHERE LOWER(username) = ?", (username.lower().strip(),))
        return c.fetchone() is not None

def register_user(email, username, password, security_question, security_answer):
    email_clean = email.lower().strip()
    username_clean = username.strip()
    sa_clean = security_answer.lower().strip()
    
    pwd_hashed = hash_text(password)
    sa_hashed = hash_text(sa_clean)
    now = _get_timestamp()
    
    with get_connection() as conn:
        c = conn.cursor()
        try:
            c.execute("""
                INSERT INTO users (email, username, password_hash, security_question, security_answer_hash, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (email_clean, username_clean, pwd_hashed, security_question, sa_hashed, now))
            c.execute("""
                INSERT INTO password_history (email, password_hash, set_at)
                VALUES (?, ?, ?)
            """, (email_clean, pwd_hashed, now))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

def authenticate_user(email, password):
    email_clean = email.lower().strip()
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT password_hash FROM users WHERE email = ?", (email_clean,))
        row = c.fetchone()
    if row:
        stored_hash = row[0]
        if check_hash(password, stored_hash):
            reset_login_attempts(email_clean)
            return True
    increment_login_attempts(email_clean)
    return False

def get_user_by_email(email):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT username, security_question, security_answer_hash FROM users WHERE email = ?", (email.lower().strip(),))
        return c.fetchone()

def check_password_reused(email, new_password):
    email_clean = email.lower().strip()
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT password_hash FROM password_history WHERE email = ?", (email_clean,))
        history = c.fetchall()
    for (stored_hash,) in history:
        if check_hash(new_password, stored_hash):
            return True
    return False

def update_password(email, new_password):
    email_clean = email.lower().strip()
    pwd_hashed = hash_text(new_password)
    now = _get_timestamp()
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("UPDATE users SET password_hash = ? WHERE email = ?", (pwd_hashed, email_clean))
        c.execute("INSERT INTO password_history (email, password_hash, set_at) VALUES (?, ?, ?)", (email_clean, pwd_hashed, now))
        conn.commit()

def get_all_users():
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT username, email, created_at FROM users")
        return c.fetchall()

def delete_user(email):
    email_clean = email.lower().strip()
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE email = ?", (email_clean,))
        c.execute("DELETE FROM password_history WHERE email = ?", (email_clean,))
        c.execute("DELETE FROM login_attempts WHERE email = ?", (email_clean,))
        conn.commit()
        return True
