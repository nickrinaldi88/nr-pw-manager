import time
import hashlib
import string
import secrets
import string

# def make_password(salt, pwd):
#     return hashlib.sha256(salt+pwd).hexdigest()


def final_pwd(length):

    chars = string.ascii_lowercase + string.ascii_uppercase + \
        string.digits + string.punctuation

    the_pwd = []

    while len(the_pwd) < length:
        i = secrets.choice(chars)
        the_pwd.append(i)

    return"".join(the_pwd)

