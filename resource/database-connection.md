##  Step 1: Installing the Flask MySQL library
```
pip3 install flask-mysqldb
```
#### If error comes like below img
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-connect-flask/1.png?raw=true)

#### To solve error - run below commands
```
mysql_config --version
sudo apt install libmysqlclient-dev
sudo apt install libmariadb-dev-compat

```
#### Now Run command again
```
pip3 install flask-mysqldb
```


## Step 2: Connecting a Flask Application to a MySQL Database - in main.py file

#####    Add below line in top of the main.py file ignore if already exist
```
from flask import Flask, render_template, request, session, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
app = Flask(__name__)
app.secret_key = 'jhfiwerhe894rwhkfwgf93u2rjkbnhiuh@Hhejvwh'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'multishop'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
```

##  Step3: Open Terminal/CMD OR any mysql client like (mysql-workbench) and Run Query

```
CREATE DATABASE IF NOT EXISTS multi_db;

CREATE TABLE IF NOT EXISTS accounts(id int(11) PRIMARY KEY AUTO_INCREMENT,
first_name varchar(50),last_name varchar(50),
email varchar(50),mobile varchar(10),
password varchar(255),
is_active tinyint,
created_at datetime default CURRENT_TIMESTAMP,
updated_at datetime);

INSERT INTO accounts(first_name, last_name, email, mobile, password) 
VALUES 
('rahul', 'dev', 'deepak@gmail.com','8826220876',"123456");
```
##  Step4: In main.py file create function to handle form submit

```
@app.route('/signup', methods=['GET', 'POST'])
def register():
  if request.method == "POST":
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["mobile"]
    mobile = request.form["email"]
    password = request.form["password"]
    confirm_password = request.form["confirm_password"]
    print(first_name,last_name,email,mobile,password, confirm_password)
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM accounts WHERE email = %s', (email,))
    account = cursor.fetchone()
    
    if account:
        flash("'Account already exists!'","error")
    else:
        cursor.execute('INSERT INTO accounts(first_name,last_name, email, mobile, password) VALUES (%s, %s, %s, %s, %s)', (first_name, last_name, email, mobile, password))
        mysql.connection.commit()
        flash("You have successfully registered!","success")
  return render_template("signup.html")
```


#### To kill port run below command(change port number)
```
sudo kill -9 $(sudo lsof -t -i:5000)
```
### The END! You are successfully registered.