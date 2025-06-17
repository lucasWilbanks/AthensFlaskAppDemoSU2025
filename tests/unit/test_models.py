from app.models import User

def test_new_user():
	"""
	GIVEN a User model
	WHEN a new User is created
	THEN check the username, email, and password_hash fields are defined correctly
	"""
	user = User('lucas', 'lwilbank@my.athens.edu', 'Qwerty@123!')
	assert user.username == 'lucas'
	assert user.email == 'lwilbank@my.athens.edu'
	assert user.password_hash == 'Qwerty@123!'

def test_setting_password(new_user):
	"""
	GIVEN an existing user
	WHEN the password for the user is set
	THEN check the password is stored correctly and not as plaintext
	"""
	new_user.set_password('MyNewPassword')
	assert new_user.password_hash != 'MyNewPassword'
	assert new_user.check_password('MyNewPassword')
	assert not new_user.check_password('MyNewPassword2')

