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

the following example adds new roster item with subscription 'both' for user 'kafka'

    api.add_roster("kafka", "franz@example.com", "franz", UserService.SUBSCRIPTION_BOTH)

the following example updates existing roster item to subscription 'none' for user 'kafka'

    api.update_roster("kafka", "franz@example.com", "franz", UserService.SUBSCRIPTION_NONE)

the following example deletes roster item 'franz@kafka.com' for user 'kafka'

    api.delete_roster("kafka", "franz@example.com")


See
===============

* [User Service Plugin Readme](http://www.igniterealtime.org/projects/openfire/plugins/userservice/readme.html)
