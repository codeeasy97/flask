##  Step 1: Update/Upgrade Package Repository
```
sudo apt update
sudo apt upgrade
```
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-install-img/1.png?raw=true)

##  Step 2: Install MySQL
```
sudo apt install mysql-server
sudo systemctl start mysql.service
mysql --version
```
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-install-img/2.png?raw=true)
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-install-img/3.png?raw=true)
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-install-img/4.png?raw=true)

##  Step 3: Securing MySQL
```
sudo mysql_secure_installation
```
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-install-img/5-1.png?raw=true)
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-install-img/5-2.png?raw=true)

##  Step 4: Check if MySQL Service Is Running
```
sudo systemctl status mysql
```
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-install-img/6.png?raw=true)

##  Step 5: Log in to MySQL Server
```
sudo mysql -u root
```
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-install-img/7.png?raw=true)

##  Run MySql Queries
```
create a new database
create database ecom_project;

use any database
use ecom_project;

create new table
create table product(id int(10) auto_increment primary key,name varchar(),price float,created_at datetime,is_active tinyint);

view all tables in a database
show tables;

view records
select * from product;

insert 2 records to table
insert into product(name,price,created_at)values("red color t-shirt",200,NOW());
insert into product(name,price,created_at)values("golden watch",24500,NOW());

to view table data
select * from product;

to update all records
update product set is_active=1;

to update specific row
update product set is_active=0 where id=1;
```
####    Find Images Below
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-install-img/8.png?raw=true)
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-install-img/9.png?raw=true)
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-install-img/10.png?raw=true)

### Where does MySql store password validation
```
SHOW VARIABLES LIKE 'validate_password%';
SET GLOBAL validate_password.length = 6;
SET GLOBAL validate_password.number_count = 0;
SET GLOBAL validate_password.policy = LOW
```