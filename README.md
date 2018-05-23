# psngr

Project to serve CSV data over DJANGO REST API.

Installation & Run

1. Create virtual environment with python3.6

2. Install project package from project folder `pip install -r requirements.txt`

3. Load fixtures for default details  `python manage.py loaddata fixtures/*`

4. To execute project on local server run following command in virutal env
	
	`python manage.py runserver`

NOTE: 2 Default superuser created
	
username : siddhesh

password : sidh@123

username : rotem

password : rote@123


Features

1. Secure API with token autentication system.

3. `STORE_IN_CACHE` varible in settings, if True - loads CSV on app load else loads on each rest call.

2. Fetch Cache data with `/data-list`.

3. Fetch dynamic data from csv file using `dynamic-data-list`

4. Read data from database `store-data-list`

4. Query parameter :-  `title` and `description` also implemented in all three API.


PROS and CONS of above three API implementation

1. `/data-list`
	
	PROS:

		1. Data store in memory. Hence performance is very fast.

	CONS:
		1. Memory filled with CSV file data.
		2. New CSV file data not store in memory.


2. `dynamic-data-list`

	PROS:
		1. Only required data read from CSV file. Less data access from file.
		2. Updated CSV file data get in list

	CONS:
		1. Each time data read from csv file
		2. Performance issue

3. `store-data-list`
	
	PROS:
		1. Data store in database. Less memory used
		2. Fast data access also based on requirement data fetch from database.

	CONS:
		1. New CSV file data not store in memory.


Assumptions

1. No. of records in CSV are considered to be very small (25 in this case). Hence pagination is not implemented.
