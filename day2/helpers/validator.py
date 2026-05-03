def is_email_valid(email):
    return '@' in email and '.' in email

def is_password_strong(password):
    return len(password) >=8
