-- Script to update the score of Bob to 10 in the table second_table
-- The database name will be passed as an argument to the mysql command

-- The following line is a comment and will not be executed by MySQL
-- It shows how the script might be called from the command line:
-- mysql -u <your_username> -p <your_database_name> < path/to/this_script.sql

-- Update the score of the record where the name is 'Bob'
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
