
from hashlib import sha256

token = sha256('QNAP@123'.encode('ascii')).hexdigest()
print('token------: X-AppIToken', token)