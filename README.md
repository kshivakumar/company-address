**Environment Setup (Python 3)**
1. cd into the project directory(CompanyAddress)  
2. Create and activate virtualenv - `virtualenv venv; source venv/bin/activate`  
3. Install the requirements - `pip install -r requirements.txt`  
4. Configure Database - `python manage.py migrate`  
5. Load dummy data into sqlite DB - `sqlite3 db.sqlite3`, Inside sqlite3 shell - `.read data.sql`  
6. Start Django Dev Server - `python manage.py runserver 0:8000`  

Optional:
Run test cases - `python manage.py test address`
PEP8 checks - `flake8 CompanyAddress/ --exclude=migrations`


**API description**  
root_url : http://localhost:8000

GET  	`/address/` - get all addresses  
POST 	`/address/` - add a new address(all address fields should be present in the payload)  

GET  	`/address/2/` - get the address row with id = 2  
PUT  	`/address/2/` - update one or more address fields of an address with id = 2 (payload should contain all the fields)  
DELETE  `/address/2/` - delete the address row with id = 2  

GET 	`/address/company/My Company/` - get addresses of company - My Company  
GET 	`/address/city/MyCity/` - get companies in MyCity  
GET 	`/address/getPostalCodes?companiesCountGreaterThan=2` - get postal codes where number of companies is greater than 2  

Please note the trailing `/` in most of the urls. Missing the trailing slash will cause Django to return - `Page Not Found` error.
