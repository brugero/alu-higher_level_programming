-- Script to remove all records with a score <= 5
-- in the table second_table of the specified database.
-- The database name will be passed as an argument to the mysql command.

-- The following line is a comment and will not be executed by MySQL.
-- It shows how the script might be called from the command line:
-- mysql -u <your_username> -p <your_database_name> < path/to/this_script.sql

-- Delete records from second_table where the score is less than or equal to 5.
DELETE FROM second_table
WHERE score <= 5;
