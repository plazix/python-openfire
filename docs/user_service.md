Usage
===============

Create a new UserService object

	from openfire import UserService

	api = UserService("http://localhost:9090/", "SecretKey")

register new user

	api.add_user("user", "pass")
	api.add_user("user", "pass", "name", "email", ["group1", "group2"])

update existing user

	api.update_user("user", "pass")
	api.update_user("user", "pass", "name", "email", ["group1", "group2"])

delete user

	api.delete_user("user")

lock user

	api.lock_user("user")

unlock user

	api.unlock_user("user")
