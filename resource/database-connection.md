##  Step 1: Installing the Flask MySQL library
```
pip3 install flask_mysqldb
```
#### If error comes like below img
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-connect-flask/1.png?raw=true)

#### solve error - run commands
```
mysql_config --version
sudo apt install libmysqlclient-dev
sudo apt install libmariadb-dev-compat

```
#### Now Run command again
```
pip3 install flask_mysqldb
```


## Step 2: Connecting a Flask Application to a MySQL Database - in main.py file
```
from flask_mysqldb import MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' ## This is what you have set during mysql installation
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)
```

##  Step 2: Configuring the MySQL Connection Cursor - In view file (account.py)
```
from main.app import mysql

#Creating a connection cursor
cursor = mysql.connection.cursor()
 
#Executing SQL Statements
cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')
cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
cursor.execute(''' DELETE FROM table_name WHERE condition ''')
 
#Saving the Actions performed on the DB
mysql.connection.commit()
 
#Closing the cursor
cursor.close()