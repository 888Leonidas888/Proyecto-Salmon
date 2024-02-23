-- Se crea base de datos y usuario para el sistema de abastecimiento.
-- Configure las credenciales en el .bashrc.

CREATE DATABASE IF NOT EXISTS abast_dev_db;
CREATE USER IF NOT EXISTS 'abast_dev'@'localhost' IDENTIFIED BY 'UvQ7PAgVRI';
GRANT ALL PRIVILEGES ON abast_dev_db.* TO 'abast_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'abast_dev'@'localhost';
