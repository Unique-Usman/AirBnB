CREATE DATABASE
IF NOT EXISTS
hbnb_test_db;

CREATE USER
IF NOT EXISTS
'hbnb_dev'@'localhost'
IDENTIFIED WITH
mysql_native_password BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES
ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT
ON performance_schema.* TO 'hbnb_dev'@'localhost';
