import os
import gnupg
from os.path import expanduser
import getpass

home = expanduser("~")
gpghome = os.path.join(home, 'gpghome')

def gpg_initialize():

	if not os.path.exists(gpghome):
		sos.makedirs(gpghome)
	
	gpg = gnupg.GPG(gnupghome=gpghome)
	
	email = raw_input('Email: ')
	pw = getpass.getpass()

	input_data = gpg.gen_key_input(
		name_email=email,
		passphrase=pw)
	
	key = gpg.gen_key(input_data)
	return key

def gpg_export_keys(key):

	gpg = gnupg.GPG(gnupghome=gpghome)

	ascii_armored_public_keys = gpg.export_keys(key)
	ascii_armored_private_keys = gpg.export_keys(key, True)
	
	with open('keyfile.asc', 'w') as f:
		f.write(ascii_armored_public_keys)
		f.write(ascii_armored_private_keys)

def gpg_import_keys():
	gpg = gnupg.GPG(gnupghome=gpghome)
	key_data = open('keyfile.asc').read()
	import_result = gpg.import_keys(key_data)

def gpg_encrypt_string(unencrypted_string):
	gpg = gnupg.GPG(gnupghome=gpghome)
	
	email = raw_input('Email: ')
	encrypted_data = gpg.encrypt(unencrypted_string, email)
	encrypted_string = str(encrypted_data)
	print 'ok: ', encrypted_data.ok
	print 'status: ', encrypted_data.status
	print 'stderr: ', encrypted_data.stderr
	print 'unencrypted_string: ', unencrypted_string
	print 'encrypted_string: ', encrypted_string

	return encrypted_string


