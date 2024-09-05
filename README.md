# pothole-project
A comprehensive solution to identifying, evaluating, and addressing pot holes in an urban environment 

# LOCAL DEVELOPMENT
## Getting Started
1. Start Your Python Enviornment (First Make Sure You Have Python Installed On Your System):
```shell
$ python -m venv env
```
2. Activate Your Python Enviornment:
```shell
$ source env/bin/activate
```
3. Install all required packages:
```shell
$ pip install -r requirements.txt
```
4. Install MySQL:
```shell
# if you don't have the mysql service already (for mac users)
$ brew install mysql
$ brew services start mysql
```
5. Create a MySQL Database:
```shell
$ mysql -u root
<mysql> CREATE DATABASE local_db;
<mysql> exit;
```
5. Perform the migrations:
```shell
$ python app/manage.py makemigrations
$ python app/manage.py migrate
```
6. Start the server:
```shell
$ python app/manage.py runserver
```

## NOTE: Your database name that you create in MySQL needs to match the .env
