import random
import string

def generate_email():
    return f"user_{random.randint(1000,9999)}@example.com"

def generate_name(length=6):
    return ''.join(random.choices(string.ascii_letters, k=length))
