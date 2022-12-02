-- script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
ALTER DATABASE hbtn_0c_0
READ ONLY = 0
DEFAULT COLLATE utf8mb4_unicode_ci
;

ALTER TABLE hbtn_0c_0.first_table
MODIFY id INT(11),
MODIFY name varchar(256)
COLLATE utf8mb4_unicode_ci
