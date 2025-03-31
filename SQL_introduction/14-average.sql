-- Script to compute the score average of all records
-- in the table second_table of the specified database.
-- The result column name should be average.
-- The database name will be passed as an argument to the mysql command.

-- The following line is a comment and will not be executed by MySQL.
-- It shows how the script might be called from the command line:
-- mysql -u <your_username> -p <your_database_name> < path/to/this_script.sql

-- Calculate the average score and alias the result column as 'average'.
SELECT AVG(score) AS average
FROM second_table;
