CREATE DATABASE edu_challenge_db CHARACTER SET utf8;
CREATE USER 'edu_challenge_user'@'localhost' IDENTIFIED BY '3duc4';
GRANT ALL PRIVILEGES ON edu_challenge_db.* TO 'edu_challenge_user'@'localhost';