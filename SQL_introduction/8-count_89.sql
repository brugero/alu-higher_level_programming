-- Script to display the number of records with id = 89
-- in the table first_table of the specified database.
-- The database name will be passed as an argument to the mysql command.

-- The following line is a comment and will not be executed by MySQL.
-- It shows how the script might be called from the command line:
-- mysql -u <your_username> -p <your_database_name> < path/to/this_script.sql

-- Select the count of records where id is 89 from the first_table.
SELECT COUNT(*) FROM first_table WHERE id = 89;
