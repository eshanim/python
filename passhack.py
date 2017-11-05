from hashlib import *

def hashPassword(password):
	return sha256(password).hexdigest()
	
