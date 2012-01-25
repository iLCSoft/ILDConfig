-- GRANT ALL PRIVILEGES ON *.* TO consult IDENTIFIED BY "consult";
GRANT SELECT ON *.* TO consult@'localhost' IDENTIFIED BY 'consult';
GRANT UPDATE, INSERT, DELETE, CREATE, DROP ON `TMP_DB%`.* TO 'consult';
GRANT LOCK TABLES ON `models03`.* TO 'consult';
GRANT UPDATE ON `models03`.`tmp_databases` TO 'consult';
FLUSH PRIVILEGES;
