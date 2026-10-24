import re


def is_valid_login(username):
    return re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{4,16}", username) is not None


if __name__ == "__main__":
    for username in ("user_123", "admin", "123user", "ab", "user-name", "very_long_username"):
        print(f"{username:20} → {is_valid_login(username)}")
