from passlib.context import CryptContext

#object initialized to manage password hashing
#bcrypt is the hasging algorithm
pwd_context = CryptContext(schemes=['bcrypt'])

#hashes pwd when registering
def hash_password(password:str):
    return pwd_context.hash(password)

#verifies when logging in
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)