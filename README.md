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


DOCKER RUN

1. First install docker and docker-compose in your system (Docker dependancies)
	
	`sudo apt-get install docker`

	`sudo apt-get install docker-compose`

2. Perform `docker-compose build` command to install project dependancies inside project path

3. Run `docker-compose up` command to run project on localhost:8000

4. To close docker run `docker-compose down`


Features

1. Secure API with token autentication system.

3. `STORE_IN_CACHE` varible in settings, if True - loads CSV on app load else loads on each rest call.

2. Fetch Cache data with `/data-list`.

3. Fetch dynamic data from csv file using `dynamic-data-list`

4. Read data from database `store-data-list`

5. Query parameter :- `title` and `description` also implemented in all three API.

6. `SOFT_IMAGE_VALIDATION` to check image url contains image types name. If not replace with `DEFAULT_IMAGE_URL`.


Assumptions,Pros and Cons of above three API implementation

1. `/data-list`
	
	Assumption
		1. CSV file data is static.
		2. To increase API performance, data store in memory

	PROS:

		1. API performance is very fast.

	CONS:
		1. Memory filled with CSV file data(size of csv file data == size of memory used).
		2. New CSV file data not store in memory.


2. `dynamic-data-list`
	
	Assumption
		1. CSV file data is dynamic.
		2. Read specific line of data from CSV file.

	PROS:
		1. Specific line of rows read from CSV file. Hence less memory use.
		2. Updated CSV file data get in list

	CONS:
		1. Each time data read from csv file.
		2. Slow performance compare to above API.
		3. API response time increase.

3. `store-data-list`
	
	Assumption
		1. CSV file data is static.
		2. To increase API performance, data store in database

	PROS:
		1. Data store in database. Less memory used.
		2. Moderate API performance compare to `data-list`.

	CONS:
		1. New CSV file data not store in memory. (This can be removed by using celery delay function which fetch and load new data in database after specific interval)

