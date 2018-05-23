# psngr

Project to serve CSV data over DJANGO REST API.

Installation

1. Create virtual environment with python3.6

2. Install project package from project folder `pip install -r requirements.txt`

3. Load fixtures for default details  `python manage.py loaddata fixtures/*`

NOTE: 2 Default superuser created
	
username : siddhesh

password : sidh@123

username : rotem

password : rote@123


Features

1. Secure API with token autentication system.

2. Fetch data with `/data-list`.

3. `STORE_IN_CACHE` varible in settings, if True - loads CSV on app load else loads on each rest call.

4. Query parameter :-  `title` and `description` also implemented.

Assumptions

1. No. of records in CSV are considered to be very small (25 in this case). Hence pagination is not implemented.