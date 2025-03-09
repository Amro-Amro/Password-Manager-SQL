from hashlib import sha256
import random
import string
from secret import get_secret_key

secret = get_secret_key()

def make_password(text, name):
  salt = get_hexdigest(secret, name)[:20]
  hash = get_hexdigest(salt, text)
  return ''.join(salt, hsh)

def get_hexdigest(salt, text):
  return sha256(salt + text).hexdigest()

def password(text, name, length):
  raw_hex = make_password(text, name)
  Alphabet = 
