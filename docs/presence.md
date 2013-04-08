Usage
===============

Create a new Presence object

	from openfire import Presence

	api = Presence("http://localhost:9090/")

check user status

	api.status("user")
