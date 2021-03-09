import string
import secrets
import string


def custom_pwd(length):

    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))


def final_pwd(length):

    chars = string.ascii_lowercase + string.ascii_uppercase + \
        string.digits + string.punctuation

    return "".join(secrets.choice(chars) for _ in range(length))
