-- Creates the database hbtn_0d_usa and the table states in it
-- Creates the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Creates the table states with an auto-generated primary key id
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
