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