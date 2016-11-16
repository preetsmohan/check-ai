DROP DATABASE IF EXISTS checkai;
CREATE DATABASE checkai;

USE checkai;
CREATE TABLE user (uid INT NOT NULL AUTO_INCREMENT, username VARCHAR(30), password VARCHAR(30), skills VARCHAR(256), exclusions VARCHAR(256), postype VARCHAR(128), field VARCHAR(128), explevel VARCHAR(20), PRIMARY KEY (uid) );
